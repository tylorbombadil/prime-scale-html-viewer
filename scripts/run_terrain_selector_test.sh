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
