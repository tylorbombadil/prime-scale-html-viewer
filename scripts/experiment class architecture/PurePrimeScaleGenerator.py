import math
from scripts.BaseScaleGenerator import BaseScaleGenerator
from scripts.scale_utils import (
    generate_primes,
    reduce_value,
    get_log_positions,
    export_json,
    add_bounds
)

class PurePrimeScaleGenerator(BaseScaleGenerator):
    name = "pure_prime_scale"
    description = "Generates a scale from the raw prime set with no filtering or terrain logic."
    supports_modes = []

    def generate(self):
        primes = generate_primes(self.config["prime_count"])
        reduced_primes = [reduce_value(p) for p in primes]
        log_positions = get_log_positions(primes)

        if self.config["include_bounds"]:
            log_positions = add_bounds(log_positions, self.config["base_frequency"])

        notes = []
        for x in log_positions:
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
            "algorithm_manifest": {
                "name": self.name
            }
        }

        scale_data = {
            "notes": notes,
            "metadata": metadata
        }

        export_json(scale_data, "pure_scale.json")
        return scale_data
