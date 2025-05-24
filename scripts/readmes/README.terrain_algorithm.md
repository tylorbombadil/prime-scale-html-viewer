# Core Terrain Algorithm – Step-by-Step with Explanations

---

1. **Generate Primes**  
   Get the first `N` primes.  
   → *These will be the source values that shape the scale.*

2. **Log-Reduce**  
   Map each prime into [0, 1] using base-2 log reduction.  
   → *This places them inside a single octave for comparison.*

3. **Build Linear Axis**  
   Create a uniformly spaced `x_axis` with `density_resolution + 1` points.  
   → *This defines where the algorithm will scan for prime influence.*

4. **Compute Density Map**  
   For each scan point `x`:  
   - Measure wrapped distance to each reduced prime.  
   - If within `window_size / 2`, apply a fading weight.  
   - Add all influences to compute total density at `x`.  
   → *This builds a terrain map showing where primes are most concentrated.*

5. **Segment and Select**  
   Split the axis into `num_notes` segments.  
   Pick the lowest (`valley`) or highest (`peak`) density point in each.  
   → *This extracts one musically significant note per region.*

6. **Add Bounds** *(optional)*  
   Include 0.0 and 1.0 if enabled.  
   → *This anchors the scale at the base and octave if desired.*

7. **Convert to Notes**  
   Turn selected `x` values into frequencies, MIDI notes, and cents.  
   → *This makes the data usable for sound generation or playback.*

8. **Export**  
   Output a note list and metadata block.  
   → *This preserves both the result and how it was generated.*
