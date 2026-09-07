#!/usr/bin/env node

/**
 * Opt-in geometry / occlusion guard for layouts where specific rendered owners
 * must not cover, collide with, or escape one another.
 *
 * Why this exists:
 * A foreground/background contrast scan can be completely green while a label
 * is physically hidden under a higher stacking-context panel. Generic browsers
 * cannot infer whether every overlap is intentional, so this runner consumes an
 * explicit project contract rather than guessing.
 *
 * Requires Playwright in the consuming project/environment:
 *   npm install --no-save playwright
 *
 * Environment:
 *   VISUAL_GEOMETRY_BASE_URL=http://127.0.0.1:4173
 *   VISUAL_GEOMETRY_CONTRACT=./scripts/visual-geometry-contract.json
 *   VISUAL_GEOMETRY_VIEWPORTS=1900x820,1363x936,1100x900
 *   VISUAL_GEOMETRY_OUT_DIR=qa-artifacts/geometry-occlusion-integrity
 *   VISUAL_GEOMETRY_INIT_SCRIPT=./scripts/qa-seed-state.js   (optional)
 *
 * Contract JSON:
 * [
 *   {
 *     "name": "home-campaign-caption",
 *     "route": "/",
 *     "subject": ".hero-caption span",
 *     "inside": ".hero-media",
 *     "avoid": [".hero-panel", ".hero-actions"],
 *     "requireVisible": true
 *   },
 *   {
 *     "name": "home-decision-panel",
 *     "route": "/",
 *     "subject": ".hero-panel",
 *     "inside": ".hero"
 *   }
 * ]
 *
 * Optional contract fields:
 *   viewports: ["1900x820", "1363x936"]  // omit to run at every viewport
 *   minCount: 1                           // default 1
 *   maxCount: 10                          // optional
 *   tolerance: 1                          // px; default 1
 *   requireVisible: true                  // default true
 *
 * `avoid` means every matched subject must not geometrically intersect any
 * visible matched avoid target. `inside` means the subject rectangle must stay
 * inside the first visible owner rectangle. This is geometry evidence, not a
 * substitute for opening and inspecting the captured screenshots.
 */

import { chromium } from "playwright";
import { mkdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";

const baseURL = process.env.VISUAL_GEOMETRY_BASE_URL || "http://127.0.0.1:4173";
const contractPath = process.env.VISUAL_GEOMETRY_CONTRACT || "";
const outputDir = path.resolve(process.env.VISUAL_GEOMETRY_OUT_DIR || "qa-artifacts/geometry-occlusion-integrity");
const initScript = process.env.VISUAL_GEOMETRY_INIT_SCRIPT || "";

if (!contractPath) {
  throw new Error("VISUAL_GEOMETRY_CONTRACT is required. Geometry overlap is intentional in many designs, so this runner will not guess owners automatically.");
}

const viewports = (process.env.VISUAL_GEOMETRY_VIEWPORTS || "1363x936,1100x900")
  .split(",")
  .map((value) => value.trim())
  .filter(Boolean)
  .map((value) => {
    const match = value.match(/^(\d+)x(\d+)$/i);
    if (!match) throw new Error(`Invalid VISUAL_GEOMETRY_VIEWPORTS entry: ${value}`);
    return {
      key: `${match[1]}x${match[2]}`,
      width: Number(match[1]),
      height: Number(match[2]),
    };
  });

const rawContract = JSON.parse(await readFile(path.resolve(contractPath), "utf8"));
if (!Array.isArray(rawContract) || rawContract.length === 0) {
  throw new Error("VISUAL_GEOMETRY_CONTRACT must be a non-empty JSON array");
}

const contracts = rawContract.map((entry, index) => {
  if (!entry || typeof entry !== "object") throw new Error(`Contract ${index} must be an object`);
  if (!entry.name || typeof entry.name !== "string") throw new Error(`Contract ${index} requires a string name`);
  if (!entry.route || typeof entry.route !== "string") throw new Error(`Contract ${entry.name} requires a string route`);
  if (!entry.subject || typeof entry.subject !== "string") throw new Error(`Contract ${entry.name} requires a string subject selector`);
  if (entry.inside != null && typeof entry.inside !== "string") throw new Error(`Contract ${entry.name} inside must be a selector string`);
  if (entry.avoid != null && (!Array.isArray(entry.avoid) || entry.avoid.some((value) => typeof value !== "string"))) {
    throw new Error(`Contract ${entry.name} avoid must be an array of selector strings`);
  }
  if (entry.viewports != null && (!Array.isArray(entry.viewports) || entry.viewports.some((value) => typeof value !== "string"))) {
    throw new Error(`Contract ${entry.name} viewports must be an array of WxH strings`);
  }
  return {
    ...entry,
    minCount: Number.isInteger(entry.minCount) ? entry.minCount : 1,
    maxCount: Number.isInteger(entry.maxCount) ? entry.maxCount : null,
    tolerance: Number.isFinite(Number(entry.tolerance)) ? Number(entry.tolerance) : 1,
    requireVisible: entry.requireVisible !== false,
    avoid: entry.avoid || [],
    viewports: entry.viewports || null,
  };
});

for (const entry of contracts) {
  if (entry.minCount < 0) throw new Error(`Contract ${entry.name} minCount must be >= 0`);
  if (entry.maxCount != null && entry.maxCount < entry.minCount) throw new Error(`Contract ${entry.name} maxCount must be >= minCount`);
  if (entry.tolerance < 0) throw new Error(`Contract ${entry.name} tolerance must be >= 0`);
}

const routes = [...new Set(contracts.map((entry) => entry.route))];
await mkdir(outputDir, { recursive: true });

const report = {
  generatedAt: new Date().toISOString(),
  baseURL,
  contractPath: path.resolve(contractPath),
  viewports,
  routes,
  note: "Explicit geometry regression only. Open and inspect rendered screenshots before PASS.",
  states: [],
  blockers: [],
};

const browser = await chromium.launch({ headless: true });
const block = (key, contract, message, detail = null) => report.blockers.push({ key, contract, message, detail });

function slug(value) {
  return value.replace(/^https?:\/\//, "").replace(/[^a-z0-9]+/gi, "-").replace(/^-|-$/g, "") || "root";
}

function visibleRectPayload(rect) {
  return {
    left: Math.round(rect.left),
    top: Math.round(rect.top),
    right: Math.round(rect.right),
    bottom: Math.round(rect.bottom),
    width: Math.round(rect.width),
    height: Math.round(rect.height),
  };
}

function intersects(a, b, tolerance = 1) {
  return (
    a.left < b.right - tolerance &&
    a.right > b.left + tolerance &&
    a.top < b.bottom - tolerance &&
    a.bottom > b.top + tolerance
  );
}

function inside(child, owner, tolerance = 1) {
  return (
    child.left >= owner.left - tolerance &&
    child.right <= owner.right + tolerance &&
    child.top >= owner.top - tolerance &&
    child.bottom <= owner.bottom + tolerance
  );
}

async function freezeMotion(page) {
  await page.addStyleTag({ content: `
    *,*::before,*::after{
      animation-duration:.001ms!important;
      animation-delay:0ms!important;
      transition-duration:.001ms!important;
      transition-delay:0ms!important;
      scroll-behavior:auto!important;
    }
  ` });
}

async function geometry(locator) {
  return locator.evaluate((el) => {
    const style = getComputedStyle(el);
    const rect = el.getBoundingClientRect();
    return {
      rect: rect.toJSON(),
      visible: rect.width > 0 && rect.height > 0 && style.display !== "none" && style.visibility !== "hidden" && Number.parseFloat(style.opacity || "1") > 0.05,
      position: style.position,
      zIndex: style.zIndex,
      overflow: style.overflow,
      text: (el.innerText || el.textContent || "").replace(/\s+/g, " ").trim().slice(0, 120),
      className: typeof el.className === "string" ? el.className : "",
    };
  });
}

for (const viewport of viewports) {
  for (const route of routes) {
    const applicable = contracts.filter((entry) => (
      entry.route === route && (!entry.viewports || entry.viewports.includes(viewport.key))
    ));
    if (!applicable.length) continue;

    const context = await browser.newContext({
      viewport: { width: viewport.width, height: viewport.height },
      deviceScaleFactor: 1,
      colorScheme: "light",
      reducedMotion: "reduce",
    });
    if (initScript) await context.addInitScript({ path: path.resolve(initScript) });
    const page = await context.newPage();
    const url = new URL(route, baseURL).toString();
    const response = await page.goto(url, { waitUntil: "networkidle", timeout: 30_000 });
    await page.evaluate(async () => { if (document.fonts?.ready) await document.fonts.ready; });
    await freezeMotion(page);
    await page.waitForTimeout(60);

    const key = `${route}@${viewport.key}`;
    const state = { key, route, viewport, httpStatus: response?.status() || null, contracts: [] };
    if (!response?.ok()) block(key, "route", `HTTP ${response?.status() ?? "no response"}`);

    for (const contract of applicable) {
      const subjectNodes = page.locator(contract.subject);
      const subjectCount = await subjectNodes.count();
      const contractState = {
        name: contract.name,
        subject: contract.subject,
        inside: contract.inside || null,
        avoid: contract.avoid,
        subjectCount,
        subjects: [],
      };

      if (subjectCount < contract.minCount) {
        block(key, contract.name, `subject count ${subjectCount} below minCount ${contract.minCount}`, { selector: contract.subject });
      }
      if (contract.maxCount != null && subjectCount > contract.maxCount) {
        block(key, contract.name, `subject count ${subjectCount} above maxCount ${contract.maxCount}`, { selector: contract.subject });
      }

      let owner = null;
      if (contract.inside) {
        const ownerNodes = page.locator(contract.inside);
        if (await ownerNodes.count() === 0) {
          block(key, contract.name, "inside owner selector did not resolve", { selector: contract.inside });
        } else {
          const ownerGeometry = await geometry(ownerNodes.first());
          if (!ownerGeometry.visible) {
            block(key, contract.name, "inside owner is not visibly rendered", { selector: contract.inside, owner: ownerGeometry });
          } else {
            owner = { ...ownerGeometry, rect: visibleRectPayload(ownerGeometry.rect) };
            contractState.owner = owner;
          }
        }
      }

      const avoidTargets = [];
      for (const selector of contract.avoid) {
        const nodes = page.locator(selector);
        for (let index = 0; index < await nodes.count(); index += 1) {
          const item = await geometry(nodes.nth(index));
          if (!item.visible) continue;
          avoidTargets.push({ selector, index, ...item, rect: visibleRectPayload(item.rect) });
        }
      }
      contractState.avoidTargets = avoidTargets;

      for (let index = 0; index < subjectCount; index += 1) {
        const item = await geometry(subjectNodes.nth(index));
        const subject = { index, ...item, rect: visibleRectPayload(item.rect) };
        contractState.subjects.push(subject);

        if (contract.requireVisible && !item.visible) {
          block(key, contract.name, "subject is not visibly rendered", { index, selector: contract.subject, subject });
          continue;
        }
        if (!item.visible) continue;

        if (owner && !inside(subject.rect, owner.rect, contract.tolerance)) {
          block(key, contract.name, "subject escapes declared owner", { index, subject: subject.rect, owner: owner.rect, tolerance: contract.tolerance });
        }

        for (const target of avoidTargets) {
          if (intersects(subject.rect, target.rect, contract.tolerance)) {
            block(key, contract.name, "subject intersects forbidden rendered owner", {
              index,
              subject: subject.rect,
              avoid: { selector: target.selector, index: target.index, rect: target.rect },
              tolerance: contract.tolerance,
            });
          }
        }
      }

      state.contracts.push(contractState);
    }

    await page.evaluate(() => scrollTo(0, 0));
    await page.screenshot({
      path: path.join(outputDir, `${slug(route)}-${viewport.key}.png`),
      fullPage: false,
    });
    report.states.push(state);
    await context.close();
  }
}

await browser.close();
await writeFile(path.join(outputDir, "report.json"), JSON.stringify(report, null, 2));

console.log(`Geometry occlusion integrity: ${report.states.length} route/viewport states.`);
console.log(`Blockers: ${report.blockers.length}`);
for (const blocker of report.blockers) console.log(JSON.stringify(blocker));
if (report.blockers.length) process.exit(1);
