Prime Scale App – Modular Rewrite (In Progress)

## Purpose
This README documents the ongoing modular refactor of the Prime Scale App. Its goal is to offer a clean, scalable, and extensible architecture that supports multiple scale-generation algorithms and prepares the codebase for future CLI, GUI, and web-based interfaces.

---

## Project Goals
- Modular core scale types
- Reusable utilities for primes, reduction, weighting, and export
- CLI interface to choose and configure scale types
- Future-ready for GUI or Web front-end

---

## Directory Structure (Target)
```
/prime-scale-app/
├── scripts/
│   ├── core_terrain_scale.py              # Terrain-based density generator
│   ├── core_gap_scale.py                  # Gap-based note detection (WIP)
│   ├── core_pure_prime_scale.py           # Raw prime tone sequence
│   ├── core_cluster_scale.py              # Density-based cluster detection (WIP)
│   ├── scale_utils.py                     # Shared utilities and exports
│   ├── main.py                            # CLI entry point (planned)
│   └── __init__.py                        # Package init
├── output/                                # Generated scale .json files
├── interface/                             # Optional HTML or GUI code
├── README.md                              # Legacy reference
├── nextgen_README.md                      # This file – active documentation
```

---

## Shared Utilities (`scale_utils.py`)
Implements common functionality:
- `generate_primes(n)`
- `reduce_value(val)`
- `get_log_positions(primes)`
- `generate_density_axis(resolution)`
- `circular_distance(a, b)`
- `prime_weight(p, curve)`
- `add_bounds(notes, base_freq)` – Adds base and octave markers
- `export_json(scale_data, filename)` – Saves output to `/output/`

Note: `density_resolution` is included in many modules for future plotting/visualization but may currently be unused. Commented accordingly.

---

## Scale Types

### 1. Terrain-Based Scale (`core_terrain_scale.py`)
Generates a weighted density map of reduced primes, tiles the log2 octave, and selects either valleys or peaks within segments.
- Uses gravity-style smoothing for density fade
- Fully implemented CLI interface

**Arguments**: `--prime-count`, `--base-frequency`, `--num-notes`, `--window-size`, `--density-resolution`, `--mode` (valley/peak), `--include-bounds`, `--weight-curve`

### 2. Gap-Based Scale (`gap_threshold_scout.py`)
Scans through gap thresholds between log-reduced primes, selecting gaps that match a target note count.
- Outputs matching scales to JSON
- CLI runner implemented

**Arguments**: `--threshold-range`, `--note-goal`, `--tolerance`, `--step-size`, `--prime-count`, `--base-frequency`, `--include-bounds`

Note: `density_resolution` is currently unused (commented).

### 3. Pure Prime Scale (`core_pure_prime.py`)
Maps raw reduced primes into pitch space with no filtering.
- Simplest generator, clean reference

**Arguments**: `--prime-count`, `--base-frequency`, `--include-bounds`, `--density-resolution` *(commented if unused)*

### 4. Cluster Scale (WIP)
Combines:
- `binary_gap_analyzer.py`: Computes binary-segment gaps from reduced primes
- `cluster_finder.py`: Identifies sparse clusters by filtering gap counts

**Current output is CLI print only – no JSON export yet.**

**Next Steps**:
- Convert clusters into scale notes
- Integrate export using `scale_utils.py`
- Add CLI wrapper for standalone cluster scale

---

## Planned CLI Interface (`main.py`)
Single unified entry point to route commands to different generators.

**Examples:**
```sh
python main.py \
  --scale-type gap \
  --prime-count 2000 \
  --base-frequency 220.0 \
  --gap-threshold 0.012 \
  --sort-by pitch \
  --include-bounds

python main.py \
  --scale-type pure \
  --prime-count 128 \
  --base-frequency 220.0 \
  --order pitch

python main.py \
  --scale-type cluster \
  --prime-count 3000 \
  --base-frequency 220.0 \
  --cluster-sensitivity 0.85 \
  --sort-by strength
```

---

## Transition Checklist

### Core Modules:
- [x] `scale_utils.py` created and shared across all scripts
- [x] `core_terrain_scale.py` refactored and validated
- [x] `gap_threshold_scout.py` implemented and debugged
- [x] `core_pure_prime.py` implemented
- [ ] `core_cluster_scale.py` to be completed (cluster → note export + CLI)

### CLI Integration:
- [ ] Create `main.py` driver with `argparse` routing to each core
- [ ] Define scale types and attach to handlers in `main.py`
- [ ] Add validation and unified `--help` messaging

### Output & Interface:
- [x] Centralized all JSON exports to `/output/`
- [ ] GUI or HTML playback (optional – future scope)

---

## Notes
- All scripts use `include_bounds` to optionally add octave anchors.
- `density_resolution` is present in several modules for consistency, even if not currently used.
- This file replaces the legacy `README.md` as the living source of documentation.
- Future additions (e.g. scale metadata, UI metadata flags, performance tweaks) will be tracked here.

---

## Dev Guidance
- Comment out unused arguments (like `density_resolution`) but leave them in place for consistency.
- Use `scale_utils.py` exclusively for shared logic.
- Avoid duplicating export or reduction code in core modules.
- Add CLI wrappers to all future modules.

---

Let this README grow with the system – all additions should be documented here as they stabilize.

**Next priority: Finish cluster → note export + `main.py` CLI router.**
