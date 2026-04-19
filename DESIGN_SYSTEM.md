# Integration Manager — Design System
**Version:** 1.1 · April 2026  
**Based on:** Figma export · Color Guide · Typography Guidelines · Core Styles · Stepper · Icon Library  
**Applies to:** IntegrationManager.jsx and all future screens

---

## 1. Font System

### Primary Typeface
```
font-family: 'Roboto', 'Segoe UI', system-ui, sans-serif
```
**Replaces:** `IBM Plex Sans` (current codebase)  
Source: Figma Typography Guidelines — Font Family: **ROBOTO**

### Monospace Typeface
```
font-family: 'Roboto Mono', 'Fira Code', 'Consolas', monospace
```
Used for: System Codes, endpoint URLs, listener IDs, DLQ IDs, JSON payloads, email addresses in tables.

### Type Scale (Figma Tokens — Integration Manager usage)

| Token | Size | Line Height | Letter Spacing | Weight | Usage in product |
|---|---|---|---|---|---|
| `title/bold/t1` | 28px | 130% | -1% | 700 | Page titles (rare) |
| `title/bold/t2` | 24px | 133% | -0.8% | 700 | Section headings |
| `title/bold/t3` | 18px | 123% | -0.5% | 700 | Drawer titles, card group headers |
| `title/bold/t4` | 16px | 138% | -0.3% | 700 | Card section headers |
| `title/bold/t5` | 14px | 143% | 0% | 700 | Sub-section labels, column headers |
| `title/bold/t6` | 12px | 133% | 0% | 700 | Chip labels, status badge labels |
| `title/bold/t7` | 10px | 140% | 1% | 700 | COMING SOON micro-label, meta labels |
| `title/medium/t4` | 16px | 138% | -0.3% | 500 | Nav items |
| `title/medium/t5` | 14px | 143% | 0% | 500 | Form labels, table header |
| `title/medium/t6` | 12px | 133% | 0% | 500 | Secondary labels, badges |
| `body/regular/b1` | 18px | 156% | 0% | 400 | Long-form help text |
| `body/regular/b2` | 16px | 150% | 0% | 400 | Body paragraph, drawer description |
| `body/regular/b3` | 14px | 143% | 0% | 400 | Default UI text, table cells |
| `body/regular/b4` | 12px | 150% | 0% | 400 | Secondary metadata, timestamps |
| `body/regular/b5` | 10px | 140% | 2% | 400 | Caption, very small helper text |

### Typography Quick Reference (Component — Token)

| Component context | Font size | Weight |
|---|---|---|
| Drawer/modal title | 18px | 700 |
| Page section heading | 16px | 700 |
| Card title | 14px | 700 |
| Form field label | 12px | 500 |
| Input text / table cell | 14px | 400 |
| Table column header | 12px | 700 |
| Status badge | 12px | 500 |
| Helper / description text | 12px | 400 |
| Timestamp / metadata | 12px | 400 |
| COMING SOON chip | 9px | 700 uppercase |
| Monospace (codes, URLs) | 12px | 400 |
| Button text | 14px | 500 |

---

## 2. Color System

### Brand Primary — alpha/primary

Mapped from Figma `alpha/primary` palette. The interactive/action color for buttons, links, active steps, focus rings, and primary indicators.

| Token | Hex | Usage |
|---|---|---|
| `alpha/primary-50` | `#EEF0FB` | Hover backgrounds, selected row tint |
| `alpha/primary-100` | `#D5D9F5` | Focus ring fill, light chip background |
| `alpha/primary-300` | `#8A94E0` | Stepper inactive indicator |
| `alpha/primary-500` | `#3D4FD6` | **Primary interactive** — buttons, active nav, stepper active, links |
| `alpha/primary-700` | `#2A3EB1` | Button hover, active state dark |
| `alpha/primary-900` | `#1A2875` | Dark accents, pressed state |

> Note: Replaces current `C.blue = #1D6FE8`. The Figma primary leans slightly purple-blue (not pure blue). Adopt `#3D4FD6` as the canonical primary.

### Cool Greys — Neutral Surface & Text

Mapped from Figma `Cool Greys` palette.

| Token | Hex | Usage |
|---|---|---|
| White | `#FFFFFF` | Card surface, input background, modal background |
| `grey-100` | `#F5F5F5` | Page background, zebra row, disabled input fill |
| `grey-50` | `#FAFAFA` | **bg1** — hover rows, sidebar tint, info blocks *(see note below)* |
| `grey-200` | `#EEEEEE` | Dividers, secondary borders |
| `grey-300` | `#E0E0E0` | Default border on inputs, table borders |
| `grey-400` | `#BDBDBD` | Placeholder text, icon at rest |
| `grey-500` | `#9E9E9E` | Secondary text, meta labels |
| `grey-600` | `#757575` | Body text secondary |
| `grey-700` | `#616161` | Body text primary (dense content) |
| `text-primary` | `#212121` | High-emphasis text (headings, labels) |
| `text-secondary` | `#3D3D3D` | Medium-emphasis text |

> **bg1 implementation note:** The Figma spec lists `bg1 = grey-100 = #F5F5F5`, which equals `pageBg`. In practice this collapses surface layering — hover states on system cards, info blocks, and disabled integration rows become invisible against the page background. `bg1` is set to `#FAFAFA` (grey-50) to preserve a subtle one-step elevation between the page and the surfaces that sit on it. All other grey tokens remain exactly as specified.

### Semantic / Status Colors

Drawn from Figma gamma accent palettes, mapped to product status model.

#### Success / Active — gamma/accent/green
| Token | Hex | Usage |
|---|---|---|
| `green-500` | `#2E7D32` | Active status text, success icon |
| `green-50` | `#E8F5E9` | Active/success badge background |
| `green-200` | `#A5D6A7` | Active/success badge border |

#### Warning / Draft / Attention — gamma/accent/orange (amber)
| Token | Hex | Usage |
|---|---|---|
| `orange-700` | `#C47D0A` | Warning text, draft status |
| `orange-50` | `#FFF8E1` | Warning badge background |
| `orange-200` | `#FFE082` | Warning badge border |

#### Error / Failed — gamma/accent/red
| Token | Hex | Usage |
|---|---|---|
| `red-700` | `#C62828` | Error text, failed status, destructive action |
| `red-50` | `#FFEBEE` | Error badge background, error input border fill |
| `red-200` | `#EF9A9A` | Error badge border |

#### Info / Inbound — gamma/accent/cyan (Teal)
| Token | Hex | Usage |
|---|---|---|
| `teal-700` | `#00796B` | Inbound integration left-rail, info callout text |
| `teal-50` | `#E0F2F1` | Inbound badge background, info callout background |
| `teal-200` | `#80CBC4` | Inbound badge border |

#### Outbound / Feature — gamma/accent/purple
| Token | Hex | Usage |
|---|---|---|
| `purple-700` | `#6A1B9A` | Outbound integration left-rail, outbound badge text |
| `purple-50` | `#F3E5F5` | Outbound badge background |
| `purple-200` | `#CE93D8` | Outbound badge border |

#### Ready to Publish — alpha/primary (reuse)
Uses `alpha/primary-500` text on `alpha/primary-50` background with `alpha/primary-100` border.

### Navigation Surface

Retain current dark nav. Update token names:

| Token | Hex | Usage |
|---|---|---|
| `nav-bg` | `#1A2233` | Left/top nav background |
| `nav-border` | `#2A3447` | Nav internal borders |
| `nav-text` | `#C8D0DC` | Nav item text (inactive) |
| `nav-active` | `#FFFFFF` | Nav item text (active) |
| `nav-active-bg` | `#2A3EB1` | Nav item active background pill |

---

## 3. Spacing System

Figma `space-*` tokens — 4px base grid.

| Token | Value | Typical use |
|---|---|---|
| `space-0` | 0px | Flush elements |
| `space-4` | 4px | Chip internal padding, badge padding, icon gap |
| `space-8` | 8px | Button internal padding (vertical), list item gap, input padding |
| `space-12` | 12px | Card internal padding (compact), form field gap |
| `space-16` | 16px | Card internal padding (standard), section gap |
| `space-20` | 20px | Drawer section gap |
| `space-24` | 24px | Drawer padding, modal padding |
| `space-32` | 32px | Between major sections |
| `space-40` | 40px | Page-level vertical rhythm |
| `space-48` | 48px | Large gaps, hero sections |
| `space-64` | 64px | Full-bleed spacers |

> Most common in Integration Manager: `8px` and `16px` for internal component spacing; `24px` for drawer/card padding.

---

## 4. Border Radius

| Token | Value | Use |
|---|---|---|
| `radius-0` | 0px | Table rows, dividers |
| `radius-4` | 4px | Badges, chips, small tags |
| `radius-8` | 8px | **Default** — cards, inputs, buttons, drawers |
| `radius-12` | 12px | Modals, large panels |
| `radius-16` | 16px | Floating panels, tooltips |
| `radius-full` | 9999px | Status dots, avatars, toggle pill |

---

## 5. Stroke / Border

| Token | Value | Use |
|---|---|---|
| `border-1` | 1px | Default component borders (inputs, cards) |
| `border-2` | 1.5px | Focus rings (inside), emphasis borders |
| `border-3` | 2px | Active/selected component outline |
| `border-4` | 4px | Left-rail accent on integration cards |

---

## 6. Elevation / Shadow

| Token | CSS value | Use |
|---|---|---|
| `effect-0` | none | Flat surface — page background, table rows |
| `effect-1` | `0 1px 4px rgba(0,0,0,0.13)` | Cards, dropdowns, select menus |
| `effect-2` | `0 2px 6px rgba(0,0,0,0.18)` | Modals, drawers, dialogs |
| `effect-3` | `0 4px 8px rgba(0,0,0,0.22)` | Overlays, floating panels (top-most layer) |

---

## 7. Opacity Tokens

| Token | Value | Use |
|---|---|---|
| `opacity-100` | 100% | All active, enabled elements |
| `opacity-60` | 60% | Disabled interactive elements |
| `opacity-50` | 50% | Placeholder overlays |
| `opacity-30` | 30% | Hover tint layers |
| `opacity-20` | 20% | Overlay backgrounds |
| `opacity-10` | 10% | Subtle hover fills |

---

## 8. Component Token Map (IntegrationManager.jsx `C` constant)

Direct replacement for the current `C` object. Apply as-is.

```js
// ─── THEME (v2 — Figma-aligned) ───────────────────────────────────────────────
const C = {
  // Surfaces
  pageBg:      "#F5F5F5",   // grey-100
  bg0:         "#FFFFFF",   // White — cards, modals, inputs
  bg1:         "#FAFAFA",   // grey-50 — hover rows, sidebars, info blocks
                            // NOTE: spec says #F5F5F5 but that equals pageBg;
                            // #FAFAFA preserves surface layering and hover visibility
  bg2:         "#EEEEEE",   // grey-200 — disabled fill, divider bg
  bg3:         "#E0E0E0",   // grey-300 — stronger divider

  // Borders
  border0:     "#E0E0E0",   // grey-300 — default border
  border1:     "#BDBDBD",   // grey-400 — medium emphasis border
  border2:     "#9E9E9E",   // grey-500 — strong border

  // Text
  text0:       "#212121",   // text-primary — headings, labels
  text1:       "#3D3D3D",   // text-secondary — body text
  text2:       "#757575",   // grey-600 — secondary/meta
  text3:       "#9E9E9E",   // grey-500 — placeholder, disabled

  // Navigation
  navBg:       "#1A2233",
  navBorder:   "#2A3447",
  navText:     "#C8D0DC",
  navActive:   "#FFFFFF",
  navActiveBg: "#2A3EB1",   // alpha/primary-700 — active nav item pill

  // Primary interactive (alpha/primary)
  blue:        "#3D4FD6",   // alpha/primary-500
  blueHover:   "#2A3EB1",   // alpha/primary-700
  blueBg:      "#EEF0FB",   // alpha/primary-50
  blueBorder:  "#D5D9F5",   // alpha/primary-100

  // Teal — inbound, info (gamma/accent/cyan)
  teal:        "#00796B",
  tealBg:      "#E0F2F1",
  tealBorder:  "#80CBC4",

  // Amber — warning, draft (gamma/accent/orange)
  amber:       "#C47D0A",
  amberBg:     "#FFF8E1",
  amberBorder: "#FFE082",

  // Red — error, failed (gamma/accent/red)
  red:         "#C62828",
  redBg:       "#FFEBEE",
  redBorder:   "#EF9A9A",

  // Green — active, success (gamma/accent/green)
  green:       "#2E7D32",
  greenBg:     "#E8F5E9",
  greenBorder: "#A5D6A7",

  // Purple — outbound (gamma/accent/purple)
  purple:      "#6A1B9A",
  purpleBg:    "#F3E5F5",
  purpleBorder:"#CE93D8",
};

const FONT = "'Roboto', 'Segoe UI', system-ui, sans-serif";
const MONO = "'Roboto Mono', 'Fira Code', 'Consolas', monospace";
```

---

## 9. Stepper Component Spec

From Figma `Stepper.png`:

| State | Indicator | Label |
|---|---|---|
| Inactive | Grey circle with `#` number, grey border `border0` | `text3` 14px medium |
| Active | Filled circle `blue` (#3D4FD6), white number | `blue` 14px **bold**, underline rule below |
| Completed | Green filled circle with checkmark | `text1` 14px medium |
| Back to List | Left-arrow `←` + label, always leftmost | `text2` 14px |

Stepper bar uses `border0` background with steps spaced equally. Active step has a `2px solid blue` underline directly below the step row.

---

## 10. Icon Library

From `Icons.png`, the product uses **Ionicons** as the primary icon library (already in use via Tailwind/CDN pattern). Secondary sources visible: Feather Icons, Heroicons, Bootstrap Icons.

**Sizing standards:**
- 12px — inline with body text (status dots)
- 16px — form field icons, table row icons
- 18px — card action icons, nav icons
- 20px — primary action icons in headers
- 24px — empty state illustration icons (large)

---

## 11. What Changes vs. Original Code

| Original | New (Figma-aligned) | Impact |
|---|---|---|
| `IBM Plex Sans` | `Roboto` | Update `FONT` constant + Google Fonts link |
| `IBM Plex Mono` | `Roboto Mono` | Update `MONO` constant + Google Fonts link |
| `C.blue = #1D6FE8` | `#3D4FD6` | Cooler purple-blue primary |
| `C.blueHover = #1558C0` | `#2A3EB1` | Matches alpha/primary-700 |
| `C.pageBg = #F0F2F5` | `#F5F5F5` | Pure grey-100 |
| `C.bg1 = #F7F8FA` | `#FAFAFA` | grey-50 — preserves surface layering *(Figma spec was #F5F5F5 = pageBg; adjusted)* |
| `C.text0 = #0F1923` | `#212121` | Figma's actual near-black |
| `C.text1 = #3D4A5C` | `#3D3D3D` | Neutral grey, not blue-grey |
| `C.red = #C42B2B` | `#C62828` | gamma/accent/red-700 |
| `C.green = #1A7A3C` | `#2E7D32` | gamma/accent/green-700 |
| `C.bg2 = #EFF1F4` | `#EEEEEE` | Pure grey-200 |
| `C.border0 = #D1D5DC` | `#E0E0E0` | Pure grey-300 |
| Nav active highlight | Add `navActiveBg: #2A3EB1` | Pill highlight on active nav item |

---

## 12. Unchanged Rules

These rules from the product spec remain **fully preserved**:

- System = reusable connection context; Integration = one use-case flow
- Direction before Method; they are never merged
- Step 2 inherits request context from Step 1 (read-only)
- Push-only systems are valid, not incomplete
- Monospace for codes, URLs, IDs, payloads
- Left-rail 4px border: teal = inbound, purple = outbound
- Placeholder pattern: `bg2` fill + `text3` text + `COMING SOON` 9px uppercase
- Footer action order: Cancel · Save as Draft · Primary
- Light industrial enterprise character — functional, dense, not decorative
