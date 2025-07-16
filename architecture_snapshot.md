# Project Architecture Snapshot

## Directory Tree

**.** _(Full Path: `/home/mint/my-root/my-dev-projects/github-remote-projects/prime-scale-app/prime-scale-html-viewer`)_

├── `README.md`
├── `SESSION_CONVENTION_MODULE_EXEC.md`
├── `bug_framing_cheat_card.md`
├── `generate_manifest.py`
├── `import_scales_to_db.py`
├── **readmes/**
├── `scales.db`
├── **scripts/**
│   ├── `README.scale_utils.md`
│   ├── `__init__.py`
│   ├── `core_pure_prime_scale.py`
│   ├── `core_terrain_scale_after_restoration.py`
│   ├── **experiment class architecture/**
│   │   ├── **BaseScaleGenerator_and_Terrain/**
│   │   │   ├── `BaseScaleGenerator.py`
│   │   │   └── `TerrainScaleGenerator.py`
│   │   ├── `PurePrimeScaleGenerator.py`
│   │   └── `README.class_architecture.md`
│   ├── **original generators python/**
│   │   ├── `binary_gap_analyzer.py`
│   │   ├── `cluster_finder.py`
│   │   ├── `core_pure_prime_scale.py`
│   │   ├── `core_pure_prime_scale_backup_bounds_bug.py`
│   │   └── `gap_threshold_scout.py`
│   ├── **readmes/**
│   │   └── `readmes.tar.gz`
│   ├── `run_terrain_selector_test.sh`
│   └── `scale_utils.py`
└── **viewer/**
    ├── `architecture_snapshot.txt`
    ├── **assets/**
    ├── `index.html`
    ├── **js/**
    │   ├── **audio/**
    │   │   ├── `startup_audio.js`
    │   │   └── `tone_play.js`
    │   ├── `draw.js`
    │   ├── `main.js`
    │   ├── **midi/**
    │   │   └── `midi_input.js`
    │   ├── **modules/**
    │   │   ├── `draw_density.js`
    │   │   ├── `draw_notes.js`
    │   │   ├── `draw_primes.js`
    │   │   └── `draw_segments.js`
    │   ├── **ui/**
    │   │   └── `dropdown.js`
    │   └── `utils.js`
    └── `style.css`

---

## Project Architecture Snapshot

**/home/mint/my-root/my-dev-projects/github-remote-projects/prime-scale-app/prime-scale-html-viewer**

        `README.md`
        ```md
        # Prime Scale App Sandbox
        
        ## The Purpose of This Sandbox
        
        This sandbox exists for **one reason**:
        
        > To transition the original Python core algorithm scripts into structured schema-based modules that will be converted into JavaScript for use in the Prime Scale App Android APK.
        
        These Python scripts form the **mathematical and conceptual core** of the Prime Scale App. They are the foundation, the reference, and the holy grail. But they were not originally written to scale or adapt easily across platforms. This sandbox gives us the place to carefully restructure them.
        
        The final goal is to translate these schema-based Python modules into **JavaScript modules** that will power the **Prime Scale App APK**, which is built using **Java and other mobile-friendly dependencies**.
        
        ---
        
        ## The Schema Convention (Key Concept)
        
        The file `core_terrain_scale.py` is the official schema prototype.
        
        All other algorithms must eventually adopt its structure, either by:
        
        1. Morphing legacy scripts directly into schema-compatible Python versions,  
        2. Or porting them to JavaScript while following this schema’s logic and conventions.
        
        ### Key Features of the Schema Convention
        
        - Modular Imports from `scale_utils.py`
        - Structured Metadata:
          - Prime list
          - Log positions
          - Regular (non-log) positions
          - Sampling access resolution
          - Total prime count
        - Top-Level Notes with frequency, log position, MIDI estimate
        - CLI Arguments: base frequency, resolution, bounds, etc.
        - Embedded Manifesto: self-documents the algorithm type and structure
        
        ```text
        scripts/
        ├── core_terrain_scale.py   <- Schema GOLD STANDARD
        ├── scale_utils.py                              <- Shared utilities
        ├── update_manifest.py                          <- Refreshes manifest for viewer
        ```
        
        ---
        
        ## How to Use the Sandbox
        
        ### 1. Generate a Scale
        From the root directory, run:
        ```bash
        python3 -m scripts.core_terrain_scale_final_rewired_debug \
          --prime-count 1000 \
          --base-frequency 220 \
          --num-notes 8 \
          --window-size 0.007 \
          --density-resolution 4000 \
          --mode valley \
          --bounds
        ```
        
        > Important: Use class-style entry like `scripts.filename`. Always run from the top-level folder.
        
        ---
        
        ### 2. Update the Manifest
        ```bash
        python3 -m scripts.update_manifest
        ```
        This regenerates the list of available scale files for the viewer.
        
        ---
        
        ## Using the Sandbox Viewer
        
        This repo includes a basic HTML+JS viewer to display scale output.
        
        ### Features:
        - Tall gray lines = full prime field  
        - Black dots = selected notes  
        - Dropdown to load any scale  
        - Button list for tone preview
        
        ### Run the Viewer
        ```bash
        python3 -m http.server 8080
        ```
        Then go to:
        ```
        http://localhost:8080
        ```
        
        ### Folder Overview
        ```
        project-root/
        ├── scripts/            # Algorithm logic
        ├── output/             # .json scale files + manifest
        ├── viewer.js           # Viewer logic
        ├── index.html          # Viewer UI
        ```
        
        ---
        
        ## Final Note to Developers
        
        This is a prototype workspace for refactoring and converting the core algorithms.
        
        Stick to the schema! The better these modules conform, the easier it will be to translate them into JS and Java for the final Prime Scale App APK.
        
        Refer to the `core_terrain_scale_final_rewired_debug.py` script as your guide.
        
        Your mission: preserve the mathematical essence, refactor into schema, and get us one step closer to a fully musical APK.
        ```

        `SESSION_CONVENTION_MODULE_EXEC.md`
        ```md
        # Prime Scale App – Modular Convention Declaration
        
        # note to other collaborators:
        # This md is to help me to prompt GPT so that the model and I agree about the architecture that we are currently coding and debugging for.
        # This approach is a bug prevention measure because chat GPT is heavily reliant on internal tags. This just starts the session 
        # on the right foot.
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
        ```

        `bug_framing_cheat_card.md`
        ```md
        # Bug Framing Cheat Card: How to Ask for a Fast, Clean Fix
        
        ## Purpose
        Use this guide to frame your bug reports in a way that makes it easy for ChatGPT (or any dev assistant) to zero in on the problem and solve it quickly.
        
        ---
        
        ## 1. Mention What the Code *Should* Be Doing
        Example:
        > “There should be only one dot drawn per note, and it should appear above the prime field.”
        
        This sets a clear expectation boundary.
        
        ---
        
        ## 2. Ask to Scan All Draw or Effect Calls
        Example:
        > “Can you grep the file for `ctx.arc` or anything drawing on the canvas?”
        
        This forces a wide scan instead of narrow patching.
        
        ---
        
        ## 3. Add a Console Debug Print
        Even just:
        ```js
        console.log("drawing dot")
        ```
        Tells you immediately whether the loop is being reached or skipped.
        
        ---
        
        ## 4. Declare “This Should Be the Only Drawing Function”
        Example:
        > “drawLineReadout should be the only place anything is drawn.”
        
        This lets the assistant know if other behavior is rogue.
        
        ---
        
        ## 5. If Something’s Still Wrong, Ask for a Function Audit
        > “Can you list all functions that touch `ctx`?”
        
        This surfaces hidden draw logic, transformations, or rogue copies.
        
        ---
        
        ## 6. Ask for a Structural Sanity Pass
        > “Before patching, can you do a structural pass on the file to confirm how drawing is triggered?”
        
        This adds a pre-flight before any changes are made.
        
        ---
        
        ## Endgame Tip
        The best bug fix starts by *mapping the system*, not *swapping a part*.
        ```

        `generate_manifest.py`
        ```py
        import os
        import json
        
        output_dir = "output"
        scales = []
        
        # Collect all JSON files except manifest.json itself
        for file in sorted(os.listdir(output_dir), reverse=True):
            if file.endswith(".json") and file != "manifest.json":
                scales.append(file)
        
        manifest = {"scales": scales}
        
        with open(os.path.join(output_dir, "manifest.json"), "w") as f:
            json.dump(manifest, f, indent=2)
        
        print("✔ Manifest updated.")
        ```

        `import_scales_to_db.py`
        ```py
        import os
        import json
        import sqlite3
        from datetime import datetime
        
        # Path to folder with your .json scale files
        SCALE_FOLDER = "./output"
        DB_FILE = "scales.db"
        
        # --- Step 1: Connect to DB and Create Tables ---
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS scales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            title TEXT,
            description TEXT,
            algorithm TEXT,
            prime_count INTEGER,
            note_count INTEGER,
            bounds TEXT,
            resolution INTEGER,
            segment_count INTEGER,
            mode TEXT,
            created_at TEXT
        );
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS parameters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scale_id INTEGER,
            name TEXT,
            value TEXT,
            FOREIGN KEY(scale_id) REFERENCES scales(id)
        );
        """)
        
        # --- Step 2: Parse JSON Files ---
        def parse_scale_file(filepath):
            with open(filepath, 'r') as f:
                data = json.load(f)
        
            # Extract core fields
            manifest = data.get("algorithm_manifest", {})
            meta = {
                "filename": os.path.basename(filepath),
                "title": manifest.get("title"),
                "description": manifest.get("description"),
                "algorithm": manifest.get("parameters", {}).get("mode"),
                "prime_count": data.get("prime_count"),
                "note_count": len(data.get("notes", [])),
                "bounds": str(data.get("bounds")),
                "resolution": data.get("resolution_total") or data.get("density_resolution"),
                "segment_count": len(data.get("segment_boundaries", [])),
                "mode": manifest.get("parameters", {}).get("mode"),
                "created_at": datetime.now().isoformat()
            }
            return meta, manifest.get("parameters", {})
        
        # --- Step 3: Walk folder and load each scale ---
        for fname in os.listdir(SCALE_FOLDER):
            if fname.endswith(".json"):
                try:
                    filepath = os.path.join(SCALE_FOLDER, fname)
                    meta, params = parse_scale_file(filepath)
        
                    # Insert scale
                    cursor.execute("""
                        INSERT INTO scales (
                            filename, title, description, algorithm,
                            prime_count, note_count, bounds,
                            resolution, segment_count, mode, created_at
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        meta["filename"], meta["title"], meta["description"], meta["algorithm"],
                        meta["prime_count"], meta["note_count"], meta["bounds"],
                        meta["resolution"], meta["segment_count"], meta["mode"], meta["created_at"]
                    ))
        
                    scale_id = cursor.lastrowid
        
                    # Insert parameters
                    for key, val in params.items():
                        cursor.execute("""
                            INSERT INTO parameters (scale_id, name, value)
                            VALUES (?, ?, ?)
                        """, (scale_id, key, str(val)))
        
                    print(f"✓ Imported: {fname}")
                except Exception as e:
                    print(f"⚠️  Failed to import {fname}: {e}")
        
        conn.commit()
        conn.close()
        print("✅ Done.")
        ```

        **readmes/**

        **scripts/**

            `scripts/README.scale_utils.md`
            ```md
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
            ```

            `scripts/__init__.py`
            ```py
            ```

            `scripts/core_pure_prime_scale.py`
            ```py
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
            ```

            `scripts/core_terrain_scale_after_restoration.py`
            ```py
            # ===[ IMPORTS ]===
            from collections import OrderedDict
            import argparse
            import os
            import json
            import math
            
            # Shared utility functions
            from scripts.scale_utils import(
                generate_primes,
                reduce_value,
                get_log_positions,
                generate_density_axis,
                add_bounds,
                export_json,
                circular_distance,
                prime_weight
            )
            
            # ===[ TERRAIN-SPECIFIC FUNCTION ]===
            # This fade function simulates gravitational pull — stronger at the center of the lens.
            def gravitational_fade(distance, width, power=2.5):
                relative = distance / (width / 2)
                return 1 / (1 + (relative ** power))
            
            # ===[ MAIN SCALE GENERATION FUNCTION ]===
            def generate_scale(prime_count, base_frequency, num_notes, window_size, density_resolution, mode, include_bounds, dial_value):
                # Step 1: Generate primes and reduce them to fall within one octave
                primes = generate_primes(prime_count)
                reduced_primes = [reduce_value(p) for p in primes]
                log_positions = get_log_positions(reduced_primes)
            
                # Step 2: Create the sampling axis (granular points across [0, 1])
                x_axis = generate_density_axis(density_resolution)
            
                # Step 3: Build a weighted density map across the axis
                density_map = []
                for x in x_axis:
                    total_weight = 0
                    for log_pos, prime in zip(log_positions, primes):
                        weight = prime_weight(prime, dial_value) # Inverse of the prime for its influence
                        # CHANGED INLINE CIRCULAR DISTANCE MATH TO UTILITIES CALL FOR GOOD ORDER AND DEBUGGNG
                        wrapped_distance = circular_distance(log_pos, x)  # Handle octave wrapping
                        if wrapped_distance <= window_size / 2:
                            total_weight += weight * gravitational_fade(wrapped_distance, window_size)
                    density_map.append(total_weight)
            
                # Step 4: Split axis into even segments and pick a representative from each
                segment_width = 1.0 / num_notes
                # DELETED SWEEP WIDTH = WINDOWSIZE FOR RESORATION REFACTOR
                selected_notes = []
            
                for i in range(num_notes):
                    segment_start = i * segment_width
                    segment_end = segment_start + segment_width
                    segment_range = [
                        (x, d) for x, d in zip(x_axis, density_map)
                        if segment_start <= x < segment_end
                    ]
                    if segment_range:
                        best_x = min(segment_range, key=lambda t: t[1])[0] if mode == "valley" else max(segment_range, key=lambda t: t[1])[0]
                        selected_notes.append(best_x)
            
                # Step 5: Optionally include lower and upper bounds (0.0 and 1.0)
                if include_bounds:
                    selected_notes = add_bounds(selected_notes, base_frequency)
            
                # Step 6: Package note data and export to JSON
                notes = []
                for x in selected_notes:
                    freq = base_frequency * (2 ** x)
                    midi = round(69 + 12 * math.log2(freq / 440.0))
                    cents = round(1200 * x, 2)
                    notes.append({
                        "log_position": x,
                        "frequency": round(freq, 3),
                        "midi": midi,
                        "cents_from_base": cents
                    })
            
            # ===[Metadata, Scale data, and Algorithm Manifest]===
                parameters = OrderedDict()
                parameters["window_size"] = window_size
                parameters["lens_profile"] = "gravitational"
                parameters["mode"] = mode
            
                manifest= OrderedDict()
                manifest["name"] = "terrain_scale"   
                manifest["description"] = "sampling of prime density-peak and valley mode with other variable fields"
                manifest["notes"] = num_notes
                manifest["include_bounds"] = include_bounds
                manifest["parameters"] = parameters
            
                metadata = OrderedDict()
                metadata["algorithm_manifest"] = manifest
                metadata["prime_count"] =  len(primes)
                metadata["primes"] = primes
                metadata["segment_boundaries"] = [i / num_notes for i in range(num_notes + 1)]
                metadata["log_prime_positions"] = log_positions
                metadata["linear_prime_positions"] = reduced_primes
                metadata["x_axis"] = x_axis
                metadata["density_resolution"] = density_resolution
                metadata["density_map"] = density_map
            
                scale_data = OrderedDict()
                scale_data["name"] = f"terrain_scale_{num_notes}_{mode}"
                scale_data["base_frequency"] = base_frequency
                scale_data["notes"] = notes
                scale_data["log_positions"] = log_positions, 
                scale_data["metadata"] = metadata
            
                filename = None
                export_json(scale_data, filename)
            
                return notes, metadata
            
            # ===[ ENTRY POINT ]===
            if __name__ == "__main__":
                parser = argparse.ArgumentParser(description="Generate a terrain-based prime scale using full shared utility set.")
                parser.add_argument("--prime-count", type=int, default=1000)
                parser.add_argument("--base-frequency", type=float, default=220.0)
                parser.add_argument("--num-notes", type=int, default=8)
                parser.add_argument("--window-size", type=float, default=0.007)
                parser.add_argument("--density-resolution", type=int, default=4000)
                parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
                parser.add_argument("--include-bounds", action="store_true", default=False)
                parser.add_argument("--dial-value", type=float, required=False, default=0.0, help="Analog contrast control (-1.0 to +1.0)")
            
                args = parser.parse_args()
                generate_scale(
                    prime_count=args.prime_count,
                    base_frequency=args.base_frequency,
                    num_notes=args.num_notes,
                    window_size=args.window_size,
                    density_resolution=args.density_resolution,
                    mode=args.mode,
                    include_bounds=args.include_bounds,
                    dial_value=args.dial_value
                )
            ```

            **scripts/experiment class architecture/**

                **scripts/experiment class architecture/BaseScaleGenerator_and_Terrain/**

                    `scripts/experiment class architecture/BaseScaleGenerator_and_Terrain/BaseScaleGenerator.py`
                    ```py
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
                    ```

                    `scripts/experiment class architecture/BaseScaleGenerator_and_Terrain/TerrainScaleGenerator.py`
                    ```py
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
                    ```

                `scripts/experiment class architecture/PurePrimeScaleGenerator.py`
                ```py
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
                ```

                `scripts/experiment class architecture/README.class_architecture.md`
                ```md
                # comming very soon:
                # Prime Scale App – Class-Based Plugin Architecture
                
                This document introduces the refactor to a modular, class-based structure for scale generation logic.
                GTP suggested that we go this route ult
                
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
                ```

            **scripts/original generators python/**

                `scripts/original generators python/binary_gap_analyzer.py`
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

                `scripts/original generators python/cluster_finder.py`
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

                `scripts/original generators python/core_pure_prime_scale.py`
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

                `scripts/original generators python/core_pure_prime_scale_backup_bounds_bug.py`
                ```py
                import argparse
                import math
                import os
                print("CWD:", os.getcwd())
                from scripts.scale_utils import (
                    generate_primes,
                    get_log_positions,
                    add_bounds,
                    export_json,
                    generate_density_axis
                )
                
                def generate_pure_prime_scale(prime_count, base_frequency, include_bounds=True, density_resolution=4000):
                    # Step 1: Generate prime numbers
                    primes = generate_primes(prime_count)
                
                    # Step 2: Reduce and map primes to log2 positions
                    log_positions = get_log_positions(primes)
                
                    # Step 3: Optional density axis (for visual harmony)
                    _ = generate_density_axis(density_resolution)
                
                    # Step 4: Convert log positions to notes
                    notes = []
                    for log_pos in log_positions:
                        freq = base_frequency * (2 ** log_pos)
                        midi = round(69 + 12 * math.log2(freq / 440.0))
                        cents = round(1200 * log_pos, 2)
                        notes.append({
                            "log_position": log_pos,
                            "frequency": round(freq, 3),
                            "midi": midi,
                            "cents_from_base": cents,
                            "prime_sources": []
                        })
                
                    # Step 5: Optionally add 0.0 and 1.0 boundaries
                    if include_bounds:
                        notes = add_bounds(notes, base_frequency)
                
                    # Step 6: Create metadata block
                    metadata = {
                        "prime_count": len(primes),
                        "primes": primes,
                        "log_prime_positions": log_positions,
                        "algorithm_manifest": {
                            "name": "pure_prime_scale",
                            "description": "Unfiltered prime positions mapped directly to pitch space"
                        }
                    }
                
                    # Step 7: Package and export
                    scale_data = {
                        "notes": notes,
                        "metadata": metadata
                    }
                
                    export_json(scale_data, f"pure_prime_scale_{prime_count}_primes.json")
                
                if __name__ == "__main__":
                    parser = argparse.ArgumentParser(description="Generate a scale from raw primes with no filtering.")
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

                `scripts/original generators python/gap_threshold_scout.py`
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

            **scripts/readmes/**

            `scripts/run_terrain_selector_test.sh`
            ```sh
            #!/bin/bash
            # Run the terrain_with_selector module using the current architecture
            
            python scripts/terrain_with_selector.py \
              --prime-count 32 \
              --base-frequency 220.0 \
              --num-notes 16 \
              --window-size 0.15 \
              --density-resolution 512 \
              --mode peak \
              --include-bounds \
              --dial-value 0.5 \
              --use-gravity
            ```

            `scripts/scale_utils.py`
            ```py
            import math
            import json
            import os
            from datetime import datetime
            
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
            
            def prime_weight(p, user_input):
                """
                Logarithmic analog contrast control:
                - user_input = -1.0 → weight = 1 / p  (stronger small prime influence)
                - user_input =  0.0 → weight = 1.0    (neutral influence accross the board)
                - user_input = +1.0 → weight = p      (stronger larg prime influence)
            
                Smooth, continuous interpolation using log math.
                If input exceeds bounds, clamps and notifies.
                """
                if user_input < -1.0:
                    print(f"Input {user_input} below -1.0, clamping to -1.0")
                    dial = -1.0
                elif user_input > 1.0:
                    print(f"Input {user_input} above 1.0, clamping to 1.0")
                    dial = 1.0
                else:
                    dial = user_input
            
                log_target = math.log(p) * (1 + dial)  # from log(1) to log(p^2)
                target = math.exp(log_target)
                return target / p
            
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
            
            def export_json(scale_data, filename=None):
                script_dir = os.path.dirname(os.path.abspath(__file__))
                project_root = os.path.dirname(script_dir)
                output_dir = os.path.join(project_root, "output")
                os.makedirs(output_dir, exist_ok=True)
            
                if not filename:
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"scale_{timestamp}.json"
            
                full_path = os.path.join(output_dir, filename)
            
                with open(full_path, "w", encoding="utf-8") as f:
                    json.dump(scale_data, f, indent=2)
            
                print(f"✔ Saved scale to {full_path}")
            ```

        **viewer/**

            `viewer/architecture_snapshot.txt`
            ```txt
            # Project Architecture Snapshot
            
            ## Directory Tree
            
            **.** _(Full Path: `/home/mint/my-root/my-dev-projects/github-remote-projects/prime-scale-app/prime-scale-html-viewer/viewer`)_
            
            ├── **assets/**
            ├── `index.html`
            ├── **js/**
            │   ├── **audio/**
            │   │   ├── `startup_audio.js`
            │   │   └── `tone_play.js`
            │   ├── `draw.js`
            │   ├── `main.js`
            │   ├── **midi/**
            │   │   └── `midi_input.js`
            │   ├── **modules/**
            │   │   ├── `draw_density.js`
            │   │   ├── `draw_notes.js`
            │   │   ├── `draw_primes.js`
            │   │   └── `draw_segments.js`
            │   ├── **ui/**
            │   │   └── `dropdown.js`
            │   └── `utils.js`
            └── `style.css`
            
            ---
            
            ## Project Architecture Snapshot
            
            **/home/mint/my-root/my-dev-projects/github-remote-projects/prime-scale-app/prime-scale-html-viewer/viewer**
            
                    **assets/**
            
                    `index.html`
                    ```html
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                      <meta charset="UTF-8" />
                      <title>Prime Scale Viewer</title>
                      <link rel="stylesheet" href="style.css" />
                    </head>
                    <body>
                      <h1>Prime Scale Viewer</h1>
                      <div id="scale-display">Loading...</div>
                      <canvas id="line-readout" width="1000" height="80"></canvas>
                      <script type="module" src="./js/main.js"></script>
                    </body>
                    </html>
                    ```
            
                    **js/**
            
                        **js/audio/**
            
                            `js/audio/startup_audio.js`
                            ```js
                            import * as Tone from 'https://cdn.skypack.dev/tone';
                            
                            export function enableAudioOnClick() {
                              document.body.addEventListener('click', async () => {
                                if (Tone.context.state !== 'running') {
                                  await Tone.start();
                                }
                              console.log('Audio context resumed by user gesture');
                              }, { once: true });
                            }
                            ```
            
                            `js/audio/tone_play.js`
                            ```js
                            import * as Tone from 'https://cdn.skypack.dev/tone';
                            const reverb = new Tone.Reverb({ decay: 4, wet: 0.5 }).toDestination();
                            const synth = new Tone.PolySynth(Tone.Synth).connect(reverb);
                            
                            export function playNote(frequency) {
                              synth.triggerAttackRelease(frequency, "2n");
                            }
                            
                            export function resumeAudio() {
                              if (Tone.context.state !== 'running') {
                                Tone.context.resume();
                               }
                             }
                            ```
            
                        `js/draw.js`
                        ```js
                        import { drawNotes } from './modules/draw_notes.js';
                        import { drawSegments } from './modules/draw_segments.js';
                        import { drawPrimes } from './modules/draw_primes.js';
                        import { drawDensity } from './modules/draw_density.js';
                        
                        export function drawScale(scale) {
                          const canvas = document.getElementById('line-readout');
                          const ctx = canvas.getContext('2d');
                        
                          ctx.clearRect(0, 0, canvas.width, canvas.height);
                        
                          // draw base line
                          ctx.beginPath();
                          ctx.moveTo(0, canvas.height / 2);
                          ctx.lineTo(canvas.width, canvas.height / 2);
                          ctx.strokeStyle = '#888';
                          ctx.lineWidth = 1;
                          ctx.stroke();
                        
                          drawPrimes(ctx, scale, canvas);  
                          drawSegments(ctx, scale, canvas);
                          drawNotes(ctx, scale, canvas);
                          drawDensity(ctx, scale, canvas);
                        }
                        ```
            
                        `js/main.js`
                        ```js
                        import * as Tone from 'https://cdn.skypack.dev/tone';
                        import { enableAudioOnClick } from './audio/startup_audio.js';
                        
                        window.addEventListener('DOMContentLoaded', () => {
                          enableAudioOnClick(); 
                        });
                        
                        import { drawScale } from './draw.js';
                        import { loadScale } from './utils.js';
                        import { setupDropdown } from './ui/dropdown.js';
                        
                        setupDropdown(drawScale);
                        ```
            
                        **js/midi/**
            
                            `js/midi/midi_input.js`
                            ```js
                            import { playNote } from '../audio/tone_play.js';
                            
                            let midiInputs = [];
                            
                            export function setupMidiInput(scale) {
                              navigator.requestMIDIAccess().then(midi => {
                                // Clear old handlers
                                for (const input of midiInputs) {
                                  input.onmidimessage = null;
                                }
                            
                                midiInputs = [...midi.inputs.values()];
                            
                                for (const input of midiInputs) {
                                  input.onmidimessage = ({ data }) => {
                                    console.log('MIDI message:', data);
                                    const [status, note, velocity] = data;
                            
                                    if (status === 144 && velocity > 0) {
                                      const index = note - 60; // Middle C = 60
                                      const scaleNote = scale.notes[index];
                            
                                      if (scaleNote && scaleNote.frequency) {
                                        console.log(`Playing index ${index}: ${scaleNote.frequency}`);
                                        playNote(scaleNote.frequency);
                                      }
                                    }
                                  };
                                }
                              }).catch(err => {
                                console.error("MIDI init failed:", err);
                              });
                            }
                            ```
            
                        **js/modules/**
            
                            `js/modules/draw_density.js`
                            ```js
                            // Draw density map as grayscale
                            export function drawDensity(ctx, scale, canvas) {
                              if (scale.metadata && scale.metadata.density_map && scale.metadata.x_axis) {
                                const max = Math.max(...scale.metadata.density_map);
                                const min = Math.min(...scale.metadata.density_map);
                                const range = max - min || 1;
                            
                                scale.metadata.density_map.forEach((val, i) => {
                                  const x = scale.metadata.x_axis[i] * canvas.width;
                                  const norm = (val - min) / range;
                                  const gray = Math.floor(norm * 255);
                                  ctx.strokeStyle = `rgb(${gray}, ${gray}, ${gray})`;
                            
                                  ctx.beginPath();
                                  ctx.moveTo(x, canvas.height / 2 + 30);
                                  ctx.lineTo(x, canvas.height / 2 + 35);
                                  ctx.stroke();
                                });
                              }
                            }
                            ```
            
                            `js/modules/draw_notes.js`
                            ```js
                            export function drawNotes(ctx, scale, canvas) {
                              if (!scale.notes) return;
                            
                              ctx.fillStyle = 'black';
                              const offset = 14;
                            
                              scale.notes.forEach(note => {
                                const x = note.log_position * canvas.width;
                                const y = canvas.height / 2 - offset;
                            
                                ctx.beginPath();
                                ctx.arc(x, y, 4, 0, 2 * Math.PI);
                                ctx.fill();
                              });
                            }
                            ```
            
                            `js/modules/draw_primes.js`
                            ```js
                            export function drawPrimes(ctx, scale, canvas) {
                              const primes = scale.metadata?.log_prime_positions;
                              if (!primes || !primes.length) return;
                            
                              ctx.strokeStyle = '#ccc';
                              ctx.lineWidth = 1;
                            
                              primes.forEach(p => {
                                const x = p * canvas.width;
                                ctx.beginPath();
                                ctx.moveTo(x, canvas.height / 2 - 10);
                                ctx.lineTo(x, canvas.height / 2 + 10);
                                ctx.stroke();
                              });
                            }
                            ```
            
                            `js/modules/draw_segments.js`
                            ```js
                            export function drawSegments(ctx, scale, canvas) {
                              if (!scale.metadata?.segment_boundaries) return;
                            
                              ctx.strokeStyle = '#aaa';
                              ctx.lineWidth = 1;
                              ctx.setLineDash([5, 4]); // dashed
                            
                              scale.metadata.segment_boundaries.forEach(pos => {
                                const x = pos * canvas.width;
                                ctx.beginPath();
                                ctx.moveTo(x, 0);
                                ctx.lineTo(x, canvas.height);
                                ctx.stroke();
                              });
                            
                              ctx.setLineDash([]); // reset dash
                            }
                            ```
            
                        **js/ui/**
            
                            `js/ui/dropdown.js`
                            ```js
                            import { setupMidiInput } from '../midi/midi_input.js';
                            import { playNote, resumeAudio } from '../audio/tone_play.js';
                            export function setupDropdown(drawCallback) {
                              const scaleDisplay = document.getElementById('scale-display');
                            
                              fetch('../output/manifest.json')
                                .then(res => res.json())
                                .then(manifest => {
                                  const dropdown = document.createElement('select');
                                  dropdown.onchange = () => loadScale(dropdown.value);
                            
                                  manifest.scales.forEach(file => {
                                    const option = document.createElement('option');
                                    option.value = file;
                                    option.textContent = file;
                                    dropdown.appendChild(option);
                                  });
                            
                                  document.body.insertBefore(dropdown, scaleDisplay);
                                  if (manifest.scales.length > 0) {
                                    loadScale(manifest.scales[0]);
                                  }
                                })
                                .catch(err => {
                                  scaleDisplay.textContent = 'Failed to load manifest file.';
                                  console.error(err);
                                });
                            
                              function loadScale(filename) {
                                fetch('../output/' + filename)
                                  .then(res => res.json())
                                  .then(scale => {
                                    scaleDisplay.innerHTML = '';
                                    drawCallback(scale);
                            
                              setupMidiInput(scale);
                             
                                 console.log('scale.notes:', scale.notes)
                            
                                 const buttonContainer = document.createElement('div');
                                  buttonContainer.style.marginTop = '1em';
                            
                                  scale.notes.forEach(note => {
                                    const btn = document.createElement('button');
                                    btn.textContent = note.frequency.toFixed(2) + ' Hz';
                                    btn.style.margin = '4px';
                                    btn.onclick = () => playNote(note.frequency);
                                    buttonContainer.appendChild(btn);
                                  });
                            
                                  scaleDisplay.appendChild(buttonContainer);
                                  })
                                  .catch(err => {
                                    scaleDisplay.textContent = 'Failed to load scale file.';
                                    console.error(err);
                                  });
                              }
                            }
                            ```
            
                        `js/utils.js`
                        ```js
                        export async function loadScale(path) {
                          const res = await fetch(path);
                          if (!res.ok) throw new Error('Failed to load scale file');
                          return await res.json();
                        }
                        ```
            
                    `style.css`
                    ```css
                    body {
                      font-family: sans-serif;
                      margin: 2rem;
                      background: #f4f4f4;
                    }
                    
                    canvas {
                      border: 1px solid #ccc;
                      background: #fff;
                    }
                    ```
            ```

            **viewer/assets/**

            `viewer/index.html`
            ```html
            <!DOCTYPE html>
            <html lang="en">
            <head>
              <meta charset="UTF-8" />
              <title>Prime Scale Viewer</title>
              <link rel="stylesheet" href="style.css" />
            </head>
            <body>
              <h1>Prime Scale Viewer</h1>
              <div id="scale-display">Loading...</div>
              <canvas id="line-readout" width="1000" height="80"></canvas>
              <script type="module" src="./js/main.js"></script>
            </body>
            </html>
            ```

            **viewer/js/**

                **viewer/js/audio/**

                    `viewer/js/audio/startup_audio.js`
                    ```js
                    import * as Tone from 'https://cdn.skypack.dev/tone';
                    
                    export function enableAudioOnClick() {
                      document.body.addEventListener('click', async () => {
                        if (Tone.context.state !== 'running') {
                          await Tone.start();
                        }
                      console.log('Audio context resumed by user gesture');
                      }, { once: true });
                    }
                    ```

                    `viewer/js/audio/tone_play.js`
                    ```js
                    import * as Tone from 'https://cdn.skypack.dev/tone';
                    const reverb = new Tone.Reverb({ decay: 4, wet: 0.5 }).toDestination();
                    const synth = new Tone.PolySynth(Tone.Synth).connect(reverb);
                    
                    export function playNote(frequency) {
                      synth.triggerAttackRelease(frequency, "2n");
                    }
                    
                    export function resumeAudio() {
                      if (Tone.context.state !== 'running') {
                        Tone.context.resume();
                       }
                     }
                    ```

                `viewer/js/draw.js`
                ```js
                import { drawNotes } from './modules/draw_notes.js';
                import { drawSegments } from './modules/draw_segments.js';
                import { drawPrimes } from './modules/draw_primes.js';
                import { drawDensity } from './modules/draw_density.js';
                
                export function drawScale(scale) {
                  const canvas = document.getElementById('line-readout');
                  const ctx = canvas.getContext('2d');
                
                  ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                  // draw base line
                  ctx.beginPath();
                  ctx.moveTo(0, canvas.height / 2);
                  ctx.lineTo(canvas.width, canvas.height / 2);
                  ctx.strokeStyle = '#888';
                  ctx.lineWidth = 1;
                  ctx.stroke();
                
                  drawPrimes(ctx, scale, canvas);  
                  drawSegments(ctx, scale, canvas);
                  drawNotes(ctx, scale, canvas);
                  drawDensity(ctx, scale, canvas);
                }
                ```

                `viewer/js/main.js`
                ```js
                import * as Tone from 'https://cdn.skypack.dev/tone';
                import { enableAudioOnClick } from './audio/startup_audio.js';
                
                window.addEventListener('DOMContentLoaded', () => {
                  enableAudioOnClick(); 
                });
                
                import { drawScale } from './draw.js';
                import { loadScale } from './utils.js';
                import { setupDropdown } from './ui/dropdown.js';
                
                setupDropdown(drawScale);
                ```

                **viewer/js/midi/**

                    `viewer/js/midi/midi_input.js`
                    ```js
                    import { playNote } from '../audio/tone_play.js';
                    
                    let midiInputs = [];
                    
                    export function setupMidiInput(scale) {
                      navigator.requestMIDIAccess().then(midi => {
                        // Clear old handlers
                        for (const input of midiInputs) {
                          input.onmidimessage = null;
                        }
                    
                        midiInputs = [...midi.inputs.values()];
                    
                        for (const input of midiInputs) {
                          input.onmidimessage = ({ data }) => {
                            console.log('MIDI message:', data);
                            const [status, note, velocity] = data;
                    
                            if (status === 144 && velocity > 0) {
                              const index = note - 60; // Middle C = 60
                              const scaleNote = scale.notes[index];
                    
                              if (scaleNote && scaleNote.frequency) {
                                console.log(`Playing index ${index}: ${scaleNote.frequency}`);
                                playNote(scaleNote.frequency);
                              }
                            }
                          };
                        }
                      }).catch(err => {
                        console.error("MIDI init failed:", err);
                      });
                    }
                    ```

                **viewer/js/modules/**

                    `viewer/js/modules/draw_density.js`
                    ```js
                    // Draw density map as grayscale
                    export function drawDensity(ctx, scale, canvas) {
                      if (scale.metadata && scale.metadata.density_map && scale.metadata.x_axis) {
                        const max = Math.max(...scale.metadata.density_map);
                        const min = Math.min(...scale.metadata.density_map);
                        const range = max - min || 1;
                    
                        scale.metadata.density_map.forEach((val, i) => {
                          const x = scale.metadata.x_axis[i] * canvas.width;
                          const norm = (val - min) / range;
                          const gray = Math.floor(norm * 255);
                          ctx.strokeStyle = `rgb(${gray}, ${gray}, ${gray})`;
                    
                          ctx.beginPath();
                          ctx.moveTo(x, canvas.height / 2 + 30);
                          ctx.lineTo(x, canvas.height / 2 + 35);
                          ctx.stroke();
                        });
                      }
                    }
                    ```

                    `viewer/js/modules/draw_notes.js`
                    ```js
                    export function drawNotes(ctx, scale, canvas) {
                      if (!scale.notes) return;
                    
                      ctx.fillStyle = 'black';
                      const offset = 14;
                    
                      scale.notes.forEach(note => {
                        const x = note.log_position * canvas.width;
                        const y = canvas.height / 2 - offset;
                    
                        ctx.beginPath();
                        ctx.arc(x, y, 4, 0, 2 * Math.PI);
                        ctx.fill();
                      });
                    }
                    ```

                    `viewer/js/modules/draw_primes.js`
                    ```js
                    export function drawPrimes(ctx, scale, canvas) {
                      const primes = scale.metadata?.log_prime_positions;
                      if (!primes || !primes.length) return;
                    
                      ctx.strokeStyle = '#ccc';
                      ctx.lineWidth = 1;
                    
                      primes.forEach(p => {
                        const x = p * canvas.width;
                        ctx.beginPath();
                        ctx.moveTo(x, canvas.height / 2 - 10);
                        ctx.lineTo(x, canvas.height / 2 + 10);
                        ctx.stroke();
                      });
                    }
                    ```

                    `viewer/js/modules/draw_segments.js`
                    ```js
                    export function drawSegments(ctx, scale, canvas) {
                      if (!scale.metadata?.segment_boundaries) return;
                    
                      ctx.strokeStyle = '#aaa';
                      ctx.lineWidth = 1;
                      ctx.setLineDash([5, 4]); // dashed
                    
                      scale.metadata.segment_boundaries.forEach(pos => {
                        const x = pos * canvas.width;
                        ctx.beginPath();
                        ctx.moveTo(x, 0);
                        ctx.lineTo(x, canvas.height);
                        ctx.stroke();
                      });
                    
                      ctx.setLineDash([]); // reset dash
                    }
                    ```

                **viewer/js/ui/**

                    `viewer/js/ui/dropdown.js`
                    ```js
                    import { setupMidiInput } from '../midi/midi_input.js';
                    import { playNote, resumeAudio } from '../audio/tone_play.js';
                    export function setupDropdown(drawCallback) {
                      const scaleDisplay = document.getElementById('scale-display');
                    
                      fetch('../output/manifest.json')
                        .then(res => res.json())
                        .then(manifest => {
                          const dropdown = document.createElement('select');
                          dropdown.onchange = () => loadScale(dropdown.value);
                    
                          manifest.scales.forEach(file => {
                            const option = document.createElement('option');
                            option.value = file;
                            option.textContent = file;
                            dropdown.appendChild(option);
                          });
                    
                          document.body.insertBefore(dropdown, scaleDisplay);
                          if (manifest.scales.length > 0) {
                            loadScale(manifest.scales[0]);
                          }
                        })
                        .catch(err => {
                          scaleDisplay.textContent = 'Failed to load manifest file.';
                          console.error(err);
                        });
                    
                      function loadScale(filename) {
                        fetch('../output/' + filename)
                          .then(res => res.json())
                          .then(scale => {
                            scaleDisplay.innerHTML = '';
                            drawCallback(scale);
                    
                      setupMidiInput(scale);
                     
                         console.log('scale.notes:', scale.notes)
                    
                         const buttonContainer = document.createElement('div');
                          buttonContainer.style.marginTop = '1em';
                    
                          scale.notes.forEach(note => {
                            const btn = document.createElement('button');
                            btn.textContent = note.frequency.toFixed(2) + ' Hz';
                            btn.style.margin = '4px';
                            btn.onclick = () => playNote(note.frequency);
                            buttonContainer.appendChild(btn);
                          });
                    
                          scaleDisplay.appendChild(buttonContainer);
                          })
                          .catch(err => {
                            scaleDisplay.textContent = 'Failed to load scale file.';
                            console.error(err);
                          });
                      }
                    }
                    ```

                `viewer/js/utils.js`
                ```js
                export async function loadScale(path) {
                  const res = await fetch(path);
                  if (!res.ok) throw new Error('Failed to load scale file');
                  return await res.json();
                }
                ```

            `viewer/style.css`
            ```css
            body {
              font-family: sans-serif;
              margin: 2rem;
              background: #f4f4f4;
            }
            
            canvas {
              border: 1px solid #ccc;
              background: #fff;
            }
            ```
