
# ===[ IMPORTS & CONSTANTS ]===
import argparse
import json
import math
import os

# ===[ PRIME UTILITIES ]===
def generate_primes(n):
    primes = [2]
    candidate = 3
    while len(primes) < n:
        is_prime = True
        for p in primes:
            if candidate % p == 0:
                is_prime = False
                break
            if p * p > candidate:
                break
        if is_prime:
            primes.append(candidate)
        candidate += 2
    return primes

def reduce_value(val):
    while val >= 2:
        val /= 2
    while val < 1:
        val *= 2
    return val

# ===[ DENSITY LENS PROFILE ]===
def gravitational_fade(d, w, n=2.5):
    relative = d / (w / 2)
    return 1 / (1 + (relative ** n))

# ===[ MAIN SCALE GENERATION ENGINE ]===
def generate_scale(prime_count, base_frequency, num_notes, window_size, density_resolution, mode):
    primes = generate_primes(prime_count)
    print(f"✔ Generated {len(primes)} primes")

    log_positions = [math.log2(reduce_value(p)) for p in primes]
    weights = [1 / p for p in primes]
    print("✔ Prepared log positions and reciprocal weights")

    x_axis = [i / density_resolution for i in range(density_resolution)]
    density_map = []

    for i, x in enumerate(x_axis):
        if i % (density_resolution // 10) == 0:
            print(f"  > Density progress: {int(i / density_resolution * 100)}%")
        total_weight = 0
        for log_pos, weight in zip(log_positions, weights):
            distance = abs(log_pos - x)
            wrapped_distance = min(distance, 1 - distance)
            if wrapped_distance <= window_size / 2:
                focus = gravitational_fade(wrapped_distance, window_size)
                total_weight += weight * focus
        density_map.append(total_weight)
    print("✔ Completed density mapping")

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

            frequency = base_frequency * (2 ** best_x)
            midi_note = round(69 + 12 * math.log2(frequency / 440.0))
            cents = 1200 * best_x

            selected_notes.append({
                "log_position": best_x,
                "frequency": frequency,
                "midi": midi_note,
                "cents_from_base": cents,
                "prime_sources": []
            })
    print("✔ Selected all notes and generating output file...")

    # Prepare extended metadata
    metadata = {
        "primes": primes,
        "prime_count": len(primes),
        "linear_prime_positions": [reduce_value(p) for p in primes],
        "log_prime_positions": log_positions,
        "x_axis": x_axis,
        "density_map": density_map,
        "algorithm_manifest": {
            "name": "core_terrain_scale",
            "mode": mode,
            "window_size": window_size,
            "lens_profile": "gravitational"
        }
    }

    scale_data = {
        "metadata": metadata,
        "name": f"terrain_scale_{num_notes}_{mode}",
        "base_frequency": base_frequency,
        "notes": selected_notes
    }

    filename = os.path.expanduser(f"~/prime-scale-html-viewer/output/terrain_scale_{num_notes}_{mode}.json")
    with open(filename, "w") as f:
        json.dump(scale_data, f, indent=2)

    print(f"✔ Scale saved to {os.path.abspath(filename)}")

# ===[ COMMAND LINE ENTRY ]===
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a musical scale from prime terrain.")
    parser.add_argument("--prime-count", type=int, default=1000)
    parser.add_argument("--base-frequency", type=float, default=220.0)
    parser.add_argument("--num-notes", type=int, default=8)
    parser.add_argument("--window-size", type=float, default=0.007)
    parser.add_argument("--density-resolution", type=int, default=4000)
    parser.add_argument("--mode", choices=["valley", "peak"], default="valley")

    args = parser.parse_args()
    generate_scale(
        prime_count=args.prime_count,
        base_frequency=args.base_frequency,
        num_notes=args.num_notes,
        window_size=args.window_size,
        density_resolution=args.density_resolution,
        mode=args.mode
    )
