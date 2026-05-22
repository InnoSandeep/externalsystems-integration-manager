# Integration Manager — Session Handoff
**v0.8.0-alpha · May 2026**

Use this document to get up to speed at the start of a new session. Read it top to bottom — it is the single source of truth for what is built, what decisions are finalized, and what to verify before making changes.

---

## 1. Current Prototype Scope Completed

**Stack:** React 18 CDN + Babel standalone, inline styles only, no build step, no persistence.  
**Fonts:** Roboto + Roboto Mono via Google Fonts CDN  
**File:** `IntegrationManager.js` · ~3,078 lines · ~65 functions (approx — grown with inbound test gate, mapping workspace, and design system v2 updates)

**What a user can do end-to-end:**
- Create and edit external systems (name, category, plant, code, error email)
- Browse systems with search, plant filter, and status filter chips
- Add an integration under a system (two-step drawer)
- Select direction (Inbound / Outbound) and method (Webhook / REST API / File — last disabled)
- Configure inbound connection details (webhook listener URL + auth, or REST API base URL + HTTP verb + params/headers/body/auth)
- Pass an inbound connection test in Step 1 before advancing to mapping (Step 2)
- Open the full-screen Mapping Workspace for field-level source → target mapping
- Run AI Auto Map and Validate simulations
- Publish an integration (gated on mapping completeness)
- Edit integrations and enable/disable them
- Inspect the DLQ (dead-letter queue) with raw payload modal
- View the Activity and Audit Log tabs

---

## 2. Main Screens Implemented

| Screen | Entry point | Status |
|---|---|---|
| Systems List | App root | ✅ Complete |
| System Detail | Click system card | ✅ Complete |
| Add System Drawer | "+ Add System" button | ✅ Complete |
| Edit System Drawer | "Edit System" button | ✅ Complete |
| Add Integration Drawer | "+ Add Integration" button | ✅ Complete |
| Edit Integration Drawer | "Edit" on IntegrationCard | ✅ Complete |
| Mapping Workspace (full-screen) | "Open Mapping Workspace →" in Step 2 | ✅ Complete |
| Webhook Registry Modal | "+ Create New Webhook" in outbound Step 1 | ✅ Complete |
| DLQ Inspect Modal | "View record detail" in DLQ tab | ✅ Complete |

---

## 3. Finalized UX / Product Decisions

These decisions are **locked**. Do not reopen them without an explicit product decision.

### System-level

- System Code is auto-generated from name + category on first save, then frozen (read-only in Edit drawer).
- Error Notification Email is required for "Save System" but optional for "Save as Draft".
- Navigating to a new system's Detail Page happens automatically after save.

### Integration-level

- Direction and Method cannot be changed after an integration is created (Edit drawer shows them read-only).
- Step 2 (Mapping & Runtime) is always shown for inbound integrations. Outbound Webhook publishes in one step (no Step 2).
- Step 2 shows a Data Mapping card with an "Open Mapping Workspace →" CTA; the Workspace opens full-screen from there.
- Product is selected at the integration level, not the system level.
- **Collections** (previously 'Business Object') is a **multi-select dropdown**. The trigger button shows the selection count; the dropdown has checkbox rows; selected items appear as chips below the field. A single integration can map to multiple collections (e.g. Observations + Work Orders from the same feed).
- **Inbound integrations** (both Webhook and REST API) require a passing connection test in Step 1 before the Next button permits advancing to Step 2. `inboundTestState` and `inboundTestResult` are stored in form state. Both reset if the endpoint selection changes. The Step 2 sample pull (`handleFetchSample`) is a separate, independent action used only for mapping — it is not the same as the Step 1 gate.

### Mapping Workspace

- Field mapping was moved out of the drawer into a **dedicated full-screen workspace**, necessary to support a side-by-side source/target panel layout.
- Step 2 shows a status card ('N of M fields mapped') with an 'Open Mapping Workspace →' CTA instead of an inline mapper.
- The Step 2 footer is context-aware: shows 'Continue →' when mapping is incomplete (opens workspace), and 'Publish Integration' once all required fields are mapped.
- The workspace toolbar uses `AIActionButton` components (purple-blue gradient, dashed border, ✦ icon) to distinguish AI-assistive actions (Auto Map, Validate) from commit actions.

### Mapping logic

- `required` on a mapping row is **frozen** — it reflects the row's original value from `SAMPLE_FIELDS` and is never overwritten when the user changes the source field (`updateSrc` destructures it out before spreading new metadata).
- Auto Map runs only on **unmapped** rows; it never overwrites a manual mapping.
- Validate counts: required unmapped + duplicate targets + real type conflicts (not cosmetic ones). `url→string` and `datetime→date` are treated as compatible.
- `mappingComplete = unmappedRequired === 0 && mappedCount > 0`. Publish is disabled until both conditions are met.

---

## 4. Prototype Architecture Notes

- **No router.** Navigation is `page` state in `App` (`"systems"` | `"detail"`).
- **No persistence.** Refresh resets everything to seed data (`INIT_SYSTEMS`, `INIT_INTEGRATIONS`, `DEMO_WEBHOOKS`).
- **All state is local React state.** No Redux, no Context API.
- **Design tokens** live in the `C` object at the top of `IntegrationManager.js`. All colors must be referenced through `C.*` — never hard-code hex values.
- **`formRef` pattern** in `MappingWorkspace`: a `useRef` set to `form` on every render so `setTimeout` callbacks (Auto Map, Validate) read fresh form state without stale closures.
- **Timer refs** (`fetchTimer`, `postTestTimer`, `inboundTestTimer`) are stored in `useRef` and cleared in `useEffect` cleanup to avoid state updates after unmount.

---

## 5. Known Placeholders Intentionally Left As-Is

| Placeholder | Location | Why left |
|---|---|---|
| "Edit Mapping" post-publish | Publish success screen | Needs workspace pre-population with saved data — design not finalized |
| Replay / Discard buttons | DLQ tab | Backend API not defined |
| "Coming Soon" — File Import / Export | Method selection in Add Integration | Intentional stub — feature not scoped |
| "Coming Soon" — Edit Mapping | Publish success screen | See above |
| Auth rotation (AFTER SAVE) | Edit System auth section | Placeholder for re-test flow — not yet designed |
| Workflows / My Approvals nav links | TopNav | Static decorative nav — no page behind them |

---

## 6. Current Compile / Runtime Status

The prototype **compiles and runs without errors** in Chromium-based browsers via the `python3 -m http.server 8000` dev server. Open `http://localhost:8000`.

Known non-errors:
- Google Fonts CDN for Roboto and Roboto Mono — requires internet access; app degrades gracefully to system fonts without it.
- GitHub Actions Node 20 deprecation annotation — non-blocking (`FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true` already applied).

Design system v2 applied (Figma-aligned C tokens, Roboto font stack). Inbound test gate added to Step 1 for all inbound methods.

---

## 7. Top 5 Things to Review First Tomorrow

1. **Inbound Webhook test gate** — Add Integration → Inbound + Webhook → select listener endpoint → click '▷ Test' → verify pass (green panel, status 200) and fail (red panel, status 405) states render correctly → confirm Next is blocked at 0.5 opacity on fail and fully enabled on pass.
2. **Inbound REST API test gate** — Add Integration → Inbound + REST API → enter endpoint URL → click '▷ Test Connection' → same pass/fail verification → confirm Next gate behaves identically to webhook case.
3. **Test state reset** — On either method, after a passing test, change the endpoint selection (or clear the URL) → confirm `inboundTestState` resets to idle, result panel disappears, and Next is blocked again.
4. **Mapping Workspace round-trip** — Add Integration → Inbound + REST API → complete Step 1 + pass test → reach Step 2 → click 'Open Mapping Workspace →' → confirm workspace opens full-screen → auto-map → validate → return to Step 2 → confirm field count card updates → Publish.
5. **Collections multi-select** — In Step 1, verify Collections dropdown shows checkboxes, allows multiple selections, shows chip summary below the field, and that single-selection still works correctly.

---

## 8. Top 5 Recommended Next Improvements

1. **Inbound test — deterministic simulation mode** — Replace the URL-validity-based pass/fail with a top-of-file constant (e.g. `SIMULATE_TEST_FAIL = false`) so demo presenters can force a specific outcome without touching runtime code.
2. **Edit Mapping post-publish** — 'Edit Mapping' on the publish success screen is currently Coming Soon. Wiring it to re-open the workspace pre-populated with saved mapping data completes the integration lifecycle loop.
3. **Connection re-test from Edit System** — Currently 'AFTER SAVE' placeholder. Embedding the animated 3-check test panel into the Edit System auth section would close the auth rotation gap.
4. **Audit log mutation** — Creates, edits, publishes, disables should append entries with timestamp + user. Currently static seed only.
5. **Outbound Webhook config fields** — Method card is selectable but target URL and signing secret fields are not built. Needs design session before it can be implemented.

---

## 9. Logic Areas That Must Not Be Broken

These are the highest-risk areas. Verify them before merging any change that touches related code.

1. **`required` field preservation** (`updateSrc` in `MappingWorkspace`): When the user changes the source dropdown on a mapping row, `required` must **never** be overwritten. The row's `required` status comes from `SAMPLE_FIELDS` and is frozen at init. Break this and a user can bypass the "required fields must be mapped" publish gate by swapping sources.

2. **Auto Map count** (`handleAutoMap`): The result message must report only the rows **newly mapped in this run**, not the total mapped count. Break this and the reported number will mislead the user about what changed.

3. **`mappingComplete` gate** (`AddIntegrationDrawer`, `MappingWorkspace` footer): `mappingComplete = unmappedRequired === 0 && mappedCount > 0`. Both conditions required. Do not change the formula.

4. **Outbound Webhook publish gate** (`AddIntegrationDrawer`): The "Publish Integration" button must stay disabled until `form.selectedWebhookId` is non-empty. This is the only gate for outbound webhook — there is no Step 2 and no mapping.

5. **Drawer reset on close** (`useEffect([open])`): When `open` becomes `false`, all form state, errors, touched, and step must reset. If this is broken, a second "Add Integration" session will inherit stale state from the previous one.

6. **`formRef` pattern** (`MappingWorkspace`): `formRef.current` must be updated on every render (`formRef.current = form`). Auto Map and Validate read from `formRef.current` inside `setTimeout` to avoid stale closures. If this is removed, they will operate on snapshot state and produce wrong results.

7. **`Collections` reset on product change**: When `form.product` changes, `form.businessObjects` must reset to `[]`. The `NESTED_TARGET_SCHEMA` is keyed by product, so stale collection selections from a previous product would produce wrong target dropdowns in the Mapping Workspace.

8. **Inbound test gate** (`AddIntegrationDrawer.handleNext`): If `direction === 'inbound'`, `handleNext()` must check `inboundTestState === 'passed'` before setting `step(2)`. Do not remove this gate or apply it to outbound flows. The gate applies to both `method === 'webhook'` and `method === 'polling'` (the inbound REST API / scheduled pull flow).

9. **`inboundTestState` reset on endpoint change**: The `onChange` handler for `webhookEndpointId` (webhook) and `endpointFullUrl` (REST API) must reset `inboundTestState` to `'idle'` and `inboundTestResult` to `null`. Do not allow a stale `'passed'` state to persist after an endpoint change.
