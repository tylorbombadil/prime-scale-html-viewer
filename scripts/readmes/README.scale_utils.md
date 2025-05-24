# scale_utils.py – Utility Layer for Scale Generation

This module provides reusable mathematical and data transformation functions for scale algorithms.

---

## Key Functions and Schemas

### 1. `generate_primes(n)`
- **Returns**: `list[int]`
- **Purpose**: Generates the first `n` prime numbers.
- **Schema**: `[2, 3, 5, 7, 11, ...]`

---

### 2. `reduce_value(val)`
- **Returns**: `float` in range `[1, 2)`
- **Purpose**: Reduces a number to a single-octave representation via powers of 2.

---

### 3. `get_log_positions(primes)`
- **Returns**: `list[float]` in `[0, 1]`
- **Purpose**: Maps reduced primes into log2 space for pitch-based modeling.

---

### 4. `generate_density_axis(resolution)`
- **Returns**: `list[float]`
- **Purpose**: Generates a linear x-axis of scan points from 0 to 1.
- **Schema**: `[0.0, 1/res, ..., (res-1)/res]`

---

### 5. `circular_distance(a, b)`
- **Returns**: `float`
- **Purpose**: Computes the shortest wrapped distance between two octave positions.

---

### 6. `prime_weight(p, curve=1.0)`
- **Returns**: `float`
- **Purpose**: Calculates the influence weight of a prime using inverse exponential scaling.

---

### 7. `add_bounds(notes, base_freq)`
- **Returns**: list of `log_position` floats (with 0.0 and 1.0 prepended and appended).
- **Purpose**: Adds octave boundary notes to a scale.
- **Bound Schema**:
```json
{
  "log_position": 0.0 or 1.0,
  "frequency": Hz,
  "midi": int,
  "cents_from_base": 0.0 or 1200.0,
  "prime_sources": []
}
```

---

### 8. `export_json(scale_data, filename)`
- **Purpose**: Saves scale output data to `/output/filename.json`.
- **Effect**: Ensures consistent and portable file storage for downstream use.

---

## Design Notes

- **Modular**: Keeps algorithm logic clean and centralized.
- **Schema-aligned**: Supports both musical and computational forms.
- **Universal**: Used by all generator modules in the system.
