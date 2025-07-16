
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
