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
