# Integration Manager — Design System
**Version:** 2.0 · 2026-05-05  
**Source:** CWP Design System Storybook (https://cwp-design-system-storybook-2026.netlify.app)  
**Applies to:** IntegrationManager.js and all future screens

> **Usage rule:** This file is authoritative. All UI changes must use tokens from this file.
> When the Storybook updates, update this file and commit on `develop`. Sections marked
> **[PENDING]** have not yet been extracted from the Storybook.

---

## Table of Contents

1. [Font System](#1-font-system)
2. [Color System — Primitives](#2-color-system--primitives)
3. [Color System — Semantics](#3-color-system--semantics)
4. [Spacing](#4-spacing)
5. [Border Radius](#5-border-radius)
6. [Elevation / Shadows](#6-elevation--shadows)
7. [Component Token Map — `C` object](#7-component-token-map--c-object)
8. [Stepper Component Spec](#8-stepper-component-spec)
9. [Icon Library](#9-icon-library)
10. [CWP Button Component Spec](#10-cwp-button-component-spec)
11. [Side Navigation Spec](#11-side-navigation-spec)
12. [Applying This System to the Prototype](#12-applying-this-system-to-the-prototype)
13. [Update Log](#13-update-log)

---

## 1. Font System

### Primary Typeface

```
font-family: 'Roboto', 'Segoe UI', system-ui, sans-serif
```

Source: Google Fonts — Roboto (Regular 400 · Medium 500 · Bold 700)

### Monospace Typeface

```
font-family: 'Roboto Mono', 'Fira Code', 'Consolas', monospace
```

Used for: System Codes, endpoint URLs, listener IDs, DLQ IDs, JSON payloads.

### Base Font Size

**12px is the base.** Most UI text (form inputs, table cells, labels, descriptions, helper text, buttons) defaults to 12px. Larger sizes are reserved for headings. Never use below 10px.

### Type Scale

#### Title / Bold (weight 700)

| Token | Size | Line Height | Letter Spacing | Usage |
|---|---|---|---|---|
| `title/bold/t1` | 28px | 130% | -1% | Page titles, hero headings |
| `title/bold/t2` | 24px | 133% | -0.8% | Section headings |
| `title/bold/t3` | 18px | 133% | -0.5% | Drawer titles, card group headers |
| `title/bold/t4` | 16px | 138% | -0.3% | Card section headers |
| `title/bold/t5` | 14px | 143% | 0% | Sub-section labels, column headers |
| `title/bold/t6` | 12px | 133% | 0% | Chip labels, status badge labels, table headers |
| `title/bold/t7` | 10px | 140% | 1% | Micro-labels, badges, stepper numbers |

#### Title / Medium (weight 500)

| Token | Size | Line Height | Letter Spacing | Usage |
|---|---|---|---|---|
| `title/medium/t1` | 28px | 130% | -1% | — |
| `title/medium/t2` | 24px | 133% | -0.8% | — |
| `title/medium/t3` | 18px | 133% | -0.5% | — |
| `title/medium/t4` | 16px | 138% | -0.3% | Panel headers, popup headers |
| `title/medium/t5` | 14px | 143% | 0% | Card titles, sub-headings |
| `title/medium/t6` | 12px | 133% | 0% | Labels, tab text, button text, table headers |
| `title/medium/t7` | 10px | 140% | 1% | Badges, small labels, stepper numbers |

#### Body / Regular (weight 400)

| Token | Size | Line Height | Letter Spacing | Usage |
|---|---|---|---|---|
| `body/regular/b1` | 18px | 156% | 0% | Long-form help text |
| `body/regular/b2` | 16px | 150% | 0% | Body paragraph, drawer description |
| `body/regular/b3` | 14px | 143% | 0% | Default body text, button large text |
| `body/regular/b4` | 12px | 150% | 0% | **Default** — form inputs, helper text, table cells |
| `body/regular/b5` | 10px | 140% | 2% | Captions, character counts, timestamps |

### Typography Quick Reference

| Component context | Token | Size | Weight |
|---|---|---|---|
| Drawer / modal title | `title/bold/t3` | 18px | 700 |
| Page section heading | `title/bold/t4` | 16px | 700 |
| Card title | `title/medium/t5` | 14px | 500 |
| Form field label | `title/medium/t6` | 12px | 500 |
| Input text / table cell | `body/regular/b4` | 12px | 400 |
| Table column header | `title/bold/t6` | 12px | 700 |
| Status badge | `title/medium/t6` | 12px | 500 |
| Helper / description text | `body/regular/b4` | 12px | 400 |
| Timestamp / metadata | `body/regular/b5` | 10px | 400 |
| COMING SOON chip | `title/bold/t7` | 10px | 700 uppercase |
| Monospace (codes, URLs) | — | 12px | 400 |
| Button text | `title/medium/t6` | 12px | 500 |

---

## 2. Color System — Primitives

CWP 2.0 uses a two-tier architecture: **Primitives** (raw palette) and **Semantics** (contextual references). Always prefer semantic tokens in component code; use primitives only when no semantic token fits.

### Alpha / Primary (Brand)

#### Solid

| Stop | Hex | Usage |
|---|---|---|
| 50 | `#ECEFFF` | Hover backgrounds, selected row tint |
| 100 | `#C3CCFF` | Focus ring fill, light chip background |
| 300 | `#7D90FE` | Focused border |
| **500** | **`#3D5AFE`** | **Primary interactive — buttons, active nav, links** |
| 700 | `#2B40B4` | Button hover, active state dark |
| 900 | `#1A266B` | Pressed state |

#### Transparent

| Level | Value |
|---|---|
| 75% | `rgba(61,90,254,0.75)` |
| 50% | `rgba(61,90,254,0.50)` |
| 25% | `rgba(61,90,254,0.25)` |
| 10% | `rgba(61,90,254,0.10)` |
| 5% | `rgba(61,90,254,0.05)` |

### Beta / Grey (Neutrals)

#### Solid

| Stop | Hex | Usage |
|---|---|---|
| White | `#FFFFFF` | Card surface, input bg, modal bg |
| 100 | `#EFF1F5` | Page background, surface |
| 200 | `#E2E4E9` | Dividers, default borders |
| 300 | `#8F93A3` | Placeholder text, disabled icon, medium border |
| 400 | `#666975` | Icon at rest |
| 500 | `#525560` | Body text secondary |
| 600 | `#2A2B30` | Body text primary, headings |
| 700 | `#0F1115` | High-contrast text |

#### Transparent

| Level | Value |
|---|---|
| White 10% | `rgba(255,255,255,0.10)` |
| Grey 25% | `rgba(143,147,163,0.25)` |
| Black 50% | `rgba(0,0,0,0.50)` |

### Gamma / Accents

Each accent has solid stops (50 · 100 · 300 · 500 · 700 · 900) and transparent levels (5% · 10% · 25% · 50% · 75%).

#### Yellow
| Stop | Hex |
|---|---|
| 50 | `#FFFBE6` |
| 100 | `#FFF3B0` |
| 300 | `#FFE454` |
| 500 | `#FFD700` |
| 700 | `#B59900` |
| 900 | `#6B5A00` |

#### Purple
| Stop | Hex |
|---|---|
| 50 | `#F3F0FF` |
| 100 | `#DBD1FF` |
| 300 | `#B19DFF` |
| 500 | `#8A6CFF` |
| 700 | `#624DB5` |
| 900 | `#3A2D6B` |

#### Cyan
| Stop | Hex |
|---|---|
| 50 | `#EDF9FD` |
| 100 | `#C8EEF8` |
| 300 | `#88D9EF` |
| 500 | `#4DC7E7` |
| 700 | `#378DA4` |
| 900 | `#205461` |

#### Orange
| Stop | Hex |
|---|---|
| 50 | `#FFF7EC` |
| 100 | `#FFE5C4` |
| 300 | `#FFC77F` |
| 500 | `#FFAB40` |
| 700 | `#B5792D` |
| 900 | `#6B481B` |

#### Green
| Stop | Hex |
|---|---|
| 50 | `#EAF9F1` |
| 100 | `#BCEED2` |
| 300 | `#6FD99F` |
| 500 | `#28C76F` |
| 700 | `#1C8D4F` |
| 900 | `#11542F` |

#### Red
| Stop | Hex |
|---|---|
| 50 | `#FFEFEF` |
| 100 | `#FFCCCC` |
| 300 | `#FF9292` |
| 500 | `#D92D20` |
| 700 | `#B42318` |
| 900 | `#912018` |

#### Teal
| Stop | Hex |
|---|---|
| 50 | `#E6F5F3` |
| 100 | `#B0DEDA` |
| 300 | `#54B9AF` |
| 500 | `#009688` |
| 700 | `#006B61` |
| 900 | `#003F39` |

#### Orchid
| Stop | Hex |
|---|---|
| 50 | `#F5E9F7` |
| 100 | `#E0BCE7` |
| 300 | `#BD6ECA` |
| 500 | `#9C27B0` |
| 700 | `#6F1C7D` |
| 900 | `#42104A` |

#### Acid Green
| Stop | Hex |
|---|---|
| 50 | `#F8F9E9` |
| 100 | `#E8ECBA` |
| 300 | `#CDD76B` |
| 500 | `#B4C322` |
| 700 | `#808A18` |
| 900 | `#4C520E` |

#### Brown
| Stop | Hex |
|---|---|
| 50 | `#F2EEED` |
| 100 | `#D5CAC6` |
| 300 | `#A58D84` |
| 500 | `#795548` |
| 700 | `#563C33` |
| 900 | `#33241E` |

#### Ruby Red
| Stop | Hex |
|---|---|
| 50 | `#F5E7E9` |
| 100 | `#E0B5B9` |
| 300 | `#BC6068` |
| 500 | `#9B111E` |
| 700 | `#6E0C15` |
| 900 | `#41070D` |

---

## 3. Color System — Semantics

Use semantic tokens in all component code. They reference primitives by role.

### Text

| Token | References | Hex | Usage |
|---|---|---|---|
| `$color-text-primary` | Grey 600 | `#2A2B30` | Headings, labels, high-emphasis text |
| `$color-text-secondary` | Grey 500 | `#525560` | Body text, descriptions |
| `$color-text-placeholder` | Grey 300 | `#8F93A3` | Input placeholders |
| `$color-text-link` | Primary 500 | `#3D5AFE` | Links, interactive text |
| `$color-text-disabled` | Grey 300 | `#8F93A3` | Disabled input text |

### Background

| Token | References | Value | Usage |
|---|---|---|---|
| `$color-bg-default` | White | `#FFFFFF` | Cards, modals, inputs |
| `$color-bg-surface` | Grey 100 | `#EFF1F5` | Page background, surface layer |
| `$color-bg-overlay` | Black 50% | `rgba(0,0,0,0.50)` | Modal backdrop |
| `$color-bg-chip` | Grey 300 25% | `rgba(143,147,163,0.25)` | Chip/tag background |

### Border

| Token | References | Hex | Usage |
|---|---|---|---|
| `$color-border-default` | Grey 200 | `#E2E4E9` | Default input, card borders |
| `$color-border-focused` | Primary 300 | `#7D90FE` | Focused input ring |
| `$color-border-disabled` | Grey 100 | `#EFF1F5` | Disabled input border |

### Icon

| Token | References | Hex | Usage |
|---|---|---|---|
| `$color-icon-default` | Grey 400 | `#666975` | Default icon color |
| `$color-icon-active` | Grey 600 | `#2A2B30` | Active / hovered icon |
| `$color-icon-disabled` | Grey 300 | `#8F93A3` | Disabled icon |

### Status

| Token | References | Value | Usage |
|---|---|---|---|
| `$color-status-success-text` | Green 700 | `#1C8D4F` | Success text |
| `$color-status-success-bg` | Green 25% | `rgba(40,199,111,0.25)` | Success badge background |
| `$color-status-success-border` | Green 500 | `#28C76F` | Success badge border |
| `$color-status-success-icon` | Green 500 | `#28C76F` | Success icon |
| `$color-status-warning-text` | Orange 700 | `#B5792D` | Warning text |
| `$color-status-warning-bg` | Orange 25% | `rgba(255,171,64,0.25)` | Warning badge background |
| `$color-status-warning-border` | Orange 500 | `#FFAB40` | Warning badge border |
| `$color-status-warning-icon` | Orange 500 | `#FFAB40` | Warning icon |
| `$color-status-error-text` | Red 700 | `#B42318` | Error text |
| `$color-status-error-bg` | Red-500 25% | `rgba(217,45,32,0.25)` | Error badge background |
| `$color-status-error-border` | Red 500 | `#D92D20` | Error badge border |
| `$color-status-error-icon` | Red 500 | `#D92D20` | Error icon |

### Focus Ring

| Token | References | Value | Usage |
|---|---|---|---|
| `$color-focus-ring-default` | Grey 200 | `#E2E4E9` | Default focus outline |
| `$color-focus-ring-success` | Green 500 | `#28C76F` | Success state focus |
| `$color-focus-ring-warning` | Orange 500 | `#FFAB40` | Warning state focus |
| `$color-focus-ring-error` | Red 500 | `#D92D20` | Error state focus |

---

## 4. Spacing

4px base grid. All values are multiples of 4.

| Token | Value | Common use |
|---|---|---|
| `spacing-1` | 4px | Chip internal padding, badge padding, icon gap |
| `spacing-2` | 8px | Button internal padding (vertical), list item gap, input padding |
| `spacing-3` | 12px | Card internal padding (compact), form field gap |
| `spacing-4` | 16px | Card internal padding (standard), section gap |
| `spacing-5` | 20px | Drawer section gap |
| `spacing-6` | 24px | Drawer padding, modal padding |
| `spacing-8` | 32px | Between major sections |
| `spacing-10` | 40px | Page-level vertical rhythm |
| `spacing-12` | 48px | Large gaps, hero sections |
| `spacing-16` | 64px | Full-bleed spacers |

---

## 5. Border Radius

| Token | Value | Usage |
|---|---|---|
| `radius-none` | 0px | Table rows, dividers, flat elements |
| `radius-sm` | 4px | Badges, chips, small tags |
| `radius-md` | 8px | **Default** — cards, inputs, buttons, drawers |
| `radius-lg` | 12px | Modals, large panels |
| `radius-xl` | 16px | Floating panels, tooltips |
| `radius-full` | 9999px | Status dots, avatars, toggle pill |

---

## 6. Elevation / Shadows

| Token | CSS value | Usage |
|---|---|---|
| `elevation-none` | `none` | Flat surface — page bg, table rows |
| `elevation-sm` | `0px 1px 2px rgba(0,0,0,0.06)` | Cards, select menus |
| `elevation-md` | `2px 2px 12px rgba(0,0,0,0.12)` | Dropdowns |
| `elevation-lg` | `0px 4px 24px rgba(0,0,0,0.16)` | Modals, drawers, dialogs |
| `elevation-xl` | `0px 8px 32px rgba(0,0,0,0.20)` | Overlays, floating panels |

---

## 7. Component Token Map — `C` object

Direct replacement for the `C` constant in `IntegrationManager.js`. Reflects CWP 2.0 tokens.

```js
// ─── THEME (CWP 2.0) ─────────────────────────────────────────────────────────
const C = {
  // Surfaces — semantic background tokens
  pageBg:      "#EFF1F5",   // $color-bg-surface / Beta Grey-100
  bg0:         "#FFFFFF",   // $color-bg-default / White
  bg1:         "#EFF1F5",   // Grey-100 — hover rows, sidebars
                            // NOTE: same as pageBg in CWP 2.0. If surface layering
                            // collapses (hover invisible), use #F7F8FA as 1-step lift.
  bg2:         "#E2E4E9",   // $color-border-default / Grey-200 — disabled fills, dividers
  bg3:         "rgba(143,147,163,0.25)",  // $color-bg-chip — chip/badge surface (~#D7D8DD on white)

  // Borders
  border0:     "#E2E4E9",   // $color-border-default / Grey-200
  border1:     "#8F93A3",   // Grey-300 — medium emphasis
  border2:     "#666975",   // Grey-400 — strong border

  // Text — semantic text tokens
  text0:       "#2A2B30",   // $color-text-primary / Grey-600
  text1:       "#525560",   // $color-text-secondary / Grey-500
  text2:       "#8F93A3",   // $color-text-placeholder / Grey-300
  text3:       "#8F93A3",   // $color-text-disabled / Grey-300

  // Navigation — retain dark nav surface
  navBg:       "#1A2233",
  navBorder:   "#2A3447",
  navText:     "#C8D0DC",
  navActive:   "#FFFFFF",
  navActiveBg: "#2B40B4",   // Alpha/Primary-700

  // Primary interactive — Alpha/Primary
  blue:        "#3D5AFE",   // Alpha/Primary-500
  blueHover:   "#2B40B4",   // Alpha/Primary-700
  blueBg:      "#ECEFFF",   // Alpha/Primary-50
  blueBorder:  "#C3CCFF",   // Alpha/Primary-100
  blueFocus:   "#7D90FE",   // Alpha/Primary-300 — $color-border-focused

  // Teal — inbound direction, info callouts — Gamma/Teal
  teal:        "#009688",   // Teal-500
  tealBg:      "#E6F5F3",   // Teal-50
  tealBorder:  "#54B9AF",   // Teal-300

  // Amber / Warning — Gamma/Orange
  amber:       "#B5792D",   // Orange-700 — $color-status-warning-text
  amberBg:     "rgba(255,171,64,0.25)",  // $color-status-warning-bg
  amberBorder: "#FFAB40",   // Orange-500 — $color-status-warning-border

  // Red — error, failed — Gamma/Red
  red:         "#B42318",   // Red-700 — $color-status-error-text
  redBg:       "rgba(217,45,32,0.25)",   // Red-500 (#D92D20) 25% — $color-status-error-bg
  redBorder:   "#D92D20",   // Red-500 — $color-status-error-border

  // Green — active, success — Gamma/Green
  green:       "#1C8D4F",   // Green-700 — $color-status-success-text
  greenBg:     "rgba(40,199,111,0.25)",  // $color-status-success-bg
  greenBorder: "#28C76F",   // Green-500 — $color-status-success-border

  // Purple — outbound direction — Gamma/Purple
  purple:      "#8A6CFF",   // Purple-500
  purpleBg:    "#F3F0FF",   // Purple-50
  purpleBorder:"#B19DFF",   // Purple-300
};

const FONT = "'Roboto', 'Segoe UI', system-ui, sans-serif";
const MONO = "'Roboto Mono', 'Fira Code', 'Consolas', monospace";
```

### What changed from the previous Figma-based spec

| Token | Old (Figma v2) | New (CWP 2.0) | Note |
|---|---|---|---|
| `pageBg` | `#F5F5F5` | `#EFF1F5` | Grey-100 shifted to cooler tone |
| `bg2` | `#EEEEEE` | `#E2E4E9` | Grey-200 shifted |
| `border0` | `#E0E0E0` | `#E2E4E9` | Unified with Grey-200 |
| `border1` | `#BDBDBD` | `#8F93A3` | Grey-300 is now medium border |
| `text0` | `#212121` | `#2A2B30` | $color-text-primary / Grey-600 |
| `text1` | `#3D3D3D` | `#525560` | $color-text-secondary / Grey-500 |
| `text2` | `#757575` | `#8F93A3` | $color-text-placeholder / Grey-300 |
| `blue` | `#3D4FD6` | `#3D5AFE` | Primary-500 shifted brighter |
| `blueHover` | `#2A3EB1` | `#2B40B4` | Primary-700 |
| `blueBg` | `#EEF0FB` | `#ECEFFF` | Primary-50 |
| `blueBorder` | `#D5D9F5` | `#C3CCFF` | Primary-100 |
| `green` | `#2E7D32` | `#1C8D4F` | Green-700 (status-success-text) |
| `greenBg` | `#E8F5E9` | `rgba(40,199,111,0.25)` | Transparent per semantic token |
| `greenBorder` | `#A5D6A7` | `#28C76F` | Green-500 |
| `amber` | `#C47D0A` | `#B5792D` | Orange-700 |
| `amberBg` | `#FFF8E1` | `rgba(255,171,64,0.25)` | Transparent per semantic token |
| `amberBorder` | `#FFE082` | `#FFAB40` | Orange-500 |
| `red` | `#C62828` | `#B42318` | Red-700 |
| `redBg` | `#FFEBEE` | `rgba(217,45,32,0.25)` | Red-500 (#D92D20) 25% per semantic token |
| `redBorder` | `#EF9A9A` | `#D92D20` | Red-500 |
| `teal` | `#00796B` | `#009688` | Teal-500 |
| `tealBg` | `#E0F2F1` | `#E6F5F3` | Teal-50 |
| `tealBorder` | `#80CBC4` | `#54B9AF` | Teal-300 |
| `purple` | `#6A1B9A` | `#8A6CFF` | Gamma/Purple-500 |
| `purpleBg` | `#F3E5F5` | `#F3F0FF` | Purple-50 |
| `purpleBorder` | `#CE93D8` | `#B19DFF` | Purple-300 |
| `bg3` | `#8F93A3` | `rgba(143,147,163,0.25)` | $color-bg-chip — chip/badge surface; old solid value collided with text3 making chip labels invisible |

---

## 8. Stepper Component Spec

| State | Indicator | Label |
|---|---|---|
| Inactive | Grey circle, `border0` border, grey number | `text3` 12px medium (`title/medium/t6`) |
| Active | Filled circle `blue` (#3D5AFE), white number | `blue` 12px bold, underline rule below |
| Completed | Green filled circle, checkmark | `text1` 12px medium |
| Back to List | `←` arrow + label, always leftmost | `text2` 12px |

Stepper bar uses `border0` as background with steps spaced equally. Active step has a `2px solid blue` underline below the step row.

---

## 9. Icon Library

The product uses **Ionicons** as the primary icon library. Secondary sources: Feather Icons, Heroicons, Bootstrap Icons.

**Sizing standards:**

| Size | Context |
|---|---|
| 12px | Inline with body text, status dots |
| 16px | Form field icons, table row icons |
| 18px | Card action icons, nav icons |
| 20px | Primary action icons in headers |
| 24px | Empty state illustration icons |

---

## 10. CWP Button Component Spec

Inventoried from Storybook `index.json` — 25 stories.

### Hierarchies

| Name | Prototype equivalent |
|---|---|
| Primary | Blue-fill button (`C.blue` bg, white text) |
| Secondary Color | Bordered, `C.blue` border + text, transparent bg |
| Secondary Grey | Bordered, `C.border1` border, `C.text1` text |
| Tertiary Color | Ghost, `C.blue` text, no border |
| Tertiary Grey | Ghost, `C.text1` text, no border |
| Link Color | Inline text link, `C.blue` |
| Link Grey | Inline text link, `C.text2` |

### Sizes

| Size | Font token | Notes |
|---|---|---|
| Small | `title/medium/t7` 10px | **[PENDING exact height/padding from Storybook]** |
| Medium | `title/medium/t6` 12px | Default |
| Large | `body/regular/b3` 14px | **[PENDING]** |

### States
Default · Hover · Focused (`$color-border-focused` ring) · Disabled (opacity `0.6`)

### Intents
Success (green tokens) · Warning (orange tokens) · Error (red tokens)

### Icon support
Leading icon · Trailing icon · Notification dot

---

## 11. Side Navigation Spec

Documented in Storybook (`?path=/docs/side-navigation--docs`) as an original and experimental draft version.

The prototype currently uses a **top nav bar** (`TopNav`). If the product migrates to side nav, reference the Storybook for: active item treatment, icon placement, group/section patterns, and collapse behavior.

---

## 12. Applying This System to the Prototype

The prototype is a single-file React 18 app with inline styles. It cannot import Angular components directly.

**Workflow for any UI change:**
1. Look up the relevant semantic token in sections 2–3
2. Map it to the `C` object entry in section 7
3. Apply via inline style in `IntegrationManager.js`
4. Verify visually against the Storybook

**Implementation rules:**
- Colors → use `C.*` object (section 7) — never hard-code hex values
- Typography → use `FONT` / `MONO` constants, apply `fontSize` / `fontWeight` from the type scale table (section 1)
- Spacing → use values from the spacing scale (section 4) for `padding`, `margin`, `gap`
- Border radius → use values from section 5 for `borderRadius`
- Shadows → use values from section 6 for `boxShadow`
- Left-rail accent (4px border): Teal = inbound, Purple = outbound
- Footer action order: Cancel · Save as Draft · Primary CTA
- Disabled state: opacity `0.6`, `not-allowed` cursor

---

## 13. Update Log

| Date | Change | Source |
|---|---|---|
| 2026-05-05 | Full CWP 2.0 token population: color primitives (Alpha/Beta/Gamma), semantic tokens (text, bg, border, icon, status, focus ring), typography complete scale (t1-t7 bold/medium, b1-b5 regular), spacing (spacing-1 to spacing-16), border radius (none/sm/md/lg/xl/full), elevation (none/sm/md/lg/xl). All sections updated to CWP 2.0 — supersedes Figma v2 spec. | User-provided from CWP Storybook 2026 |
| 2026-05-05 | Initial Storybook inventory captured (structure only — 47 entries, component list). | `index.json` auto-fetch |
| 2026-05-05 | Fixed `bg3` token collision: changed from `#8F93A3` (solid Grey-300, same as `text3`) to `rgba(143,147,163,0.25)` ($color-bg-chip). Resolves invisible "Coming Soon" chip label on SelectionCard. SelectionCard tag text changed from `text3` to `text0` (#2A2B30) for ~9:1 contrast on chip surface. | P2 bug finding |
