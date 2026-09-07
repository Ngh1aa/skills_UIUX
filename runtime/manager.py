from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from runtime.agent import ProviderNeutralAgentHarness, RunState
from runtime.flow import DevelopmentManager, ReplanDecision, ResolvedFlow, ResolvedStage
from runtime.providers import (
    ProviderAdapter,
    ProviderError,
    ProviderStagePlan,
    ProviderStageRequest,
    tool_contracts,
)
from runtime.task_context import GoalInterpreter


@dataclass
class ManagedWebsiteRun:
    manager_run_id: str
    flow: ResolvedFlow
    task_context: dict[str, Any]
    authority: str
    active_stage: str
    state: str = "READY"
    replan_count: int = 0
    completed_stages: list[str] = field(default_factory=list)
    stage_runs: dict[str, list[str]] = field(default_factory=dict)
    replan_history: list[dict[str, Any]] = field(default_factory=list)
    approved_gates: list[str] = field(default_factory=list)
    gate_evidence: dict[str, list[dict[str, Any]]] = field(default_factory=dict)
    provider_history: list[dict[str, Any]] = field(default_factory=list)

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "ManagedWebsiteRun":
        flow_payload = dict(payload["flow"])
        stages = [ResolvedStage(**dict(item)) for item in flow_payload.pop("stages", [])]
        flow = ResolvedFlow(stages=stages, **flow_payload)
        return cls(
            manager_run_id=str(payload["manager_run_id"]),
            flow=flow,
            task_context=dict(payload.get("task_context", {})),
            authority=str(payload["authority"]),
            active_stage=str(payload["active_stage"]),
            state=str(payload.get("state", "READY")),
            replan_count=int(payload.get("replan_count", 0)),
            completed_stages=list(payload.get("completed_stages", [])),
            stage_runs={key: list(value) for key, value in dict(payload.get("stage_runs", {})).items()},
            replan_history=list(payload.get("replan_history", [])),
            approved_gates=list(payload.get("approved_gates", [])),
            gate_evidence={
                key: [dict(item) for item in value]
                for key, value in dict(payload.get("gate_evidence", {})).items()
            },
            provider_history=[dict(item) for item in payload.get("provider_history", [])],
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "manager_run_id": self.manager_run_id,
            "flow": self.flow.to_dict(),
            "task_context": self.task_context,
            "authority": self.authority,
            "active_stage": self.active_stage,
            "state": self.state,
            "replan_count": self.replan_count,
            "completed_stages": list(self.completed_stages),
            "stage_runs": {key: list(value) for key, value in self.stage_runs.items()},
            "replan_history": list(self.replan_history),
            "approved_gates": list(self.approved_gates),
            "gate_evidence": {
                key: [dict(item) for item in value] for key, value in self.gate_evidence.items()
            },
            "provider_history": [dict(item) for item in self.provider_history],
        }


class DevelopmentManagerAgent:
    """Owns end-to-end website routing while specialist agents own execution stages.

    The manager interprets the user's goal, resolves a declarative flow, activates
    specialist runs, asks a configured provider to execute only the active stage,
    verifies provider gate evidence, enforces human approvals, checkpoints state,
    and applies bounded replans instead of blind retries.
    """

    def __init__(self, harness: ProviderNeutralAgentHarness) -> None:
        self.harness = harness
        self.manager = DevelopmentManager(harness.repo_root, harness.policy_doc)
        self.goal_interpreter = GoalInterpreter()

    def interpret_goal(
        self,
        goal: str,
        overrides: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        context = self.goal_interpreter.interpret(goal).to_context()
        context["goal"] = goal
        for key, value in dict(overrides or {}).items():
            if value is None:
                continue
            if key == "features":
                if value:
                    context[key] = list(value)
                continue
            context[key] = value
        context.setdefault("approval_mode", "auto")
        return context

    def resolve_flow(
        self,
        task_context: dict[str, Any],
        additional_skills: list[str] | None = None,
        exclude_skills: list[str] | None = None,
    ) -> ResolvedFlow:
        return self.manager.plan(
            task_context,
            additional_skills=additional_skills,
            exclude_skills=exclude_skills,
        )

    def _stage(self, managed: ManagedWebsiteRun, stage_id: str) -> ResolvedStage:
        stage = next((item for item in managed.flow.stages if item.id == stage_id), None)
        if stage is None:
            raise ValueError(f"unknown stage for flow {managed.flow.id}: {stage_id}")
        return stage

    def _checkpoint_managed(self, managed: ManagedWebsiteRun) -> None:
        state = self.harness.resume(managed.manager_run_id)
        state.state = managed.state
        state.context["flow_plan"] = managed.flow.to_dict()
        state.context["task_context"] = dict(managed.task_context)
        state.context["managed_run"] = managed.to_dict()
        self.harness.checkpoints.save(state.run_id, state.to_dict())

    def resume(self, manager_run_id: str) -> ManagedWebsiteRun:
        state = self.harness.resume(manager_run_id)
        payload = state.context.get("managed_run")
        if not isinstance(payload, dict):
            raise ValueError(f"checkpoint {manager_run_id} does not contain a managed website run")
        return ManagedWebsiteRun.from_dict(payload)

    def start_from_goal(
        self,
        goal: str,
        authority: str = "branch_write",
        overrides: dict[str, Any] | None = None,
        additional_skills: list[str] | None = None,
        exclude_skills: list[str] | None = None,
    ) -> ManagedWebsiteRun:
        context = self.interpret_goal(goal, overrides)
        return self.start(
            goal,
            context,
            authority=authority,
            additional_skills=additional_skills,
            exclude_skills=exclude_skills,
        )

    def start(
        self,
        task: str,
        task_context: dict[str, Any],
        authority: str = "branch_write",
        additional_skills: list[str] | None = None,
        exclude_skills: list[str] | None = None,
    ) -> ManagedWebsiteRun:
        flow = self.resolve_flow(task_context, additional_skills, exclude_skills)
        manager_state = self.harness.create_run(
            task,
            "development",
            authority,
            selected_skills=[],
            explicit_sources=[],
        )
        managed = ManagedWebsiteRun(
            manager_run_id=manager_state.run_id,
            flow=flow,
            task_context=dict(task_context),
            authority=authority,
            active_stage=flow.stages[0].id,
        )
        self._checkpoint_managed(managed)
        return managed

    def start_stage(
        self,
        managed: ManagedWebsiteRun,
        stage_id: str | None = None,
        explicit_sources: list[str] | None = None,
    ) -> RunState:
        target = stage_id or managed.active_stage
        if target != managed.active_stage:
            raise ValueError(
                f"cannot start stage {target}; active stage is {managed.active_stage}. "
                "Complete the active stage or apply an explicit replan first."
            )
        stage = self._stage(managed, target)

        role = self.harness.policy_doc["roles"][stage.agent]
        order = tuple(self.harness.permissions.order)
        authority = managed.authority
        if order.index(authority) > order.index(role["max_authority"]):
            authority = role["max_authority"]

        state = self.harness.create_run(
            task=f"{managed.flow.id}:{stage.id}",
            agent=stage.agent,
            authority=authority,
            selected_skills=stage.skills,
            explicit_sources=explicit_sources or [],
        )
        state.context["manager_run_id"] = managed.manager_run_id
        state.context["flow_id"] = managed.flow.id
        state.context["flow_revision"] = managed.flow.revision
        state.context["stage_id"] = stage.id
        state.context["stage_gates"] = list(stage.gates)
        self.harness.checkpoints.save(state.run_id, state.to_dict())

        managed.active_stage = stage.id
        managed.state = "RUNNING"
        managed.stage_runs.setdefault(stage.id, []).append(state.run_id)
        self._checkpoint_managed(managed)
        return state

    def required_human_approvals(self, managed: ManagedWebsiteRun, stage_id: str | None = None) -> list[str]:
        if str(managed.task_context.get("approval_mode", "auto")) != "manual":
            return []
        stage = self._stage(managed, stage_id or managed.active_stage)
        required: list[str] = []
        for gate in stage.gates:
            if gate.get("approval") == "human" and str(gate.get("id", "")) not in managed.approved_gates:
                required.append(str(gate["id"]))
        return required

    def approve_gate(self, managed: ManagedWebsiteRun, gate_id: str) -> None:
        stage = self._stage(managed, managed.active_stage)
        gate = next((item for item in stage.gates if str(item.get("id", "")) == gate_id), None)
        if gate is None:
            raise ValueError(f"gate {gate_id} is not part of active stage {stage.id}")
        if gate.get("approval") != "human":
            raise ValueError(f"gate {gate_id} does not require human approval")
        if gate_id not in managed.approved_gates:
            managed.approved_gates.append(gate_id)
        self._checkpoint_managed(managed)

    def complete_stage(self, managed: ManagedWebsiteRun, stage_id: str | None = None) -> str | None:
        target = stage_id or managed.active_stage
        if target != managed.active_stage:
            raise ValueError(
                f"cannot complete stage {target}; active stage is {managed.active_stage}"
            )
        self._stage(managed, target)
        pending = self.required_human_approvals(managed, target)
        if pending:
            managed.state = "AWAITING_APPROVAL"
            self._checkpoint_managed(managed)
            raise ValueError(
                f"cannot complete stage {target}; human approval required for gate(s): {', '.join(pending)}"
            )

        runs = managed.stage_runs.get(target, [])
        if not runs:
            raise ValueError(f"cannot complete stage {target}; no specialist run has been started")
        latest = self.harness.resume(runs[-1])
        if latest.state != "COMPLETED":
            raise ValueError(
                f"cannot complete stage {target}; latest specialist run is {latest.state}"
            )
        if target not in managed.completed_stages:
            managed.completed_stages.append(target)

        stage_ids = [stage.id for stage in managed.flow.stages]
        index = stage_ids.index(target)
        if index == len(stage_ids) - 1:
            managed.state = "COMPLETED"
            managed.active_stage = target
            self._checkpoint_managed(managed)
            return None

        managed.active_stage = stage_ids[index + 1]
        managed.state = "READY"
        self._checkpoint_managed(managed)
        return managed.active_stage

    def replan(
        self,
        managed: ManagedWebsiteRun,
        signal: str,
        current_stage: str | None = None,
        replan_count: int | None = None,
        context_updates: dict[str, Any] | None = None,
        apply: bool = True,
    ) -> ReplanDecision:
        stage_id = current_stage or managed.active_stage
        self._stage(managed, stage_id)
        if apply and stage_id != managed.active_stage:
            raise ValueError(
                f"cannot apply replan from stage {stage_id}; active stage is {managed.active_stage}"
            )

        context = dict(managed.task_context)
        context.update(context_updates or {})
        context["current_stage"] = stage_id
        effective_count = managed.replan_count if replan_count is None else replan_count
        decision = self.manager.replan(
            managed.flow,
            signal=signal,
            context=context,
            replan_count=effective_count,
        )

        if decision.accepted and apply:
            managed.flow = self.manager.apply_replan(managed.flow, decision)
            managed.replan_count += 1
            managed.replan_history.append(decision.to_dict())
            managed.state = "REPLANNED"

            target = decision.target_stage or stage_id
            managed.active_stage = target
            stage_ids = [stage.id for stage in managed.flow.stages]
            target_index = stage_ids.index(target)
            managed.completed_stages = [
                item
                for item in managed.completed_stages
                if stage_ids.index(item) < target_index
            ]
            managed.gate_evidence = {
                key: value
                for key, value in managed.gate_evidence.items()
                if key in stage_ids and stage_ids.index(key) < target_index
            }
            self._checkpoint_managed(managed)

        return decision

    def _provider_request(
        self,
        managed: ManagedWebsiteRun,
        state: RunState,
        *,
        round_index: int,
        max_rounds: int,
    ) -> ProviderStageRequest:
        stage = self._stage(managed, managed.active_stage)
        return ProviderStageRequest(
            goal=str(managed.task_context.get("goal", "UIUX website task")),
            flow_id=managed.flow.id,
            flow_revision=managed.flow.revision,
            stage_id=stage.id,
            agent=stage.agent,
            authority=state.authority,
            purpose=stage.purpose,
            skills=list(stage.skills),
            gates=list(stage.gates),
            task_context=dict(managed.task_context),
            project_root=str(self.harness.project_root),
            context_manifest=dict(state.context),
            observations=[dict(item) for item in state.observations],
            tools=tool_contracts(self.harness.registry),
            round_index=round_index,
            max_rounds=max_rounds,
        )

    def _record_provider_plan(
        self,
        managed: ManagedWebsiteRun,
        state: RunState,
        plan: ProviderStagePlan,
        round_index: int,
    ) -> None:
        row = {
            "stage": managed.active_stage,
            "stage_run_id": state.run_id,
            "flow_revision": managed.flow.revision,
            "round": round_index,
            "provider": plan.provider,
            "model": plan.model,
            "request_id": plan.request_id,
            "status": plan.status,
            "signal": plan.signal,
            "summary": plan.summary,
            "reason": plan.reason,
            "tools": [str(action.get("tool", "")) for action in plan.actions],
            "gate_evidence": [item.to_dict() for item in plan.gate_evidence],
        }
        managed.provider_history.append(row)
        state.context["provider"] = {
            "name": plan.provider,
            "model": plan.model,
            "last_request_id": plan.request_id,
            "last_status": plan.status,
            "round": round_index,
        }
        self.harness.checkpoints.save(state.run_id, state.to_dict())
        self._checkpoint_managed(managed)

    def _verify_gate_evidence(
        self,
        managed: ManagedWebsiteRun,
        state: RunState,
        plan: ProviderStagePlan,
    ) -> list[dict[str, Any]]:
        stage = self._stage(managed, managed.active_stage)
        gate_ids = [str(item.get("id", "")) for item in stage.gates if item.get("id")]
        by_gate: dict[str, list[Any]] = {gate_id: [] for gate_id in gate_ids}
        for evidence in plan.gate_evidence:
            if evidence.gate_id in by_gate:
                by_gate[evidence.gate_id].append(evidence)

        observations = {str(item.get("id", "")): item for item in state.observations}
        verified: list[dict[str, Any]] = []
        project_root = self.harness.project_root.resolve()

        for gate_id in gate_ids:
            candidates = by_gate.get(gate_id, [])
            if not candidates:
                raise ValueError(f"provider PASS missing evidence for gate: {gate_id}")

            accepted: dict[str, Any] | None = None
            for evidence in candidates:
                if evidence.kind == "artifact":
                    path = (project_root / evidence.ref).resolve()
                    try:
                        path.relative_to(project_root)
                    except ValueError:
                        continue
                    if path.is_file():
                        accepted = evidence.to_dict()
                        break
                elif evidence.kind == "tool_observation":
                    observation = observations.get(evidence.ref)
                    if observation and observation.get("status") == "success":
                        accepted = evidence.to_dict()
                        break
                elif evidence.kind == "human":
                    if evidence.ref in managed.approved_gates:
                        accepted = evidence.to_dict()
                        break

            if accepted is None:
                raise ValueError(
                    f"provider PASS evidence for gate {gate_id} does not resolve to a real artifact, "
                    "successful tool observation, or approved human gate"
                )
            verified.append(accepted)

        return verified

    def execute_active_stage_with_provider(
        self,
        managed: ManagedWebsiteRun,
        provider: ProviderAdapter,
        *,
        explicit_sources: list[str] | None = None,
        dry_run: bool = False,
        max_rounds: int = 8,
    ) -> dict[str, Any]:
        if max_rounds < 1:
            raise ValueError("max_rounds must be at least 1")

        stage_id = managed.active_stage
        state = self.start_stage(managed, stage_id, explicit_sources=explicit_sources)
        last_plan: ProviderStagePlan | None = None

        for round_index in range(1, max_rounds + 1):
            request = self._provider_request(
                managed,
                state,
                round_index=round_index,
                max_rounds=max_rounds,
            )
            try:
                plan = provider.plan_stage(request)
            except ProviderError as exc:
                state.state = "FAILED"
                state.limitations.append(f"provider error: {exc}")
                self.harness.checkpoints.save(state.run_id, state.to_dict())
                decision = self.replan(
                    managed,
                    signal="TOOL_FAILURE",
                    context_updates={"provider_error": str(exc)},
                )
                return {
                    "status": "PROVIDER_ERROR",
                    "stage_state": state.to_dict(),
                    "provider_error": str(exc),
                    "replan": decision.to_dict(),
                }

            last_plan = plan
            self._record_provider_plan(managed, state, plan, round_index)

            if plan.status in {"BLOCKED", "GATE_FAIL"}:
                state.state = "BLOCKED" if plan.status == "BLOCKED" else "FAILED"
                self.harness.checkpoints.save(state.run_id, state.to_dict())
                decision = self.replan(
                    managed,
                    signal=plan.signal or ("BLOCKED" if plan.status == "BLOCKED" else "GATE_FAIL"),
                    context_updates={"provider_reason": plan.reason, "provider_summary": plan.summary},
                )
                return {
                    "status": "REPLANNED" if decision.accepted else plan.status,
                    "stage_state": state.to_dict(),
                    "plan": plan.to_dict(),
                    "replan": decision.to_dict(),
                }

            if plan.actions:
                try:
                    state = self.harness.execute_plan(state, plan.actions, dry_run=dry_run)
                except Exception as exc:
                    decision = self.replan(
                        managed,
                        signal="TOOL_FAILURE",
                        context_updates={"tool_error": f"{type(exc).__name__}: {exc}"},
                    )
                    return {
                        "status": "REPLANNED" if decision.accepted else "TOOL_FAILURE",
                        "stage_state": state.to_dict(),
                        "plan": plan.to_dict(),
                        "tool_error": f"{type(exc).__name__}: {exc}",
                        "replan": decision.to_dict(),
                    }
                if state.state == "BLOCKED":
                    managed.state = "AWAITING_AUTHORITY"
                    self._checkpoint_managed(managed)
                    return {
                        "status": "AWAITING_AUTHORITY",
                        "stage_state": state.to_dict(),
                        "plan": plan.to_dict(),
                    }

            if plan.status == "CONTINUE":
                continue

            if plan.status == "PASS":
                try:
                    verified = self._verify_gate_evidence(managed, state, plan)
                except ValueError as exc:
                    decision = self.replan(
                        managed,
                        signal="GATE_FAIL",
                        context_updates={"gate_evidence_error": str(exc)},
                    )
                    return {
                        "status": "REPLANNED" if decision.accepted else "GATE_FAIL",
                        "stage_state": state.to_dict(),
                        "plan": plan.to_dict(),
                        "gate_evidence_error": str(exc),
                        "replan": decision.to_dict(),
                    }

                managed.gate_evidence[stage_id] = verified
                self._checkpoint_managed(managed)
                try:
                    next_stage = self.complete_stage(managed, stage_id)
                except ValueError:
                    if managed.state == "AWAITING_APPROVAL":
                        return {
                            "status": "AWAITING_APPROVAL",
                            "stage_state": state.to_dict(),
                            "plan": plan.to_dict(),
                            "required_approvals": self.required_human_approvals(managed, stage_id),
                        }
                    raise
                return {
                    "status": "COMPLETED" if next_stage is None else "ADVANCED",
                    "stage_state": state.to_dict(),
                    "plan": plan.to_dict(),
                    "next_stage": next_stage,
                }

        decision = self.replan(
            managed,
            signal="TOOL_FAILURE",
            context_updates={"provider_round_budget": max_rounds},
        )
        return {
            "status": "ROUND_BUDGET_EXHAUSTED",
            "stage_state": state.to_dict(),
            "plan": last_plan.to_dict() if last_plan else None,
            "replan": decision.to_dict(),
        }

    def run_with_provider(
        self,
        managed: ManagedWebsiteRun,
        provider: ProviderAdapter,
        *,
        explicit_sources: list[str] | None = None,
        dry_run: bool = False,
        max_rounds: int = 8,
        max_cycles: int = 24,
    ) -> dict[str, Any]:
        events: list[dict[str, Any]] = []

        for _ in range(max_cycles):
            if managed.state == "COMPLETED":
                return {"status": "COMPLETED", "managed": managed.to_dict(), "events": events}

            if managed.state == "AWAITING_APPROVAL":
                pending = self.required_human_approvals(managed)
                if pending:
                    return {
                        "status": "AWAITING_APPROVAL",
                        "managed": managed.to_dict(),
                        "required_approvals": pending,
                        "events": events,
                    }
                self.complete_stage(managed)
                continue

            if managed.state == "AWAITING_AUTHORITY":
                return {"status": "AWAITING_AUTHORITY", "managed": managed.to_dict(), "events": events}

            result = self.execute_active_stage_with_provider(
                managed,
                provider,
                explicit_sources=explicit_sources,
                dry_run=dry_run,
                max_rounds=max_rounds,
            )
            events.append(result)
            status = str(result.get("status", ""))

            if status in {"ADVANCED", "REPLANNED"}:
                continue
            if status == "COMPLETED":
                return {"status": "COMPLETED", "managed": managed.to_dict(), "events": events}
            return {"status": status, "managed": managed.to_dict(), "events": events}

        managed.state = "BLOCKED"
        self._checkpoint_managed(managed)
        return {
            "status": "CYCLE_BUDGET_EXHAUSTED",
            "managed": managed.to_dict(),
            "events": events,
            "reason": f"provider execution exceeded max_cycles={max_cycles}",
        }
