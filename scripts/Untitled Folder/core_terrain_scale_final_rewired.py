# ===[ IMPORTS ]===
import argparse
import json
import math
import os
from scripts.scale_utils import generate_primes, reduce_value, gravitational_fade

# ===[ MAIN SCALE GENERATION ENGINE ]===
def generate_scale(prime_count, base_frequency, num_notes, window_size, density_resolution, mode, include_bounds=True):
    primes = generate_primes(prime_count)
    log_positions = [math.log2(reduce_value(p)) for p in primes]
    weights = [1 / p for p in primes]

    x_axis = [i / density_resolution for i in range(density_resolution)]
    density_map = []

    for x in x_axis:
        total_weight = 0
        for log_pos, weight in zip(log_positions, weights):
            distance = abs(log_pos - x)
            wrapped_distance = min(distance, 1 - distance)
            if wrapped_distance <= window_size / 2:
                focus = gravitational_fade(wrapped_distance, window_size)
                total_weight += weight * focus
        density_map.append(total_weight)

    segment_width = 1.0 / num_notes
    selected_notes = []

    for i in range(num_notes):
        segment_start = i * segment_width
        segment_end = segment_start + segment_width
        segment_range = [(x, d) for x, d in zip(x_axis, density_map) if segment_start <= x < segment_end]
        if segment_range:
            if mode == "valley":
                best_x, _ = min(segment_range, key=lambda t: t[1])
            elif mode == "peak":
                best_x, _ = max(segment_range, key=lambda t: t[1])
            else:
                raise ValueError("Invalid mode. Use 'valley' or 'peak'.")
            selected_notes.append(best_x)

    if include_bounds:
        selected_notes.insert(0, 0.0)
        selected_notes.append(1.0)

    notes_data = []
    for log_pos in selected_notes:
        frequency = base_frequency * (2 ** log_pos)
        midi_note = round(69 + 12 * math.log2(frequency / 440.0))
        cents = 1200 * log_pos
        nearby_primes = [p for p, lp in zip(primes, log_positions)
                         if min(abs(lp - log_pos), 1 - abs(lp - log_pos)) <= window_size / 2]
        notes_data.append({
            "log_position": log_pos,
            "frequency": frequency,
            "midi": midi_note,
            "cents_from_base": cents,
            "prime_sources": nearby_primes
        })

    metadata = {
        "prime_count": len(primes),
        "primes": primes,
        "log_prime_positions": log_positions,
        "linear_prime_positions": [reduce_value(p) for p in primes],
        "x_axis": x_axis,
        "density_map": density_map,
        "algorithm_manifest": {
            "name": "core_terrain_scale_final",
            "mode": mode,
            "window_size": window_size,
            "lens_profile": "gravitational"
        }
    }

    scale_data = {
        "name": f"terrain_scale_{num_notes}_{mode}",
        "base_frequency": base_frequency,
        "notes": notes_data,
        "metadata": metadata
    }

    filename = os.path.expanduser(f"~/prime-scale-html-viewer/output/terrain_scale_{num_notes}_{mode}.json")
    with open(filename, "w") as f:
        json.dump(scale_data, f, indent=2)

    print(f"✔ Scale saved to {os.path.abspath(filename)}")

# ===[ CLI ENTRY POINT ]===
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a terrain-based scale using reduced primes and density mapping.")
    parser.add_argument("--prime-count", type=int, default=1000)
    parser.add_argument("--base-frequency", type=float, default=220.0)
    parser.add_argument("--num-notes", type=int, default=8)
    parser.add_argument("--window-size", type=float, default=0.007)
    parser.add_argument("--density-resolution", type=int, default=4000)
    parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
    parser.add_argument("--include-bounds", action="store_true", default=False, help="Include base frequency and its octave as bounds")

    args = parser.parse_args()
    generate_scale(
        prime_count=args.prime_count,
        base_frequency=args.base_frequency,
        num_notes=args.num_notes,
        window_size=args.window_size,
        density_resolution=args.density_resolution,
        mode=args.mode,
        include_bounds=args.include_bounds
    )
