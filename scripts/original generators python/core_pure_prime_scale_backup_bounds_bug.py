import argparse
import math
import os
print("CWD:", os.getcwd())
from scripts.scale_utils import (
    generate_primes,
    get_log_positions,
    add_bounds,
    export_json,
    generate_density_axis
)

def generate_pure_prime_scale(prime_count, base_frequency, include_bounds=True, density_resolution=4000):
    # Step 1: Generate prime numbers
    primes = generate_primes(prime_count)

    # Step 2: Reduce and map primes to log2 positions
    log_positions = get_log_positions(primes)

    # Step 3: Optional density axis (for visual harmony)
    _ = generate_density_axis(density_resolution)

    # Step 4: Convert log positions to notes
    notes = []
    for log_pos in log_positions:
        freq = base_frequency * (2 ** log_pos)
        midi = round(69 + 12 * math.log2(freq / 440.0))
        cents = round(1200 * log_pos, 2)
        notes.append({
            "log_position": log_pos,
            "frequency": round(freq, 3),
            "midi": midi,
            "cents_from_base": cents,
            "prime_sources": []
        })

    # Step 5: Optionally add 0.0 and 1.0 boundaries
    if include_bounds:
        notes = add_bounds(notes, base_frequency)

    # Step 6: Create metadata block
    metadata = {
        "prime_count": len(primes),
        "primes": primes,
        "log_prime_positions": log_positions,
        "algorithm_manifest": {
            "name": "pure_prime_scale",
            "description": "Unfiltered prime positions mapped directly to pitch space"
        }
    }

    # Step 7: Package and export
    scale_data = {
        "notes": notes,
        "metadata": metadata
    }

    export_json(scale_data, f"pure_prime_scale_{prime_count}_primes.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a scale from raw primes with no filtering.")
    parser.add_argument("--prime-count", type=int, required=True)
    parser.add_argument("--base-frequency", type=float, default=220.0)
    parser.add_argument("--density-resolution", type=int, default=4000)
    parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
    parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
    parser.set_defaults(include_bounds=True)

    args = parser.parse_args()

    generate_pure_prime_scale(
        prime_count=args.prime_count,
        base_frequency=args.base_frequency,
        include_bounds=args.include_bounds,
        density_resolution=args.density_resolution
    )
