# Playwright rendered-evidence adapter

This adapter turns rendered routes into evidence consumable by the existing visual-quality and template-monotony graders.

It is optional because `skills_UIUX` does not impose a Node/browser dependency on every consumer.

## Install in an execution environment

```bash
npm install -D playwright
npx playwright install chromium
```

## Capture

Create a JSON config:

```json
{
  "baseUrl": "http://127.0.0.1:3000",
  "outputDir": ".uiux-evidence",
  "routes": [
    {"name": "home", "path": "/"},
    {"name": "about", "path": "/about"}
  ],
  "viewports": [
    {"name": "desktop", "width": 1440, "height": 900}
  ]
}
```

Then:

```bash
node integrations/playwright/capture.mjs capture.json
```

For each route/viewport the adapter writes:
- screenshot PNG;
- rendered HTML (`page.content()`);
- console error log;
- failed request log;
- a manifest referencing the HTML and screenshot artifacts.

Rendered screenshot existence is evidence collection, not proof that visual quality passed; the pixels still require inspection/rubric evaluation.
