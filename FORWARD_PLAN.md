# Integration Manager — Forward Plan
**v0.8.0-alpha · May 2026**

---

## 1. Immediate Next Polish Items

~~**Inbound connection test gate**~~ ✅ SHIPPED — Inline test button and result panel added to Step 1 for both Inbound Webhook and Inbound REST API. Next button is gated on `inboundTestState === 'passed'`. State resets on endpoint change.

2. **Wire 'Edit Mapping' post-publish** — The publish success screen has a disabled "Edit Mapping" chip. Wire it to re-open `MappingWorkspace` pre-populated with the saved `fieldMappings` from the published integration. Requires passing the integration object back into the workspace and writing changes back on close.

3. **Audit log mutation** — `AUDIT_LOG` is a static seed constant. Creates, edits, publishes, and disable actions should append entries with timestamp and user identity. Implement as a `setAuditLog` state setter passed down to all mutation handlers.

4. **Deterministic inbound test simulation** — Add a top-of-file constant `SIMULATE_INBOUND_TEST_FAIL = false`. `handleInboundTest` reads it to override the `isValidUrl` result so demo presenters can force pass or fail without editing the URL.

5. **`NESTED_TARGET_SCHEMA` — fill missing collections** — Many collections in `PRODUCT_OBJECTS` have no schema entry (iMaintenance: Operation, Component, Equipment, Functional Location, Attachment, Failure Reporting; mRounds: Round Plan, Asset, Location, Assignment; mInventory: Plant, Storage Location, Storage Bin, Stock, Reservation, Transfer Posting, Cycle Count, Label; EHS: Audit, JHA; Platform: Audit). Users selecting these get an empty target dropdown in the Mapping Workspace.

6. **Auth rotation flow (Edit System)** — The auth section in Edit System Drawer shows "AFTER SAVE" placeholder text. Design and implement an inline re-test panel (3-check animated flow: DNS → TCP → Auth) to close the auth rotation loop.

---

## 2. PRD Automation Readiness Assessment

Assessment of how ready the prototype is to demonstrate key Integration Manager PRD scenarios.

| PRD scenario | Status | Notes |
|---|---|---|
| Create and manage external systems | ✅ Ready | Full CRUD, draft save, status badges |
| Configure inbound polling integration | ✅ Ready | Base URL, HTTP verb, params, headers, body, auth, test gate, mapping, publish |
| Configure inbound webhook integration | ✅ Ready | Listener URL, incoming auth, test gate, mapping, publish |
| Configure outbound webhook integration | ✅ Ready | Webhook registry selection or creation, single-step publish |
| Field-level source → target mapping | ✅ Ready | Full workspace with Auto Map, Validate, filter, required gate |
| Collections multi-select | ✅ Ready | Checkbox dropdown, chip summary, per-product schema |
| Edge cases identified | ⚠️ Partial | Push-only done; inbound test gate done; outbound webhook config and auth rotation still need spec |
| DLQ inspection | ✅ Ready | Record list, inspect modal, raw payload copy |
| Audit log | ⚠️ Static only | Static seed data; mutation not wired |
| Edit integration | ✅ Ready | Name, product, collections, frequency, trigger, failure handling |

---

## 3. Architecture Constraints (Prototype vs. Production)

| Constraint | Prototype | Production implication |
|---|---|---|
| State | Local `useState`, no persistence | Replace with API calls + global state (Redux, Zustand, or React Query) |
| Data | Static seed constants | Backend API for CRUD on systems, integrations, webhooks |
| Mapping | Simulated Auto Map + Validate | Wire to real schema inference and validation service |
| Auth | Mock form fields only | Real OAuth flows, token rotation, secret storage |
| DLQ | Static entries | Real-time queue consumer with replay/discard actions |
| Font | CDN (requires internet) | Bundle or serve Roboto locally |
| File count | 1 JS file | Split into feature modules, introduce build step |

---

## 4. Design Debt

| Item | Impact | Effort |
|---|---|---|
| `AddIntegrationDrawer` is 1,500+ lines | Hard to navigate, high merge conflict risk | High — needs component extraction |
| Inline styles throughout | No theming, no responsive breakpoints | Medium — migrate to CSS modules or styled-components when build step is added |
| `NESTED_TARGET_SCHEMA` is hand-coded | Incomplete, will drift from actual schema | Low prototype effort; production replaces with API |
| `AUTO_MAP_RULES` is a flat object | Brittle; real mapping needs semantic similarity | Replace with ML similarity in production |
| Seed data in constants | Realistic enough for demo; breaks at scale | Replace with API calls |

---

## 5. Suggested Story Breakdown

For handoff to an engineering team for productionization. Organized by epic.

### E1 — System Management

| Story ID | Title |
|---|---|
| E1-S1 | List systems with search, filter by plant, filter by status |
| E1-S2 | Create system (name, category, plant, code, error email) |
| E1-S3 | Edit system (all fields except code) |
| E1-S4 | Auto-generate System Code; freeze on first save |
| E1-S5 | System Detail: integrations tab, activity tab, DLQ tab, audit tab |
| E1-S6 | System status badges (ready, draft, needs_attention) |

### E2 — Integration Configuration

| Story ID | Title |
|---|---|
| E2-S1 | Two-step Add Integration drawer (inbound) |
| E2-S2 | Direction selection: Inbound / Outbound |
| E2-S3 | Method selection: Webhook / REST API (polling) |
| E2-S4 | Inbound Webhook: listener URL + incoming auth config |
| E2-S5 | Inbound REST API: base URL, HTTP verb, params, headers, body, auth |
| E2-S6 | Choose product, collections (multi-select), workflow action, trigger, failure behavior |
| E2-S7 | Outbound Webhook: single-step, webhook registry selection or creation |
| E2-S8 | Save as Draft (skips mapping gate) |
| E2-S9 | Publish Integration (gated on mapping completeness) |
| E2-S10 | Edit integration (name, product, collections, frequency, trigger, failure handling) |
| E2-S11 | Enable / Disable integration |
| E2-S12 | Run inbound connection test in Step 1 before proceeding to Step 2 (applies to Webhook and REST API inbound; outbound unaffected) |

### E3 — Field Mapping

| Story ID | Title |
|---|---|
| E3-S1 | Full-screen Mapping Workspace |
| E3-S2 | Source schema panel — payload field tree with type/required badges |
| E3-S3 | Mapping table — source dropdown, target dropdown, row state |
| E3-S4 | Target dropdown — per-collection schema from `NESTED_TARGET_SCHEMA` |
| E3-S5 | Auto Map — rule-based AI simulation, unmapped rows only |
| E3-S6 | Validate — required, duplicates, type conflicts, ref lookups |
| E3-S7 | Filter rows by field name |
| E3-S8 | Sample pull simulation |
| E3-S9 | Freeze `required` field on source changes |
| E3-S10 | Publish gate: `unmappedRequired === 0 && mappedCount > 0` |

### E4 — Observability

| Story ID | Title |
|---|---|
| E4-S1 | DLQ tab — list failed records |
| E4-S2 | DLQ Inspect Modal — plain-English summary + raw payload + copy |
| E4-S3 | Replay and Discard actions |
| E4-S4 | Activity tab — semantic table with status, message, timestamp |
| E4-S5 | Audit log — semantic table with timestamp, user, action |
| E4-S6 | Audit log mutation — append on create/edit/publish/disable |

---

## 6. Out of Scope (This Prototype)

- Multi-tenancy / RBAC
- Real authentication (OAuth, SAML)
- Backend API or database
- Notifications / email sending
- Scheduled job execution
- Mobile / responsive layout
- Accessibility audit
- Performance testing
- File Import / File Export methods
