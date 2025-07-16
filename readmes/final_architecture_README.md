# Prime Scale App: Final Architecture & Packaging Strategy

_Last updated: 2025-05-06_

This README consolidates and replaces previous frontend and architecture planning documents. It defines the final architecture and development direction for the Prime Scale App as a modular, JavaScript/java-based APK-ready environment.

---

## Core Principles

- **Frontend-first, JavaScript-native**
- **APK and PWA compatible** (Capacitor.js recommended)
- **Modular algorithm support** via drop-in JavaScript packages
- **No Python dependency required** for scale generation
- **Developer- and user-friendly** with hot-loadable modules and clean packaging

---

## Directory Structure

```
/prime-scale-app/
├── /public/               # Static assets (icon, manifest, splash)
├── /src/
│   ├── /modules/          # Scale algorithm modules (JS)
│   ├── /components/       # React components (tool popups, viewers, tray)
│   ├── /utils/            # Shared JS utilities (e.g. note conversion)
│   ├── /data/             # modules.json manifest + preloaded scales
│   └── App.jsx            # Main React app shell
├── /output/               # User-generated JSON scales (persistent)
├── /android/              # APK wrapper config (via Capacitor)
├── /README.md             # (This file)
└── vite.config.js         # Vite bundler setup
```

---

## Modular Loader System

Each module is a self-contained JavaScript file exporting a single generator function.

### Example module (e.g., `/src/modules/terrain.js`):
```js
export function generateTerrainScale(config) {
  // ...implementation...
  return {
    name: "terrain_scale_8_notes",
    base_frequency: config.baseFrequency,
    notes: [...]
  };
}
```

### Module manifest (`/src/data/modules.json`):
```json
[
  {
    "id": "terrain",
    "label": "Terrain Scale",
    "type": "generator",
    "entry": "../modules/terrain.js",
    "function": "generateTerrainScale"
  },
  {
    "id": "gap",
    "label": "Gap Scale",
    "type": "generator",
    "entry": "../modules/gap.js",
    "function": "generateGapScale"
  }
]
```

Modules are auto-loaded and attached to the front-end dropdowns at runtime. **No manual editing of `main` or app code is required.**

---

## App Features

- Modular **tool pop-ups** with real-time previews
- Scrollable and zoomable **multi-scale number line**
- Bottom **note tray** for collecting and combining notes
- **Playback engine** using Web Audio API
- Export any scale or tray as `.json`
- **Plugin-ready interface** for advanced tools and effects

---

## Packaging Options

- **PWA (Progressive Web App)**
  - One-click install on Android
  - Offline-capable
  - Native-like UI and splash screen
- **APK (Android)**
  - Wrap React frontend using **Capacitor.js**
  - Add native hooks if needed later (e.g. file system)

---

## Developer Guidelines

- All core scale logic should live in `/src/modules/` as ES modules.
- Add new tools by:
  1. Writing the JS module
  2. Updating `modules.json`
- Shared functions (prime generation, reduction, etc.) go in `/src/utils/`
- Always export scales to `/output/` so they can be viewed, played, or edited

---

## Roadmap Highlights

- [x] Migrate all core algorithms to JavaScript
- [x] Design final plugin loading system
- [x] Enable modular UI dropdowns
- [ ] Add metadata overlay for long-tap previews
- [ ] Build native APK shell via Capacitor.js
- [ ] Optional: GitHub-hosted web version for desktop testing

---

This document now serves as the **canonical reference** for the app's total architecture and frontend goals.
