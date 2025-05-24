# Prime Scale App – CLI Entry Point (main.py)

This file defines the command-line interface (CLI) for running scale generation modules.

---

## Purpose

Acts as the command-line gateway that routes user input to the appropriate scale generator module (`terrain`, `gap`, or `pure`).

---

## CLI Argument Schema

Each scale type expects a specific set of arguments.

### `terrain` scale
- `--prime-count`: Number of primes
- `--base-frequency`: Starting frequency in Hz
- `--num-notes`: Number of notes to extract
- `--window-size`: Width of prime influence lens
- `--density-resolution`: Axis granularity
- `--mode`: `"valley"` or `"peak"`
- `--include-bounds` / `--no-include-bounds`
- `--weight-curve`: Influence strength falloff

### `gap` scale
- `--prime-count`: Number of primes
- `--base-frequency`: Starting frequency in Hz
- `--threshold-range MIN MAX`: Min/max gap size
- `--step-size`: Granularity of gap search
- `--note-goal`: Desired number of notes
- `--tolerance`: Allowed deviation from goal
- `--density-resolution`: Axis granularity
- `--include-bounds` / `--no-include-bounds`

### `pure` scale
- `--prime-count`: Number of primes
- `--base-frequency`: Starting frequency in Hz
- `--density-resolution`: Axis granularity
- `--include-bounds` / `--no-include-bounds`

---

## Functional Responsibilities

- Parses all CLI arguments using `argparse`
- Routes to the correct function based on `--scale-type`
- Forwards all relevant config to the chosen generator

---

## Contract Enforcement

Each algorithm module must implement a function matching its expected argument signature (e.g., `generate_terrain_scale(...)`).

This is a soft interface contract implied by CLI routing logic.
