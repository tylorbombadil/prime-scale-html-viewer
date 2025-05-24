import math
from scripts.BaseScaleGenerator import BaseScaleGenerator
from scripts.scale_utils import (
    generate_primes,
    reduce_value,
    get_log_positions,
    generate_density_axis,
    circular_distance,
    prime_weight,
    add_bounds,
    export_json
)

class TerrainScaleGenerator(BaseScaleGenerator):
    name = "terrain_scale"
    description = "Generates a terrain-based scale using prime density valleys or peaks."
    supports_modes = ["valley", "peak"]

    def generate(self):
        primes = generate_primes(self.config["prime_count"])
        reduced_primes = [reduce_value(p) for p in primes]
        log_positions = get_log_positions(primes)
        x_axis = generate_density_axis(self.config["density_resolution"])

        density_map = []
        for x in x_axis:
            total_weight = 0
            for log_pos, p in zip(log_positions, primes):
                distance = circular_distance(x, log_pos)
                if distance <= self.config["window_size"] / 2:
                    weight = prime_weight(p, curve=self.config["weight_curve"])
                    total_weight += weight * self._gravitational_fade(distance)
            density_map.append(total_weight)

        segment_width = 1.0 / self.config["num_notes"]
        selected_notes = []
        for i in range(self.config["num_notes"]):
            start = i * segment_width
            end = start + segment_width
            segment_range = [(x, d) for x, d in zip(x_axis, density_map) if start <= x < end]
            if segment_range:
                if self.config["mode"] == "valley":
                    best_x = min(segment_range, key=lambda t: t[1])[0]
                else:
                    best_x = max(segment_range, key=lambda t: t[1])[0]
                selected_notes.append(best_x)

        if self.config["include_bounds"]:
            selected_notes = add_bounds(selected_notes, self.config["base_frequency"])

        notes = []
        for x in selected_notes:
            freq = self.config["base_frequency"] * (2 ** x)
            midi = round(69 + 12 * math.log2(freq / 440.0))
            cents = round(1200 * x, 2)
            notes.append({
                "log_position": x,
                "frequency": round(freq, 3),
                "midi": midi,
                "cents_from_base": cents
            })

        metadata = {
            "prime_count": len(primes),
            "primes": primes,
            "log_prime_positions": log_positions,
            "linear_prime_positions": reduced_primes,
            "x_axis": x_axis,
            "density_map": density_map,
            "algorithm_manifest": {
                "name": self.name,
                "window_size": self.config["window_size"],
                "lens_profile": "gravitational",
                "mode": self.config["mode"],
                "note_segments": selected_notes
            }
        }

        scale_data = {
            "notes": notes,
            "metadata": metadata
        }

        export_json(scale_data, "terrain_scale.json")
        return scale_data

    def _gravitational_fade(self, distance, power=2.5):
        relative = distance / (self.config["window_size"] / 2)
        return 1 / (1 + (relative ** power))
