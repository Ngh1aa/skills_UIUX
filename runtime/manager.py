from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from runtime.agent import ProviderNeutralAgentHarness, RunState
from runtime.flow import DevelopmentManager, ReplanDecision, ResolvedFlow


@dataclass
class ManagedWebsiteRun:
    manager_run_id: str
    flow: ResolvedFlow
    task_context: dict[str, Any]
    authority: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "manager_run_id": self.manager_run_id,
            "flow": self.flow.to_dict(),
            "task_context": self.task_context,
            "authority": self.authority,
        }


class DevelopmentManagerAgent:
    """Owns end-to-end website routing while specialist agents own execution stages.

    The manager deliberately does not absorb UI/UX knowledge. It resolves a declarative
    flow, selects stage skills, starts specialist runs and asks the replanner for bounded
    changes when explicit evidence signals a failure/risk/context change.
    """

    def __init__(self, harness: ProviderNeutralAgentHarness) -> None:
        self.harness = harness
        self.manager = DevelopmentManager(harness.repo_root, harness.policy_doc)

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
        manager_state.context["flow_plan"] = flow.to_dict()
        manager_state.context["task_context"] = dict(task_context)
        self.harness.checkpoints.save(manager_state.run_id, manager_state.to_dict())
        return ManagedWebsiteRun(
            manager_run_id=manager_state.run_id,
            flow=flow,
            task_context=dict(task_context),
            authority=authority,
        )

    def start_stage(
        self,
        managed: ManagedWebsiteRun,
        stage_id: str,
        explicit_sources: list[str] | None = None,
    ) -> RunState:
        stage = next((item for item in managed.flow.stages if item.id == stage_id), None)
        if stage is None:
            raise ValueError(f"unknown stage for flow {managed.flow.id}: {stage_id}")

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
        state.context["stage_id"] = stage.id
        state.context["stage_gates"] = list(stage.gates)
        self.harness.checkpoints.save(state.run_id, state.to_dict())
        return state

    def replan(
        self,
        managed: ManagedWebsiteRun,
        signal: str,
        current_stage: str,
        replan_count: int,
        context_updates: dict[str, Any] | None = None,
    ) -> ReplanDecision:
        context = dict(managed.task_context)
        context.update(context_updates or {})
        context["current_stage"] = current_stage
        return self.manager.replan(
            managed.flow,
            signal=signal,
            context=context,
            replan_count=replan_count,
        )
