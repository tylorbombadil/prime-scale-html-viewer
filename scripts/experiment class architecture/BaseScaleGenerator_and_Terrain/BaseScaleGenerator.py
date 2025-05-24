class BaseScaleGenerator:
    name = "base"
    description = "Abstract base generator class."
    supports_modes = []

    def __init__(self, config):
        self.config = config

    def generate(self):
        raise NotImplementedError("Subclasses must implement generate().")

    def describe(self):
        return {
            "name": self.name,
            "description": self.description,
            "supports_modes": self.supports_modes
        }
