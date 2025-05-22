
import argparse
import math
from scripts.scale_utils import (
    generate_primes,
    get_log_positions,
    prime_weight,
    circular_distance,
    generate_density_axis,
    add_bounds,
    export_json
)

# Terrain-specific smoothing function
def gravitational_fade(d, w, n=2.5):
    relative = d / (w / 2)
    return 1 / (1 + (relative ** n))

# Generate density map across log2-reduced space
def generate_density_map(log_positions, weights, resolution, window_size):
    x_axis = generate_density_axis(resolution)
    density_map = []

    for x in x_axis:
        total_weight = 0
        for log_pos, weight in zip(log_positions, weights):
            distance = circular_distance(log_pos, x)
            if distance <= window_size / 2:
                focus = gravitational_fade(distance, window_size)
                total_weight += weight * focus
        density_map.append(total_weight)

    return x_axis, density_map

# Segment and select notes from density map
def select_notes_from_density(x_axis, density_map, num_notes, base_frequency, mode):
    segment_width = 1.0 / num_notes
    selected_notes = []

    for i in range(num_notes):
        segment_start = i * segment_width
        segment_end = segment_start + segment_width
        segment_range = [(x, d) for x, d in zip(x_axis, density_map) if segment_start <= x < segment_end]

        if segment_range:
            best_x, _ = min(segment_range, key=lambda t: t[1]) if mode == "valley" else max(segment_range, key=lambda t: t[1])
            freq = base_frequency * (2 ** best_x)
            selected_notes.append({
                "log_position": best_x,
                "frequency": freq,
                "midi": round(69 + 12 * math.log2(freq / 440.0)),
                "cents_from_base": 1200 * best_x,
                "prime_sources": []
            })

    return selected_notes

# Full generator function
def generate_terrain_scale(prime_count, base_frequency, num_notes, window_size, density_resolution, mode, include_bounds=True, weight_curve=1.0):
    primes = generate_primes(prime_count)
    log_positions = get_log_positions(primes)
    weights = [prime_weight(p, weight_curve) for p in primes]

    x_axis, density_map = generate_density_map(log_positions, weights, density_resolution, window_size)
    selected_notes = select_notes_from_density(x_axis, density_map, num_notes, base_frequency, mode)

    if include_bounds:
        selected_notes = add_bounds(selected_notes, base_frequency)

    scale_data = {
        "name": f"terrain_scale_{num_notes}_{mode}",
        "base_frequency": base_frequency,
        "notes": selected_notes,
        "log_prime_positions": log_positions,
        "segment_boundaries": [i / num_notes for i in range(num_notes + 1)]
    }

    filename = f"output/terrain_scale_{num_notes}_{mode}.json"
    export_json(scale_data, filename)

# CLI runner
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime-count", type=int, default=1000)
    parser.add_argument("--base-frequency", type=float, default=220.0)
    parser.add_argument("--num-notes", type=int, default=8)
    parser.add_argument("--window-size", type=float, default=0.007)
    parser.add_argument("--density-resolution", type=int, default=4000)
    parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
    parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
    parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
    parser.add_argument("--weight-curve", type=float, default=1.0)
    parser.set_defaults(include_bounds=True)

    args = parser.parse_args()

    generate_terrain_scale(
        prime_count=args.prime_count,
        base_frequency=args.base_frequency,
        num_notes=args.num_notes,
        window_size=args.window_size,
        density_resolution=args.density_resolution,
        mode=args.mode,
        include_bounds=args.include_bounds,
        weight_curve=args.weight_curve
    )
