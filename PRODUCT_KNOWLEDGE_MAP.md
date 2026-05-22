# Integration Manager — Product Knowledge Map
**v0.8.0-alpha · May 2026**

A reference for anyone working on this prototype. Covers the data model, screen-to-component map, UX rules, finalized decisions, deferred features, and critical constraints.

---

## 1. Core Entities

### System

Represents an external data source or destination (e.g. AVEVA PI, Augury, SAP).

Fields: `id`, `name`, `category`, `plant`, `code` (auto-generated, frozen after first save), `description`, `errorEmail`, `status` (`ready` | `draft` | `needs_attention`), `errorCount`, `errorBadge`

### Integration

Represents a configured data flow between an external system and an Innovapptive product.

Fields: `id`, `systemId`, `name`, `direction` (`inbound` | `outbound`), `method` (`"webhook"` | `"polling"` | `"file_import"` | `"file_export"` — the inbound REST API / scheduled pull flow uses `"polling"` as the method constant), `status`, `product`, `businessObjects` (array — the persisted key; UI labels it "Collections". Was single-select "Business Object", now multi-select), `triggerOn`, `failureBehavior`, `frequency`, `startTime`, `fieldMappings`, `inboundTestState` (`idle`|`loading`|`passed`|`failed` — transient, form-only, not persisted to the saved integration record), `inboundTestResult` (null or `{ statusCode, responseTimeMs, responseBody }` — transient, form-only)

Note: `inboundTestState` and `inboundTestResult` exist only during form editing. They are never written to the saved integration object.

### Webhook

A registered outbound endpoint. Fields: `id`, `name`, `targetUrl`, `signingSecret`, `eventTypes`

### Mapping Row

Part of `integration.fieldMappings`. Each row: `src` (source path), `srcType`, `required` (frozen at init), `refLookup`, `nested`, `arrayPath`, `target` (selected by user), `rowState` (`unmapped` | `manual` | `auto-mapped`)

---

## 2. Screen → Component Map

| Screen | Component | Notes |
|---|---|---|
| Systems list | `SystemsPage` + `SystemCard` | Search + filter chips + plant select |
| System detail | `SystemDetailPage` | Tabs: integrations, activity, dlq, audit |
| Add system | `AddSystemDrawer` | 500px right drawer |
| Edit system | `EditSystemDrawer` | 500px right drawer |
| Add integration | `AddIntegrationDrawer` | 580px right drawer, 2-step for inbound |
| Edit integration | `EditIntegrationDrawer` | 520px right drawer |
| Mapping workspace | `MappingWorkspace` | Full-screen fixed overlay, z-index 211 |
| Webhook registry modal | `WebhookRegistryModal` | Centered 520px modal |
| DLQ inspect | `DLQInspectModal` | Centered 620px modal, 82vh |

---

## 3. State Architecture

All state is local React `useState`. No global store, no Context API, no persistence (refresh resets to seed data).

**Form pattern (every drawer):**
1. `form` object — initialized from blank factory (`blankIntegrationForm()`, `blankAddSystemForm()`)
2. `set(key, value)` shorthand — `setForm(f => ({...f, [k]: v}))`
3. `errors` + `touched` objects — keyed by field name
4. `validate()` — returns `{ fieldName: "message" }` or `{}`
5. `useEffect([open])` — resets all state when drawer closes

**Timer refs:** `fetchTimer`, `postTestTimer`, `inboundTestTimer` — stored in `useRef`, cleared in `useEffect` cleanup.

**`formRef` pattern (`MappingWorkspace`):** `useRef` set to `form` on every render so `setTimeout` callbacks (Auto Map, Validate) read fresh state without stale closures.

---

## 4. Key UX Rules

1. **Draft saves skip email validation.** The "Save as Draft" action never validates the Error Notification Email field. Full save requires it.
2. **Direction + Method are immutable after creation.** The Edit Integration drawer shows them read-only. Do not add edit capability without a product decision.
3. **Outbound Webhook has no Step 2.** It publishes in one step once a webhook is selected. No mapping required.
4. **Publish is gated on mapping completeness.** `mappingComplete = unmappedRequired === 0 && mappedCount > 0`. The button is disabled (not just visually) when this is false.
5. **`required` field on mapping rows is frozen.** Source field changes update `src`, `srcType`, etc. but never `required`. This protects the publish gate.
6. **Changing product resets collections.** `NESTED_TARGET_SCHEMA` is keyed by product; stale collection selections produce wrong target dropdowns.
7. **Auto Map only fills unmapped rows.** It never overwrites `manual` or `auto-mapped` rows from a previous run.
8. **Monospace font (Roboto Mono) for codes, URLs, IDs, JSON.** All other UI text uses Roboto.
9. **All colors through `C.*` tokens.** Never hard-code hex values in inline styles. `C` is defined at the top of `IntegrationManager.js`.
10. **Disabled method cards convey state via subtitle.** No overlay badges — "Coming soon" is set as the `description` prop of `SelectionCard`.
11. **Inbound test before Step 2** — For all inbound integrations (both Webhook and REST API), a connection test must pass in Step 1 before the user can advance to Step 2. `inboundTestState` must equal `'passed'`. This gate does not apply to outbound integrations. The test state resets if the endpoint or listener endpoint changes.

---

## 5. Finalized Decisions

| Decision | What was decided | Rationale |
|---|---|---|
| System Code | Auto-generated on first save, frozen (read-only) in edit | Prevents accidental code changes that break external references |
| Mapping in Workspace, not drawer | Full-screen `MappingWorkspace` replaces inline mapper | Drawer is too narrow for side-by-side source/target layout |
| `required` freezing in `updateSrc` | Destructure `required` out before spreading new field metadata | Prevents source-swap publish gate bypass — security fix |
| Auto Map count | Reports rows newly mapped this run, not total mapped | Accurate feedback; prevents false impression of more work done |
| Outbound Webhook — single step | No Step 2, no mapping, publish when webhook selected | Outbound does not require field mapping in this product model |
| `formRef` for async callbacks | Set `formRef.current = form` on every render | Avoids stale closures in `setTimeout` without side effects inside updaters |
| Collections field | Multi-select (array) replacing single Business Object | A single integration can map to multiple object types from one feed |
| Inbound test gate | Required in Step 1 for all inbound methods | Prevents proceeding to mapping without a verified connection; resets on endpoint change |
| Mapping Workspace | Full-screen surface, not inline in drawer | Drawer is too narrow for side-by-side source/target layout; workspace opens from Step 2 CTA |

---

## 6. Data Flow — Inbound Polling (full path)

```
Add Integration Drawer (Step 1)
  → Name, Inbound + REST API, Product + Collections
  → Base URL, HTTP Method, Params, Headers, Body, Auth
  → ▷ Test Connection (handleInboundTest)
      → inboundTestState: loading → passed/failed
      → inboundTestResult: { statusCode, responseTimeMs, responseBody }
  → Next: Mapping & Runtime (gated on inboundTestState === 'passed')

Add Integration Drawer (Step 2)
  → Request Context summary
  → Data Mapping card (shows N of M fields mapped)
  → Open Mapping Workspace →

MappingWorkspace (full-screen)
  → Pull Sample (optional)
  → Auto Map (AI simulation)
  → Validate
  → Manual row edits
  → Back (returns to Step 2)

Add Integration Drawer (Step 2 — continued)
  → Runtime: Frequency + Start Time
  → Readiness Checklist
  → Publish Integration (gated on mappingComplete)
  → Publish success screen
```

---

## 7. Deferred Features

| Feature | Why deferred | Priority |
|---|---|---|
| Edit Mapping post-publish | Needs workspace pre-population with saved data — design not finalized | Medium |
| Replay / Discard in DLQ | Backend API not defined | Low |
| File Import / File Export | Rendered as "Coming soon" — not scoped | Low |
| Auth rotation (AFTER SAVE) | Re-test flow not yet designed | Medium |
| Outbound Webhook config fields | Method card selectable but target URL + signing secret not built | Medium |
| Audit log mutation | Creates/edits/publishes should append entries; currently static | Low |
| Multi-collection target grouping | Target dropdowns correct per-collection; deduplication across collections not implemented | Low |
| Inbound test — deterministic simulation | URL-validity-based outcome makes demos unpredictable | Low — add a top-of-file flag |

---

## 8. Placeholders (Complete Inventory)

| Placeholder text | Component | Behavior |
|---|---|---|
| "Coming soon" subtitle | `SelectionCard` (File Import, File Export) | Card disabled, cursor not-allowed, 55% opacity |
| "AFTER SAVE" | Edit System auth section | Static text, no action |
| "Edit Mapping" (Coming Soon chip) | Publish success screen | `pointer-events: none` |
| Replay button | DLQ tab + DLQ Inspect Modal | Renders but no handler |
| Discard button | DLQ tab + DLQ Inspect Modal | Renders but no handler |
| Workflows nav link | TopNav | Renders but no navigation |
| My Approvals nav link | TopNav | Renders but no navigation |

---

## 9. Critical Business Logic Constraints

1. **`required` field on mapping rows must never be overwritten** by `updateSrc`. Destructure it out and ignore it when applying new source field metadata. Break this → user can bypass the publish gate by swapping sources.

2. **Auto Map count must be per-run, not cumulative.** `handleAutoMap` counts only rows mapped in the current invocation. Reporting total mapped would mislead the user about what changed.

3. **`mappingComplete` formula must not be simplified.** `unmappedRequired === 0 && mappedCount > 0` — both conditions are required. Removing `mappedCount > 0` would allow publishing an integration with zero field mappings.

4. **Outbound Webhook publish gate must stay.** "Publish Integration" button must remain disabled until `form.selectedWebhookId` is non-empty. No Step 2, no mapping gate — this is the only gate.

5. **Drawer must reset on `open → false`.** Form, errors, touched, step, and all timer refs must clear when the drawer closes. Stale state from a previous session must never carry over.

6. **`formRef.current` must be assigned on every render.** Auto Map and Validate callbacks read from it inside `setTimeout`. If removed or memoized, they will operate on stale state.

7. **Collections must reset when product changes.** `form.businessObjects = []` in the product `onChange` handler. Stale collection selections produce wrong target dropdowns in `NESTED_TARGET_SCHEMA`.

8. **Inbound integrations are gated on a passing Step 1 test.** `handleNext()` in `AddIntegrationDrawer` validates `inboundTestState === 'passed'` when `direction === 'inbound'`, regardless of method. The gate does not apply to outbound. `inboundTestState` and `inboundTestResult` are transient form fields — they are never written to the saved integration record.

---

## 10. Important Terms / Definitions

| Term | Definition |
|---|---|
| **System** | An external data source or destination registered in Integration Manager. Has a category (Historian, Analytics Platform, etc.) and a unique auto-generated System Code. |
| **Integration** | A configured data flow under a System. Has a direction (Inbound/Outbound), a method (`"webhook"` or `"polling"` — the latter covers the inbound REST API scheduled-pull flow), and — for inbound — a field mapping to an Innovapptive collection. |
| **Collections** | The UI label for `businessObjects` — a multi-select list of Innovapptive business object types (e.g. Observations, Work Orders) that a single integration maps to. Persisted as `businessObjects` in the integration record. Replaces the former single-select 'Business Object' field. |
| **Mapping Workspace** | A full-screen surface opened from Step 2 of Add Integration. Provides a side-by-side source schema panel and mapping row editor. Replaces the former inline mapper inside the drawer. |
| **Inbound test gate** | A simulated connection test required in Step 1 for all inbound integrations. Must pass (status 200 simulated) before the user can advance to Step 2. Applies to both `method === 'webhook'` and `method === 'polling'` (the inbound REST API / scheduled pull flow). |
| **`inboundTestState`** | Form-only field: `idle` \| `loading` \| `passed` \| `failed`. Tracks the live connection test status. Never persisted to the saved integration record. |
| **Auto Map** | AI-simulated mapping action in the Workspace. Applies `AUTO_MAP_RULES` to unmapped rows, checks the result exists in `NESTED_TARGET_SCHEMA`, and sets `rowState: "auto-mapped"`. Only fills unmapped rows. |
| **Validate** | AI-simulated validation action in the Workspace. Checks required fields mapped, duplicate targets, real type conflicts, and ref lookups. Stores result in `form.validationResult`. |
| **DLQ** | Dead-letter queue. Records that failed to process after all retries. Inspectable via `DLQInspectModal`. Replay and Discard are stubbed. |
| **`mappingComplete`** | `unmappedRequired === 0 && mappedCount > 0`. The Publish button is disabled until this is true. |
| **Seed data** | `INIT_SYSTEMS`, `INIT_INTEGRATIONS`, `DEMO_WEBHOOKS` — constants at the top of `IntegrationManager.js`. Loaded as initial state on every page refresh. |
