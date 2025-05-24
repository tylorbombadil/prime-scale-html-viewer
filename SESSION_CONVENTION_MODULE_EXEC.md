# Prime Scale App – Modular Convention Declaration
# Past any prompts here that you want as convention for switching yout AI modle to the current architecture mode.
> **This session uses strict `-m` module execution style and structured package-based architecture.**  
> Do not deviate from these rules unless explicitly instructed.

---

## Execution Rules
- All scripts must be run using:
  ```bash
  python3 -m scripts.module_name
  ```
- Never run scripts with `python3 scripts/module.py`

---

## Import Rules
- Always use full package paths:
  ```python
  from scripts.scale_utils import ...
  ```
- No relative imports or bare `import module`

---

## File & Folder Expectations
- `scripts/` must always contain `__init__.py`
- All generators, utilities, and interfaces live under `scripts/`
- Execution occurs from the **project root**

---

## Development Implications
- All generator modules should support clean `-m` execution
- CLI arguments must remain consistent across all modules
- `main.py` (if present) should serve as a dynamic loader or manifest router, not a script hub
