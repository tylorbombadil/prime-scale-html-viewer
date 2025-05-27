# ===[ IMPORTS ]===
from collections import OrderedDict
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

    reduced_primes = [reduce_value(p) for p in primes] #generate reduced primes for metadata

# ===[Metadata, Scale data, and Algorithm Manifest]===
    parameters = OrderedDict()

    manifest= OrderedDict() 
    manifest["name"] = "pure_prime_scale"
    manifest["description"] = "Unfiltered prime positions mapped directly to pitch space"
    manifest["notes"] = prime_count
    manifest["include_bounds"] = include_bounds
    manifest["parameters"] = parameters
   
    metadata = OrderedDict()
    metadata["algorithm_manifest"] = manifest
    metadata["prime_count"] = len(primes)
    metadata["primes"] = primes
    # metadata["segment_boundaries"] = [i / num_notes for i in range(num_notes + 1)]
    metadata["log_prime_positions"] = log_positions
    metadata["linear_prime_positions"] = reduced_primes
    metadata["x_axis"] = x_axis
    metadata["density_resolution"] = density_resolution
    # metadata["density_map"] = density_map
   
    scale_data = OrderedDict()
    scale_data["name"] = f"pure_prime_scale_{prime_count}_primes"
    scale_data["base_frequency"] = base_frequency
    scale_data["notes"] = notes
    scale_data["log_positions"] = log_positions
    scale_data["metadata"] = metadata
    

    # Step 6: Export to JSON
    filename = None
    export_json(scale_data, filename)

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
