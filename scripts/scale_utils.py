import math
import json
import os

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

def get_log_positions(primes):
    """Return log2 positions of primes reduced to the 1–2 octave range."""
    return [math.log2(reduce_value(p)) for p in primes]

def generate_density_axis(resolution):
    """Returns evenly spaced samples from 0 to 1 (not inclusive) for log-space rendering."""
    return [i / resolution for i in range(resolution)]

def circular_distance(a, b):
    return min(abs(a - b), 1 - abs(a - b))

def prime_weight(p, curve=1.0):
    if curve == 0.0:
        return 1.0
    return 1 / (p ** curve)

def add_bounds(notes, base_freq):
    bounds = [
        {
            "log_position": 0.0,
            "frequency": base_freq,
            "midi": round(69 + 12 * math.log2(base_freq / 440.0)),
            "cents_from_base": 0.0,
            "prime_sources": []
        },
        {
            "log_position": 1.0,
            "frequency": base_freq * 2,
            "midi": round(69 + 12 * math.log2((base_freq * 2) / 440.0)),
            "cents_from_base": 1200.0,
            "prime_sources": []
        }
    ]
    return [0.0] + notes + [1.0]

def export_json(scale_data, filename):
    # Always write to top-level /output/ folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    output_dir = os.path.join(project_root, "output")

    os.makedirs(output_dir, exist_ok=True)
    full_path = os.path.join(output_dir, os.path.basename(filename))

    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(scale_data, f, indent=2)

    print(f"✔ Saved scale to {full_path}")
