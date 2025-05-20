import argparse
import math
from scripts.scale_utils import (
    generate_primes,
    get_log_positions,
    add_bounds,
    export_json,
    generate_density_axis  # included for compatibility and visualization
)

def generate_pure_prime_scale(prime_count, base_frequency, include_bounds=True, density_resolution=4000):
    primes = generate_primes(prime_count)
    log_positions = get_log_positions(primes)

    # Optional: generate axis for any future visualization
    _ = generate_density_axis(density_resolution)

    notes = []
    for log_pos in log_positions:
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
        "name": f"pure_prime_scale_{prime_count}_primes",
        "base_frequency": base_frequency,
        "notes": notes
    }

    export_json(scale_data, f"pure_prime_scale_{prime_count}_primes.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
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
