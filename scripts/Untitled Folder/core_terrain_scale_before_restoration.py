# ===[ IMPORTS ]===
from collections import OrderedDict
import argparse
import os
import json
import math

# Shared utility functions
from scripts.scale_utils import(
    generate_primes,
    reduce_value,
    get_log_positions,
    generate_density_axis,
    add_bounds,
    export_json,
    circular_distance,
    prime_weight
)

# ===[ TERRAIN-SPECIFIC FUNCTION ]===
# This fade function simulates gravitational pull — stronger at the center of the lens.
def gravitational_fade(distance, width, power=2.5):
    relative = distance / (width / 2)
    return 1 / (1 + (relative ** power))

# ===[ MAIN SCALE GENERATION FUNCTION ]===
def generate_scale(prime_count, base_frequency, num_notes, window_size, density_resolution, mode, include_bounds, dial_value):
    # Step 1: Generate primes and reduce them to fall within one octave
    primes = generate_primes(prime_count)
    reduced_primes = [reduce_value(p) for p in primes]
    log_positions = get_log_positions(reduced_primes)

    # Step 2: Create the sampling axis (granular points across [0, 1])
    x_axis = generate_density_axis(density_resolution)

    # Step 3: Build a weighted density map across the axis
    density_map = []
    for x in x_axis:
        total_weight = 0
        for log_pos, prime in zip(log_positions, primes):
            weight = prime_weight(prime, dial_value) # Inverse of the prime for its influence
            distance = abs(log_pos - x)
            wrapped_distance = min(distance, 1 - distance)  # Handle octave wrapping
            if wrapped_distance <= window_size / 2:
                total_weight += weight * gravitational_fade(wrapped_distance, window_size)
        density_map.append(total_weight)

    # Step 4: Split axis into even segments and pick a representative from each
    segment_width = 1.0 / num_notes
    sweep_width = window_size
    selected_notes = []

    for i in range(num_notes):
        center = (i + 0.5) * segment_width
        segment_range = [
            (x, d) for x, d in zip(x_axis, density_map)
            if min(abs(center - x), 1 - abs(center - x)) <= sweep_width / 2
    ]
        if segment_range:
            best_x = min(segment_range, key=lambda t: t[1])[0] if mode == "valley" else max(segment_range, key=lambda t: t[1])[0]
            selected_notes.append(best_x)

    # Step 5: Optionally include lower and upper bounds (0.0 and 1.0)
    if include_bounds:
        selected_notes = add_bounds(selected_notes, base_frequency)

    # Step 6: Package note data and export to JSON
    notes = []
    for x in selected_notes:
        freq = base_frequency * (2 ** x)
        midi = round(69 + 12 * math.log2(freq / 440.0))
        cents = round(1200 * x, 2)
        notes.append({
            "log_position": x,
            "frequency": round(freq, 3),
            "midi": midi,
            "cents_from_base": cents
        })

# ===[Metadata, Scale data, and Algorithm Manifest]===
    parameters = OrderedDict()
    parameters["window_size"] = window_size
    parameters["lens_profile"] = "gravitational"
    parameters["mode"] = mode

    manifest= OrderedDict()
    manifest["name"] = "terrain_scale"   
    manifest["description"] = "sampling of prime density-peak and valley mode with other variable fields"
    manifest["notes"] = num_notes
    manifest["include_bounds"] = include_bounds
    manifest["parameters"] = parameters

    metadata = OrderedDict()
    metadata["algorithm_manifest"] = manifest
    metadata["prime_count"] =  len(primes)
    metadata["primes"] = primes
    metadata["segment_boundaries"] = [i / num_notes for i in range(num_notes + 1)]
    metadata["log_prime_positions"] = log_positions
    metadata["linear_prime_positions"] = reduced_primes
    metadata["x_axis"] = x_axis
    metadata["density_resolution"] = density_resolution
    metadata["density_map"] = density_map

    scale_data = OrderedDict()
    scale_data["name"] = f"terrain_scale_{num_notes}_{mode}"
    scale_data["base_frequency"] = base_frequency
    scale_data["notes"] = notes
    scale_data["log_positions"] = log_positions, 
    scale_data["metadata"] = metadata

    filename = None
    export_json(scale_data, filename)

    return notes, metadata

# ===[ ENTRY POINT ]===
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a terrain-based prime scale using full shared utility set.")
    parser.add_argument("--prime-count", type=int, default=1000)
    parser.add_argument("--base-frequency", type=float, default=220.0)
    parser.add_argument("--num-notes", type=int, default=8)
    parser.add_argument("--window-size", type=float, default=0.007)
    parser.add_argument("--density-resolution", type=int, default=4000)
    parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
    parser.add_argument("--include-bounds", action="store_true", default=False)
    parser.add_argument("--dial-value", type=float, required=False, default=0.0, help="Analog contrast control (-1.0 to +1.0)")

    args = parser.parse_args()
    generate_scale(
        prime_count=args.prime_count,
        base_frequency=args.base_frequency,
        num_notes=args.num_notes,
        window_size=args.window_size,
        density_resolution=args.density_resolution,
        mode=args.mode,
        include_bounds=args.include_bounds,
        dial_value=args.dial_value
    )
