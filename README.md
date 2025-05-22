# Prime Scale App Sandbox

## The Purpose of This Sandbox

This sandbox exists for **one reason**:

> To transition the original Python core algorithm scripts into structured schema-based modules that will be converted into JavaScript for use in the Prime Scale App Android APK.

These Python scripts form the **mathematical and conceptual core** of the Prime Scale App. They are the foundation, the reference, and the holy grail. But they were not originally written to scale or adapt easily across platforms. This sandbox gives us the place to carefully restructure them.

The final goal is to translate these schema-based Python modules into **JavaScript modules** that will power the **Prime Scale App APK**, which is built using **Java and other mobile-friendly dependencies**.

---

## The Schema Convention (Key Concept)

The file `core_terrain_scale_final_rewired_debug.py` is the official schema prototype.

All other algorithms must eventually adopt its structure, either by:

1. Morphing legacy scripts directly into schema-compatible Python versions,  
2. Or porting them to JavaScript while following this schema’s logic and conventions.

### Key Features of the Schema Convention

- Modular Imports from `scale_utils.py`
- Structured Metadata:
  - Prime list
  - Log positions
  - Regular (non-log) positions
  - Sampling access resolution
  - Total prime count
- Top-Level Notes with frequency, log position, MIDI estimate
- CLI Arguments: base frequency, resolution, bounds, etc.
- Embedded Manifesto: self-documents the algorithm type and structure

```text
scripts/
├── core_terrain_scale_final_rewired_debug.py   <- Schema GOLD STANDARD
├── scale_utils.py                              <- Shared utilities
├── update_manifest.py                          <- Refreshes manifest for viewer
```

---

## How to Use the Sandbox

### 1. Generate a Scale
From the root directory, run:
```bash
python3 -m scripts.core_terrain_scale_final_rewired_debug \
  --prime-count 1000 \
  --base-frequency 220 \
  --num-notes 8 \
  --window-size 0.007 \
  --density-resolution 4000 \
  --mode valley \
  --bounds
```

> Important: Use class-style entry like `scripts.filename`. Always run from the top-level folder.

---

### 2. Update the Manifest
```bash
python3 -m scripts.update_manifest
```
This regenerates the list of available scale files for the viewer.

---

## Using the Sandbox Viewer

This repo includes a basic HTML+JS viewer to display scale output.

### Features:
- Tall gray lines = full prime field  
- Black dots = selected notes  
- Dropdown to load any scale  
- Button list for tone preview

### Run the Viewer
```bash
python3 -m http.server 8080
```
Then go to:
```
http://localhost:8080
```

### Folder Overview
```
project-root/
├── scripts/            # Algorithm logic
├── output/             # .json scale files + manifest
├── viewer.js           # Viewer logic
├── index.html          # Viewer UI
```

---

## Final Note to Developers

This is a prototype workspace for refactoring and converting the core algorithms.

Stick to the schema! The better these modules conform, the easier it will be to translate them into JS and Java for the final Prime Scale App APK.

Refer to the `core_terrain_scale_final_rewired_debug.py` script as your guide.

Your mission: preserve the mathematical essence, refactor into schema, and get us one step closer to a fully musical APK.
