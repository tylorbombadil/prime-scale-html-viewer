# Prime Scale App – Class-Based Plugin Architecture

This document introduces the refactor to a modular, class-based structure for scale generation logic.

---

## Purpose

To standardize all scale generator modules under a shared interface for:
- Clean modular design
- Easier plugin discovery and integration
- Future migration to Java/Android

---

## Core Structure

### Base Class
All generators inherit from a shared base class:
```python
class BaseScaleGenerator:
    def __init__(self, config): ...
    def generate(self): ...
    def describe(self): ...
```

### Concrete Subclasses
Each scale type implements its own generator subclass:
```python
class TerrainScaleGenerator(BaseScaleGenerator): ...
class PurePrimeScaleGenerator(BaseScaleGenerator): ...
```

These provide `generate()` and optionally define:
- `name`
- `description`
- `supports_modes`

---

## Benefits

- Unified structure across all algorithms
- Dynamic loading and routing possible via manifest or registry
- Easier transition to Java with abstract class patterns
- Enables semantic documentation (e.g. `.describe()`) and UI automation

---

## Directory Placement

Class-based generators are stored in the `scripts/` folder:
```
scripts/
├── BaseScaleGenerator.py
├── TerrainScaleGenerator.py
├── PurePrimeScaleGenerator.py
```

---

## Next Steps

- Refactor all legacy generators into this structure
- Replace `main.py` routing with dynamic class loader
- Update module manifest to map scale types to class paths
