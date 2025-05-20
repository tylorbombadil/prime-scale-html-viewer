import argparse
import math
from scripts.scale_utils import (
    generate_primes,
    get_log_positions,
    add_bounds,
    export_json,
    generate_density_axis  # included for compatibility or plotting if needed
)

# Count qualifying gaps for a given threshold
def detect_gap_count(log_positions, threshold):
    log_positions.sort()
    gap_centers = []

    for i in range(len(log_positions) - 1):
        gap = log_positions[i + 1] - log_positions[i]
        if gap >= threshold:
            center_log = (log_positions[i] + log_positions[i + 1]) / 2
            gap_centers.append(center_log)

    return gap_centers

# Scan thresholds to find ones that match note goal
def scan_thresholds(prime_count, threshold_min, threshold_max, step_size, note_goal, tolerance, base_frequency, include_bounds, density_resolution):
    primes = generate_primes(prime_count)
    log_positions = get_log_positions(primes)
    matches = []

    # Optional: could use this for visual overlays or precision matching later
    _ = generate_density_axis(density_resolution)

    current = threshold_min
    while current <= threshold_max:
        gap_centers = detect_gap_count(log_positions, current)
        count = len(gap_centers)

        if abs(count - note_goal) <= tolerance:
            print(f"✔ Match: {count} notes at threshold {current:.6f}")
            matches.append((current, count, gap_centers))
        else:
            print(f"... Skipped: {count} notes at threshold {current:.6f}")

        current = round(current + step_size, 10)  # Avoid float rounding errors

    if matches:
        best_thresh, best_count, best_centers = matches[0]
        notes = []
        for log_pos in best_centers:
            freq = base_frequency * (2 ** log_pos)
            notes.append({
                "log_position": log_pos,
                "frequency": freq,
                "midi": round(69 + 12 * math.log2(freq / 440.0)),
                "cents_from_base": 1200 * log_pos,
                "prime_sources": []
            })

        if include_bounds:
            notes = add_bounds(notes, base_frequency)

        scale_data = {
            "name": f"gap_scout_match_{best_count}_notes",
            "base_frequency": base_frequency,
            "notes": notes
        }

        export_json(scale_data, f"gap_scout_match_{best_count}_notes.json")
    else:
        print("No matching thresholds found within specified range.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-count", type=int, required=True)
    parser.add_argument("--base-frequency", type=float, default=220.0)
    parser.add_argument("--threshold-range", nargs=2, type=float, required=True, metavar=("MIN", "MAX"))
    parser.add_argument("--step-size", type=float, default=0.001)
    parser.add_argument("--note-goal", type=int, required=True)
    parser.add_argument("--tolerance", type=int, default=1)
    parser.add_argument("--density-resolution", type=int, default=4000)
    parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
    parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
    parser.set_defaults(include_bounds=True)

    args = parser.parse_args()

    scan_thresholds(
        prime_count=args.prime_count,
        threshold_min=args.threshold_range[0],
        threshold_max=args.threshold_range[1],
        step_size=args.step_size,
        note_goal=args.note_goal,
        tolerance=args.tolerance,
        base_frequency=args.base_frequency,
        include_bounds=args.include_bounds,
        density_resolution=args.density_resolution
    )
