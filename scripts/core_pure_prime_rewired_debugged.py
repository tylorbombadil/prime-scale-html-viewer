# ===[ CORE PURE PRIME SCALE - REWIRED TO MATCH GOLD SCHEMA ]===

import argparse
import math
import os
import json
from scripts.scale_utils import (
    generate_primes,
    get_log_positions,
    generate_density_axis,
    add_bounds,
    export_json
)

# ===[ MANIFESTO ]===
MANIFESTO = {
    "name": "core_pure_prime_rewired_debugged",
    "description": "Pure Prime Scale - Direct mapping of primes to log-pitch space with no filtering.",
    "type": "pure_prime",
    "version": "1.0",
    "schema": "v1_debug",
    "fields": ["prime_count", "base_frequency", "include_bounds", "density_resolution"]
}

# ===[ SCALE GENERATION FUNCTION ]===
def generate_scale(prime_count, base_frequency, include_bounds, density_resolution, mode):
    primes = generate_primes(prime_count)
    log_positions = get_log_positions(primes)
    _ = generate_density_axis(density_resolution)

    notes = []
    for log_pos in log_positions:
        freq = base_frequency * (2 ** log_pos)
        midi = round(69 + 12 * math.log2(freq / 440.0))
        notes.append({
            "log_position": log_pos,
            "frequency": freq,
            "midi": midi,
            "cents_from_base": 1200 * log_pos,
            "prime_sources": []
        })

    if include_bounds:
        notes = add_bounds(notes, base_frequency)

    metadata = {
        "prime_count": prime_count,
        "primes": primes,
        "log_positions": log_positions,
        "density_resolution": density_resolution
    }

    scale = {
        "name": f"pure_prime_scale_{prime_count}",
        "base_frequency": base_frequency,
        "mode": mode,
        "manifesto": MANIFESTO,
        "metadata": metadata,
        "notes": notes
    }

    return scale

# ===[ MAIN ENTRY ]===
def main():
    parser = argparse.ArgumentParser(description="Generate a Pure Prime Scale")
    parser.add_argument("--prime-count", type=int, required=True)
    parser.add_argument("--base-frequency", type=float, default=220.0)
    parser.add_argument("--bounds", action="store_true")
    parser.add_argument("--density-resolution", type=int, default=4000)
    parser.add_argument("--mode", type=str, default="default", help="Included for schema consistency")

    args = parser.parse_args()
    scale = generate_scale(
        prime_count=args.prime_count,
        base_frequency=args.base_frequency,
        include_bounds=args.bounds,
        density_resolution=args.density_resolution,
        mode=args.mode
    )

    output_name = f"pure_prime_{args.prime_count}_rewired.json"
    export_json(scale, output_name)

if __name__ == "__main__":
    main()
