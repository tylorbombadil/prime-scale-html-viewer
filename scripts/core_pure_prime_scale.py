# ===[ IMPORTS ]===
import argparse
import os
import json
import math

# Shared utility functions
from scripts.scale_utils import (
    generate_primes,
    reduce_value,
    get_log_positions,
    generate_density_axis,
    add_bounds,
    export_json
)

# ===[ MAIN SCALE GENERATION FUNCTION ]===
def generate_scale(prime_count, base_frequency, density_resolution, include_bounds):
    # Step 1: Generate primes and get their log2 positions
    primes = generate_primes(prime_count)
    log_positions = get_log_positions(primes)

    # Step 2: Generate density axis (not used directly but retained for visual analysis)
    x_axis = generate_density_axis(density_resolution)

    # Step 3: Optionally include bounds (0.0 and 1.0)
    if include_bounds:
        log_positions = add_bounds(log_positions, base_frequency)

    # Step 4: Convert positions into full note objects
    notes = []
    for x in log_positions:
        freq = base_frequency * (2 ** x)
        midi = round(69 + 12 * math.log2(freq / 440.0))
        cents = round(1200 * x, 2)
        notes.append({
            "log_position": x,
            "frequency": round(freq, 3),
            "midi": midi,
            "cents_from_base": cents,
            "prime_sources": []  # Empty since no mapping to individual primes here
        })

    # Step 5: Construct metadata and scale data
    metadata = {
        "prime_count": len(primes),
        "primes": primes,
        "log_prime_positions": log_positions,
        "x_axis": x_axis,
        "algorithm_manifest": {
            "name": "pure_prime_scale",
            "description": "Unfiltered prime positions mapped directly to pitch space"
        }
    }

    scale_data = {
        "name": f"pure_prime_scale_{prime_count}_primes",
        "base_frequency": base_frequency,
        "notes": notes,
        "log_positions": log_positions,
        "metadata": metadata
    }

    # Step 6: Export to JSON
    output_path = os.path.expanduser(f"~/prime-scale-html-viewer/output/pure_prime_scale_{prime_count}_primes.json")
    with open(output_path, "w") as f:
        json.dump(scale_data, f, indent=2)

    print(f"✔ Scale saved to {os.path.abspath(output_path)}")

    return notes, metadata

# ===[ ENTRY POINT ]===
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a pure prime scale using raw primes mapped directly to pitch space.")
    parser.add_argument("--prime-count", type=int, default=1000)
    parser.add_argument("--base-frequency", type=float, default=220.0)
    parser.add_argument("--density-resolution", type=int, default=4000)
    parser.add_argument("--include-bounds", action="store_true", default=False)

    args = parser.parse_args()

    generate_scale(
        prime_count=args.prime_count,
        base_frequency=args.base_frequency,
        density_resolution=args.density_resolution,
        include_bounds=args.include_bounds
    )
