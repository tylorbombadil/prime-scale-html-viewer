# Project Architecture Snapshot

## Directory Tree

**.** _(Full Path: `/home/mint/prime-scale-html-viewer/scripts`)_

├── `__init__.py`
├── **__pycache__/**
│   ├── `__init__.cpython-310.pyc`
│   ├── `core_pure_prime_scale.cpython-310.pyc`
│   ├── `core_terrain_scale.cpython-310.pyc`
│   ├── `core_terrain_scale_final_rewired.cpython-310.pyc`
│   ├── `core_terrain_scale_modified.cpython-310.pyc`
│   ├── `core_terrain_scale_shared_axis.cpython-310.pyc`
│   ├── `gap_threshold_scout.cpython-310.pyc`
│   ├── `main.cpython-310.pyc`
│   └── `scale_utils.cpython-310.pyc`
├── `binary_gap_analyzer.py`
├── `cluster_finder.py`
├── `core_pure_prime_scale.py`
├── `core_terrain_scale.py`
├── `core_terrain_scale_final.py`
├── `core_terrain_scale_final_rewired.py`
├── `core_terrain_scale_modified.py`
├── `core_terrain_scale_shared_axis.py`
├── `gap_threshold_scout.py`
├── `main.py`
└── `scale_utils.py`

---

## Project Architecture Snapshot

**/home/mint/prime-scale-html-viewer/scripts**

        `__init__.py`
        ```py
        ```

        **__pycache__/**

        `binary_gap_analyzer.py`
        ```py
        import math
        
        def reduce_value(x):
            while x >= 2:
                x /= 2
            return x
        
        def generate_primes(n):
            primes = []
            candidate = 2
            while candidate <= n:
                is_prime = True
                for p in primes:
                    if p * p > candidate:
                        break
                    if candidate % p == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(candidate)
                candidate += 1
            return primes
        
        def compute_reduced_primes(tier):
            primes = generate_primes(tier)
            reduced = [reduce_value(p) for p in primes]
            return sorted(reduced), primes
        
        def compute_segment_gaps(reduced, tier):
            segment_width = 1 / (tier // 2)
            segments = []
            for i in range(len(reduced) - 1):
                start = reduced[i]
                end = reduced[i + 1]
                gap = end - start
                segment_count = round(gap / segment_width)
                segments.append((start, end, segment_count))
            return segments, segment_width
        ```

        `cluster_finder.py`
        ```py
        import argparse
        from scripts.binary_gap_analyzer import compute_reduced_primes, compute_segment_gaps
        import math
        
        def log_center(start, end):
            return math.sqrt(start * end)
        
        def find_clusters(segments, threshold=4):
            clusters = []
            current_cluster = []
            for start, end, count in segments:
                if count >= threshold:
                    if current_cluster:
                        clusters.append(current_cluster)
                        current_cluster = []
                else:
                    current_cluster.append((start, end))
            if current_cluster:
                clusters.append(current_cluster)
            return clusters
        
        def main():
            parser = argparse.ArgumentParser(description="Cluster Finder based on segment gaps.")
            parser.add_argument("--tier", type=int, required=True, help="Binary segmentation tier (must be power of two)")
            args = parser.parse_args()
        
            reduced, _ = compute_reduced_primes(args.tier)
            segment_data, segment_width = compute_segment_gaps(reduced, args.tier)
        
            clusters = find_clusters(segment_data)
        
            print(f"Tier: {args.tier} | Segment Width: {segment_width:.6f}")
            print(f"Found {len(clusters)} cluster(s):\n")
        
            for idx, cluster in enumerate(clusters):
                cluster_start = cluster[0][0]
                cluster_end = cluster[-1][1]
                center = log_center(cluster_start, cluster_end)
                print(f"Cluster {idx + 1}:")
                print(f"  Range: {cluster_start:.6f} -> {cluster_end:.6f}")
                print(f"  Log Center: {center:.6f}")
                print(f"  Members: {len(cluster)} segments\n")
        
        if __name__ == "__main__":
            main()
        ```

        `core_pure_prime_scale.py`
        ```py
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
        ```

        `core_terrain_scale.py`
        ```py
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
                "notes": selected_notes
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
        ```

        `core_terrain_scale_final.py`
        ```py
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
        ```

        `core_terrain_scale_final_rewired.py`
        ```py
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
        ```

        `core_terrain_scale_modified.py`
        ```py
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
        ```

        `core_terrain_scale_shared_axis.py`
        ```py
        # ===[ IMPORTS ]===
        import argparse
        import json
        import math
        import os
        
        # Shared utilities
        from scripts.scale_utils import (
            generate_primes,
            reduce_value,
            compute_log_positions,
            add_bounds,
            generate_sampling_axis
        )
        
        # ===[ LOCAL FUNCTION: Gravitational Falloff ]===
        def gravitational_fade(distance, width):
            return 1 / (1 + (distance / (width / 2)) ** 2)
        
        # ===[ MAIN FUNCTION ]===
        def generate_scale(prime_count, base_frequency, num_notes, window_size, density_resolution, mode, include_bounds=True):
            # Generate primes and reduce them
            primes = generate_primes(prime_count)
            reduced_primes = [reduce_value(p) for p in primes]
            log_positions = compute_log_positions(reduced_primes)
        
            # Generate the x-axis across one octave using shared utility
            x_axis = generate_sampling_axis(density_resolution)
            density_map = []
        
            for x in x_axis:
                total_weight = 0
                for log_pos, prime in zip(log_positions, primes):
                    weight = 1 / prime
                    distance = abs(log_pos - x)
                    wrapped_distance = min(distance, 1 - distance)
                    if wrapped_distance <= window_size / 2:
                        total_weight += weight * gravitational_fade(wrapped_distance, window_size)
                density_map.append(total_weight)
        
            segment_width = 1.0 / num_notes
            selected_notes = []
        
            for i in range(num_notes):
                segment_start = i * segment_width
                segment_end = segment_start + segment_width
                segment_range = [(x, d) for x, d in zip(x_axis, density_map) if segment_start <= x < segment_end]
                if segment_range:
                    best_x = min(segment_range, key=lambda t: t[1])[0] if mode == "valley" else max(segment_range, key=lambda t: t[1])[0]
                    selected_notes.append(best_x)
        
            if include_bounds:
                selected_notes = add_bounds(selected_notes)
        
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
                "linear_prime_positions": reduced_primes,
                "x_axis": x_axis,
                "density_map": density_map,
                "algorithm_manifest": {
                    "name": "core_terrain_scale_shared_axis",
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
        
        # ===[ CLI ENTRY ]===
        if __name__ == "__main__":
            parser = argparse.ArgumentParser(description="Generate a terrain-based prime scale using full shared utility set.")
            parser.add_argument("--prime-count", type=int, default=1000)
            parser.add_argument("--base-frequency", type=float, default=220.0)
            parser.add_argument("--num-notes", type=int, default=8)
            parser.add_argument("--window-size", type=float, default=0.007)
            parser.add_argument("--density-resolution", type=int, default=4000)
            parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
            parser.add_argument("--include-bounds", action="store_true", default=False)
        
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
        ```

        `gap_threshold_scout.py`
        ```py
        import argparse
        import math
        from scripts.scale_utils import (
            generate_primes,
            get_log_positions,
            add_bounds,
            export_json,
            generate_density_axis  # included for compatibility or plotting if needed
        )
        
        # Count qualifying gaps for a given threshold
        def detect_gap_count(log_positions, threshold):
            log_positions.sort()
            gap_centers = []
        
            for i in range(len(log_positions) - 1):
                gap = log_positions[i + 1] - log_positions[i]
                if gap >= threshold:
                    center_log = (log_positions[i] + log_positions[i + 1]) / 2
                    gap_centers.append(center_log)
        
            return gap_centers
        
        # Scan thresholds to find ones that match note goal
        def scan_thresholds(prime_count, threshold_min, threshold_max, step_size, note_goal, tolerance, base_frequency, include_bounds, density_resolution):
            primes = generate_primes(prime_count)
            log_positions = get_log_positions(primes)
            matches = []
        
            # Optional: could use this for visual overlays or precision matching later
            _ = generate_density_axis(density_resolution)
        
            current = threshold_min
            while current <= threshold_max:
                gap_centers = detect_gap_count(log_positions, current)
                count = len(gap_centers)
        
                if abs(count - note_goal) <= tolerance:
                    print(f"✔ Match: {count} notes at threshold {current:.6f}")
                    matches.append((current, count, gap_centers))
                else:
                    print(f"... Skipped: {count} notes at threshold {current:.6f}")
        
                current = round(current + step_size, 10)  # Avoid float rounding errors
        
            if matches:
                best_thresh, best_count, best_centers = matches[0]
                notes = []
                for log_pos in best_centers:
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
                    "name": f"gap_scout_match_{best_count}_notes",
                    "base_frequency": base_frequency,
                    "notes": notes
                }
        
                export_json(scale_data, f"gap_scout_match_{best_count}_notes.json")
            else:
                print("No matching thresholds found within specified range.")
        
        if __name__ == "__main__":
            parser = argparse.ArgumentParser()
            parser.add_argument("--prime-count", type=int, required=True)
            parser.add_argument("--base-frequency", type=float, default=220.0)
            parser.add_argument("--threshold-range", nargs=2, type=float, required=True, metavar=("MIN", "MAX"))
            parser.add_argument("--step-size", type=float, default=0.001)
            parser.add_argument("--note-goal", type=int, required=True)
            parser.add_argument("--tolerance", type=int, default=1)
            parser.add_argument("--density-resolution", type=int, default=4000)
            parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
            parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
            parser.set_defaults(include_bounds=True)
        
            args = parser.parse_args()
        
            scan_thresholds(
                prime_count=args.prime_count,
                threshold_min=args.threshold_range[0],
                threshold_max=args.threshold_range[1],
                step_size=args.step_size,
                note_goal=args.note_goal,
                tolerance=args.tolerance,
                base_frequency=args.base_frequency,
                include_bounds=args.include_bounds,
                density_resolution=args.density_resolution
            )
        ```

        `main.py`
        ```py
        """
        Prime Scale App – CLI Entry Point
        
        Usage (run from project root):
          python -m scripts.main --scale-type terrain ...
          python -m scripts.main --scale-type gap ...
          python -m scripts.main --scale-type pure ...
        """
        #comment hashes are used to toggle between different implementations
        import argparse
        #from scripts.core_terrain_scale import generate_terrain_scale
        from scripts.gap_threshold_scout import scan_thresholds
        from scripts.core_pure_prime_scale import generate_pure_prime_scale
        from scripts.core_terrain_scale_modified import generate_terrain_scale
        
        def main():
            parser = argparse.ArgumentParser(description="Prime Scale Generator CLI")
            subparsers = parser.add_subparsers(dest="scale_type", required=True, help="Scale type to generate")
        
            # Terrain scale CLI
            terrain_parser = subparsers.add_parser("terrain", help="Generate terrain-based scale")
            terrain_parser.add_argument("--prime-count", type=int, default=1000)
            terrain_parser.add_argument("--base-frequency", type=float, default=220.0)
            terrain_parser.add_argument("--num-notes", type=int, default=8)
            terrain_parser.add_argument("--window-size", type=float, default=0.007)
            terrain_parser.add_argument("--density-resolution", type=int, default=4000)
            terrain_parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
            terrain_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
            terrain_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
            terrain_parser.add_argument("--weight-curve", type=float, default=1.0)
            terrain_parser.set_defaults(include_bounds=True)
        
            # Gap scale CLI
            gap_parser = subparsers.add_parser("gap", help="Generate gap-based scale")
            gap_parser.add_argument("--prime-count", type=int, required=True)
            gap_parser.add_argument("--base-frequency", type=float, default=220.0)
            gap_parser.add_argument("--threshold-range", nargs=2, type=float, required=True, metavar=("MIN", "MAX"))
            gap_parser.add_argument("--step-size", type=float, default=0.001)
            gap_parser.add_argument("--note-goal", type=int, required=True)
            gap_parser.add_argument("--tolerance", type=int, default=1)
            gap_parser.add_argument("--density-resolution", type=int, default=4000)
            gap_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
            gap_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
            gap_parser.set_defaults(include_bounds=True)
        
            # Pure scale CLI
            pure_parser = subparsers.add_parser("pure", help="Generate raw prime scale")
            pure_parser.add_argument("--prime-count", type=int, required=True)
            pure_parser.add_argument("--base-frequency", type=float, default=220.0)
            pure_parser.add_argument("--density-resolution", type=int, default=4000)
            pure_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
            pure_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
            pure_parser.set_defaults(include_bounds=True)
        
            args = parser.parse_args()
        
            if args.scale_type == "terrain":
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
        
            elif args.scale_type == "gap":
                scan_thresholds(
                    prime_count=args.prime_count,
                    threshold_min=args.threshold_range[0],
                    threshold_max=args.threshold_range[1],
                    step_size=args.step_size,
                    note_goal=args.note_goal,
                    tolerance=args.tolerance,
                    base_frequency=args.base_frequency,
                    include_bounds=args.include_bounds,
                    density_resolution=args.density_resolution
                )
        
            elif args.scale_type == "pure":
                generate_pure_prime_scale(
                    prime_count=args.prime_count,
                    base_frequency=args.base_frequency,
                    include_bounds=args.include_bounds,
                    density_resolution=args.density_resolution
                )
        
        if __name__ == "__main__":
            main()
        ```

        `scale_utils.py`
        ```py
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
            return [bounds[0]] + notes + [bounds[1]]
        
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
        ```
