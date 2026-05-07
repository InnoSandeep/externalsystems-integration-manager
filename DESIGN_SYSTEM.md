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
14. [Integration Manager — Figma Source of Truth](#14-integration-manager--figma-source-of-truth)
15. [Platform Shell Pattern](#15-platform-shell-pattern)
16. [Sidebar Behavior](#16-sidebar-behavior)
17. [Header Pattern](#17-header-pattern)
18. [Toolbar Pattern](#18-toolbar-pattern)
19. [Filter Chips](#19-filter-chips)
20. [System Card Pattern](#20-system-card-pattern)
21. [Card Actions](#21-card-actions)
22. [Status Badges](#22-status-badges)
23. [Integration Manager Typography Map](#23-integration-manager-typography-map)
24. [Figma → C Token Alignment Table](#24-figma--c-token-alignment-table)
25. [Spacing, Radius & Elevation Quick Reference](#25-spacing-radius--elevation-quick-reference)
26. [Do / Don't](#26-do--dont)
27. [Implementation Notes](#27-implementation-notes)

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
| 2026-05-08 | Added sections 14–27: Integration Manager Figma design patterns — platform shell, sidebar behavior, header, toolbar, filter chips, system card, card actions, status badges, typography map, token alignment table, spacing/radius/elevation quick ref, Do/Don't, and implementation notes. | Figma node 1:17663 |

---

## 14. Integration Manager — Figma Source of Truth

**Primary design node:** `1:17663` in Figma file `2dRnIiNN2EAqshdjHgPr8Q`

This node shows the Integration Manager home screen ("Systems" list) as it exists in the product Figma file. All layout dimensions, typography, color values, and component patterns in sections 15–26 are derived from this node unless otherwise noted.

> **Note:** Figma prototype URLs (`.../proto/...`) expire and may redirect. Use the design file URL with `?node-id=1:17663` for stable access. Screenshot captures in the Update Log take priority over memory if the Figma spec changes.

**Related screens in the same file:**
- System Detail page (integrations list)
- Add Integration drawer
- Edit Integration drawer

---

## 15. Platform Shell Pattern

The Integration Manager is a **module inside the Innovapptive platform shell**, not a standalone app. The shell provides the sidebar and header; the module renders in the content area.

### Layout geometry

```
┌─────────────────────────────────────────────────────────────────┐
│  PlatformHeader  (height: 64px, full width, z-index: 100)       │
├──────────┬──────────────────────────────────────────────────────┤
│          │                                                       │
│ Sidebar  │  Content area (flex: 1, overflow-y: auto)            │
│ 68px     │                                                       │
│ (default)│  ┌───────────────────────────────────────────────┐   │
│          │  │  White rounded container                       │   │
│          │  │  margin: 16px · radius: 8px                    │   │
│          │  │  background: #FFFFFF                           │   │
│          │  └───────────────────────────────────────────────┘   │
└──────────┴──────────────────────────────────────────────────────┘
```

### Shell dimensions

| Element | Value | Token |
|---|---|---|
| Header height | 64px | `spacing-16` |
| Sidebar width (compact) | 68px | — |
| Sidebar width (expanded) | 220px | — |
| Content container margin | 16px all sides | `spacing-4` |
| Content container radius | 8px | `radius-md` |
| Content container bg | `#FFFFFF` | `C.bg0` |
| Page background | `#EFF1F5` | `C.pageBg` |

### In the prototype

The shell is composed of three sibling components in `App`:
1. `PlatformSidebar` — left column, `position:relative`
2. Expand/collapse toggle button — `position:fixed`, overlays the sidebar boundary
3. Content column — `flex:1`, contains `PlatformHeader` + scrollable content area

---

## 16. Sidebar Behavior

### Default state

The sidebar is **compact (68px) by default** on the Integration Manager home screen. Only icons are visible; labels are hidden.

### Expanded state

Width expands to 220px. Module labels become visible alongside icons.

### Toggle button

- **Position:** `fixed`, `top: 72px`, `left` tracks sidebar width (`206px` expanded / `54px` compact)
- **Style:** 28×28px circle, `C.blue` fill, white chevron SVG, `box-shadow: 0 2px 8px rgba(0,0,0,0.18)`
- **Animation:** `transition: left 0.15s` follows the sidebar slide
- **Placement rationale:** The button is a sibling in `App` (not a child of `PlatformSidebar`) to avoid clipping by `overflow:hidden` on the sidebar container

### Sidebar items

| Key | Label | Notes |
|---|---|---|
| `dashboard` | Dashboard | — |
| `integration-manager` | Integration Manager | **Active item** — highlighted `C.navActiveBg` |
| `workflow-builder` | Workflow Builder | — |
| `my-approvals` | My Approvals | — |
| `sites` | Sites | Management section |
| `assets` | Assets | — |
| `materials` | Materials | — |
| `work-orders` | Work Orders | — |
| `reports` | Reports | Configure section |
| `roles` | Roles & Permissions | — |
| `notifications` | Notifications | — |
| `data-quality` | Data Quality | Integrations section |
| `api-gateway` | API Gateway | — |
| `connectors` | Connectors | — |
| `help` | Help & Support | — |

### Icon approach

Icons use the inline SVG `PlatformIcon` component (stroke-based approximations). When `innovapptive-font` becomes available, replace `PlatformIcon` entirely — the `itemKey` strings are already the intended glyph names.

---

## 17. Header Pattern

### Dimensions and surface

| Property | Value | Token |
|---|---|---|
| Height | 64px | `spacing-16` |
| Background | `#FFFFFF` | `C.bg0` |
| Bottom border | `1px solid #E2E4E9` | `C.border0` |
| Horizontal padding | 24px | `spacing-6` |
| z-index | 100 | — |

### Title

| Property | Value | Token/Scale |
|---|---|---|
| Text | "Integration Manager" | — |
| Font | Roboto | `FONT` |
| Size | 18px | `title/medium/t3` |
| Weight | 500 (Medium) | — |
| Line height | 133% (≈ 24px) | — |
| Color | `#2A2B30` | `C.text0` |

### Right-side controls

1. **Notification bell** — 20px SVG icon button, `C.text1` color, `C.bg1` hover background, 8px radius
2. **Profile block** — avatar circle (32px, `C.blue` bg, white initials) + user name text (`C.text0`, 12px/500) + Innovapptive logo square (32×32)

---

## 18. Toolbar Pattern

The toolbar sits at the top of the systems list content area, inside the white container.

### Structure (left → right)

```
[ System Type ▾ ]  [ ⊞ ]  N Systems     [Search…]  [ + Add System ]
```

| Element | Details |
|---|---|
| **System Type dropdown** | Floating-label select; label "System Type", 160px width; options: All + unique system categories |
| **Filter icon button** | 32×32px, `C.border0` border, 8px radius, `C.text1` icon; opens filter panel (future) |
| **Count label** | `"{N} Systems"`, `C.text1`, 12px/400 — updates live as filters change |
| **Search input** | Right-aligned, 220px, 8px radius, `C.border0` border, magnifier icon prefix, placeholder "Search systems…" |
| **Add System button** | Primary (`C.blue` bg, white text, `+` prefix), 8px radius, 12px/500 |

### Toolbar spacing

- Container padding: `16px 16px 12px` (top/sides, less bottom before filter chips)
- Gap between left group and right group: `flex: 1` spacer
- Gap within left group: 8px
- Gap within right group: 8px

---

## 19. Filter Chips

Filter chips appear below the toolbar and allow quick status filtering of the systems list.

### Design

- **Container:** `flex-wrap`, `gap: 8px`, `padding: 0 16px 12px`
- **Chip shape:** `border-radius: 8px` (`radius-md`)
- **Chip surface:** `C.bg3` (`rgba(143,147,163,0.25)`) default; `C.blueBg` + `C.blueBorder` border when active
- **Chip padding:** `4px 10px`
- **Typography:** 12px / 500 (`title/medium/t6`), `C.text1`

### Standard chips for Systems list

| Chip key | Label | Status dot color |
|---|---|---|
| `ready` | Configured | `C.green` (`#1C8D4F`) |
| `draft` | Draft | `C.text2` (`#8F93A3`) |
| `needs_attention` | Needs Attention | `C.red` (`#B42318`) |

### Dot spec

- Size: 6px circle (`border-radius: 9999px`)
- Position: inline-flex, `margin-right: 6px`, vertically centered
- Color: matches the status color listed above

### Active chip

When a chip is active (selected), apply:
```
background: C.blueBg  (#ECEFFF)
border: 1px solid C.blueBorder  (#C3CCFF)
color: C.blue  (#3D5AFE)
```
The dot retains its original status color even when the chip is active.

---

## 20. System Card Pattern

### Layout and surface

| Property | Value |
|---|---|
| Flex basis | `0 1 424px` (grows to fill row, max ~424px) |
| Min width | 280px |
| Background | `#FFFFFF` (`C.bg0`) |
| Border | `1px solid #E2E4E9` (`C.border0`) |
| Border radius | 8px (`radius-md`) |
| Padding | 16px (`spacing-4`) |
| Box shadow | `0px 1px 2px rgba(0,0,0,0.06)` (`elevation-sm`) |

### Card internal structure (top → bottom)

```
┌── Row 1: Logo/Initials  ·  Status Badge ──────────────────────┐
│                                                                │
│  Row 2: System Name (16px/500)                                 │
│  Row 3: Category (12px/400, C.text2)                          │
│                                                                │
│  ── divider ──────────────────────────────────────────────── │
│                                                                │
│  Row 4: "N active integrations"  ·  [View Details / Connect]  │
└────────────────────────────────────────────────────────────────┘
```

### Logo / Initials block

- Container: 40×40px, `border-radius: 8px`, `C.bg1` background
- **With logo URL:** `<img>` fills the container, `object-fit: contain`, 4px padding
- **Without logo (null):** Two-letter initials, `C.blue` text, 14px/700, `C.blueBg` background
- Initials formula: first letter of each of the first two words in `system.name`, uppercase

### System name

- Font: 16px / 500 (`title/medium/t4`)
- Color: `C.text0` (`#2A2B30`)
- Margin top: 12px from logo row

### Category subtitle

- Font: 12px / 400 (`body/regular/b4`)
- Color: `C.text2` (`#8F93A3`)
- Margin top: 2px

### Integration count

- Font: 12px / 400 (`body/regular/b4`)
- Color: `C.text1` (`#525560`)
- Text: `"{N} active integration{s}"`; `N=0` shows "No active integrations" in `C.text2`

### Card grid

- Container: `display: flex`, `flex-wrap: wrap`, `gap: 16px`, `padding: 16px`

---

## 21. Card Actions

Each card has a single action button in the bottom-right, chosen based on integration count:

| Condition | Button label | Style |
|---|---|---|
| `liveCount > 0` | View Details | `background: C.blueBg` (`#ECEFFF`), `color: C.blue`, `border: 1px solid C.blueBorder` |
| `liveCount === 0` | Connect | `background: C.blue` (`#3D5AFE`), `color: #FFFFFF`, no border |

**Shared button styles:**
- Font: 12px / 500 (`title/medium/t6`)
- Border radius: 6px
- Padding: `6px 14px`
- Cursor: pointer
- No box-shadow

> Use "Connect" only when there are zero active integrations. Using it when integrations exist would mislead the user into thinking no connection is configured.

---

## 22. Status Badges

Status badges appear on cards (system status) and in the integrations list (integration status).

### Dimensions and shape

| Property | Value |
|---|---|
| Height | 18px (line-height based, not fixed) |
| Padding | `2px 8px` |
| Border radius | 4px (`radius-sm`) |
| Font | 11px / 500 (`title/medium/t6` capped at 11px for badge context) |
| Display | `inline-flex`, `align-items: center` |
| Border | `1px solid {statusBorder}` |

### Badge colors (STATUS_CONFIG)

| Status key | Label | Text color | Background | Border |
|---|---|---|---|---|
| `ready` | Configured | `C.green` `#1C8D4F` | `rgba(40,199,111,0.25)` | `C.greenBorder` `#28C76F` |
| `draft` | Draft | `C.text1` `#525560` | `rgba(143,147,163,0.25)` | `C.border0` `#E2E4E9` |
| `needs_attention` | Needs Attention | `C.red` `#B42318` | `rgba(217,45,32,0.25)` | `C.redBorder` `#D92D20` |
| `active` | Active | `C.green` | `rgba(40,199,111,0.25)` | `C.greenBorder` |
| `ready_to_publish` | Ready to Publish | `C.blue` `#3D5AFE` | `C.blueBg` `#ECEFFF` | `C.blueBorder` `#C3CCFF` |
| `failed` | Failed | `C.red` | `rgba(217,45,32,0.25)` | `C.redBorder` |
| `disabled` | Disabled | `C.text2` `#8F93A3` | `C.bg2` `#E2E4E9` | `C.border0` |

**Key rule:** Badge backgrounds use **transparent rgba values**, not solid fills. This keeps badges readable on any card surface without blending issues.

---

## 23. Integration Manager Typography Map

Precise type tokens used in each UI region of Integration Manager. Supplements the global type scale (section 1).

| UI region | Text | Size | Weight | Color token |
|---|---|---|---|---|
| PlatformHeader title | "Integration Manager" | 18px | 500 | `C.text0` |
| Toolbar count | "N Systems" | 12px | 400 | `C.text1` |
| Toolbar dropdown label | "System Type" | 12px | 500 | `C.text1` |
| Search placeholder | "Search systems…" | 12px | 400 | `C.text2` |
| Add System button | "+ Add System" | 12px | 500 | `#FFFFFF` |
| Filter chip label | status name | 12px | 500 | `C.text1` (default) / `C.blue` (active) |
| System card name | system.name | 16px | 500 | `C.text0` |
| System card category | system.category | 12px | 400 | `C.text2` |
| Integration count | "N active…" | 12px | 400 | `C.text1` |
| Card action button | "View Details" / "Connect" | 12px | 500 | `C.blue` / `#FFFFFF` |
| Status badge | status.label | 11px | 500 | status-specific |
| Sidebar item label | module name | 12px | 400 | `C.navText` |
| Sidebar active item | module name | 12px | 500 | `C.navActive` |
| Profile name | user name | 12px | 500 | `C.text0` |

---

## 24. Figma → C Token Alignment Table

Observed hex values in Figma node `1:17663` mapped to their `C` object equivalents. Use this table when a Figma inspection shows a hex that you need to identify.

| Figma hex | Figma role | `C` token | Notes |
|---|---|---|---|
| `#EFF1F5` | Page background | `C.pageBg` | Beta Grey-100 |
| `#FFFFFF` | Card surface, header bg | `C.bg0` | White |
| `#E2E4E9` | Card border, divider | `C.border0` | Beta Grey-200 |
| `#8F93A3` | Placeholder, disabled | `C.text2` / `C.text3` | Beta Grey-300 |
| `#666975` | Icon at rest | `C.border2` | Beta Grey-400 |
| `#525560` | Body text, secondary labels | `C.text1` | Beta Grey-500 |
| `#2A2B30` | Primary text, headings | `C.text0` | Beta Grey-600 |
| `#3D5AFE` | Primary buttons, links | `C.blue` | Alpha Primary-500 |
| `#ECEFFF` | Hover bg, View Details btn bg | `C.blueBg` | Alpha Primary-50 |
| `#C3CCFF` | View Details btn border | `C.blueBorder` | Alpha Primary-100 |
| `#2B40B4` | Nav active bg, button hover | `C.blueHover` / `C.navActiveBg` | Alpha Primary-700 |
| `#1A2233` | Sidebar background | `C.navBg` | Dark navy |
| `#C8D0DC` | Sidebar item text | `C.navText` | — |
| `#1C8D4F` | Configured badge text | `C.green` | Green-700 |
| `rgba(40,199,111,0.25)` | Configured badge bg | `C.greenBg` | Green-500 25% |
| `#28C76F` | Configured badge border | `C.greenBorder` | Green-500 |
| `#B42318` | Error badge text | `C.red` | Red-700 |
| `rgba(217,45,32,0.25)` | Error badge bg | `C.redBg` | Red-500 25% |
| `#D92D20` | Error badge border | `C.redBorder` | Red-500 |
| `rgba(143,147,163,0.25)` | Draft badge bg, chip surface | `C.bg3` | Grey-300 25% / `$color-bg-chip` |

---

## 25. Spacing, Radius & Elevation Quick Reference

Practical lookup for the most common values in Integration Manager screens.

### Spacing used

| Location | Value | Spacing token |
|---|---|---|
| Page background → content container | 16px | `spacing-4` |
| Card internal padding | 16px | `spacing-4` |
| Card grid gap | 16px | `spacing-4` |
| Toolbar padding (top/sides) | 16px | `spacing-4` |
| Filter chip gap | 8px | `spacing-2` |
| Header horizontal padding | 24px | `spacing-6` |
| Sidebar icon padding (compact) | 24px centered (auto) | — |
| Logo/initials block size | 40×40px | — |

### Border radius used

| Component | Value | Token |
|---|---|---|
| System card | 8px | `radius-md` |
| Content container | 8px | `radius-md` |
| Filter chips | 8px | `radius-md` |
| Logo/initials block | 8px | `radius-md` |
| Status badge | 4px | `radius-sm` |
| Card action button | 6px | between `radius-sm` and `radius-md` |
| Toggle button | 9999px | `radius-full` |
| Status dot | 9999px | `radius-full` |

### Elevation used

| Component | Value | Token |
|---|---|---|
| System card | `0px 1px 2px rgba(0,0,0,0.06)` | `elevation-sm` |
| Sidebar toggle button | `0px 2px 8px rgba(0,0,0,0.18)` | custom |
| Dropdown menus | `2px 2px 12px rgba(0,0,0,0.12)` | `elevation-md` |
| Drawers | `0px 4px 24px rgba(0,0,0,0.16)` | `elevation-lg` |

---

## 26. Do / Don't

### Colors

| Do | Don't |
|---|---|
| Use `C.*` tokens for all colors | Hard-code hex values in inline styles |
| Use transparent rgba for badge backgrounds | Use solid fills for status badge backgrounds |
| Use `C.bg3` (`rgba(143,147,163,0.25)`) for chip/tag surfaces | Use `#8F93A3` solid for chip backgrounds (makes text invisible) |
| Use `C.text0` or `C.text1` for text on chip/badge surfaces | Use `C.text2`/`C.text3` for text on `C.bg3` backgrounds |

### Typography

| Do | Don't |
|---|---|
| Use Roboto via the `FONT` constant | Reference "IBM Plex Sans" or other fonts |
| Use `title/medium/t3` (18px/500) for the header title | Use bold (700) for the header module title |
| Use 12px as the default UI text size | Use anything below 10px |

### Layout

| Do | Don't |
|---|---|
| Keep sidebar compact (68px) as the default state | Open the sidebar expanded by default |
| Place the toggle button as a `position:fixed` sibling in App | Place the toggle inside `PlatformSidebar` (gets clipped by `overflow:hidden`) |
| Use `flex: 1` on the content column | Give the content column a fixed width |
| Use `C.pageBg` (`#EFF1F5`) as the outer page background | Use white or transparent as the page background |

### Cards

| Do | Don't |
|---|---|
| Show "View Details" (blue outlined) when integrations exist | Show "Connect" for systems that already have active integrations |
| Show initials with `C.blueBg` background when no logo URL is set | Show a broken `<img>` tag or empty box |
| Use `flex: 0 1 424px` with `flex-wrap` for the card grid | Use CSS Grid with a fixed column count |

### Status

| Do | Don't |
|---|---|
| Label `ready` status as "Configured" (Figma language) | Use "Active" or "Ready" as the label for the `ready` status key |
| Label `draft` with neutral grey tones | Use amber/orange for draft status |

---

## 27. Implementation Notes

### Prototype constraints

The prototype is a single-file CDN React 18 app (`IntegrationManager.js`). There is no build step, no CSS modules, and no package imports beyond CDN React/Babel/ReactDOM. All styles are inline JS objects.

- **Token changes** → update the `C` object (and `FONT`/`MONO` constants) near the top of the file
- **Status label/color changes** → update `STATUS_CONFIG` — it is the single source of truth for all badge text and colors
- **New icons** → add to the `icons` map in `PlatformIcon`; use stroke-based SVG at `viewBox="0 0 20 20"`
- **Logo URLs** → update `SYSTEM_LOGOS` map; `null` values fall back to initials automatically

### SVG icons (`PlatformIcon`)

Icons are stroke-based inline SVGs at 20×20. They are placeholder approximations — when `innovapptive-font` (or an agreed icon library CDN) is available:
1. Remove the `PlatformIcon` function entirely
2. Replace `<PlatformIcon itemKey={item.key} .../>` calls with the font icon component
3. The `itemKey` strings match the intended glyph names in the design system

### System logo infrastructure

`SYSTEM_LOGOS` is a map of `systemId → URL | null`. All entries are currently `null` (no stable hosted logo URLs exist yet). When logo URLs are available:
1. Add them to `SYSTEM_LOGOS` by system ID
2. `getSystemLogo(system)` will automatically return the URL
3. `SystemCard` renders an `<img>` when a URL is present, falls back to initials when `null`

### Figma URL stability

The Figma **prototype** URL (`figma.com/proto/...`) uses a one-time token that expires and redirects. For future reference, use the **design file** URL:

```
https://www.figma.com/design/2dRnIiNN2EAqshdjHgPr8Q/?node-id=1:17663
```

(Replace `:` with `-` in the `node-id` query param when using the Figma MCP tool: `node-id=1-17663`.)

### Storybook updates

Per the daily update requirement (section header in this file), fetch `https://cwp-design-system-storybook-2026.netlify.app` at the start of each session. The site is JS-rendered — token values must be pasted from the browser into the `[POPULATE FROM BROWSER]` placeholders in section 13 when they change. Confirmed changes go in the Update Log table above.
