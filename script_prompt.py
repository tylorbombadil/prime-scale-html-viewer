"""
Prime Scale App – CLI Entry Point

Usage (run from project root):
  python -m scripts.main --scale-type terrain ...
  python -m scripts.main --scale-type gap ...
  python -m scripts.main --scale-type pure ...
"""
#comment hashes are used to toggle between different implementations
import argparse
#from scripts.core_terrain_scale import generate_terrain_scale
from scripts.gap_threshold_scout import scan_thresholds
from scripts.core_pure_prime_scale import generate_pure_prime_scale
from scripts.core_terrain_scale_modified import generate_terrain_scale

def main():
    parser = argparse.ArgumentParser(description="Prime Scale Generator CLI")
    subparsers = parser.add_subparsers(dest="scale_type", required=True, help="Scale type to generate")

    # Terrain scale CLI
    terrain_parser = subparsers.add_parser("terrain", help="Generate terrain-based scale")
    terrain_parser.add_argument("--prime-count", type=int, default=1000)
    terrain_parser.add_argument("--base-frequency", type=float, default=220.0)
    terrain_parser.add_argument("--num-notes", type=int, default=8)
    terrain_parser.add_argument("--window-size", type=float, default=0.007)
    terrain_parser.add_argument("--density-resolution", type=int, default=4000)
    terrain_parser.add_argument("--mode", choices=["valley", "peak"], default="valley")
    terrain_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
    terrain_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
    terrain_parser.add_argument("--weight-curve", type=float, default=1.0)
    terrain_parser.set_defaults(include_bounds=True)

    # Gap scale CLI
    gap_parser = subparsers.add_parser("gap", help="Generate gap-based scale")
    gap_parser.add_argument("--prime-count", type=int, required=True)
    gap_parser.add_argument("--base-frequency", type=float, default=220.0)
    gap_parser.add_argument("--threshold-range", nargs=2, type=float, required=True, metavar=("MIN", "MAX"))
    gap_parser.add_argument("--step-size", type=float, default=0.001)
    gap_parser.add_argument("--note-goal", type=int, required=True)
    gap_parser.add_argument("--tolerance", type=int, default=1)
    gap_parser.add_argument("--density-resolution", type=int, default=4000)
    gap_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
    gap_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
    gap_parser.set_defaults(include_bounds=True)

    # Pure scale CLI
    pure_parser = subparsers.add_parser("pure", help="Generate raw prime scale")
    pure_parser.add_argument("--prime-count", type=int, required=True)
    pure_parser.add_argument("--base-frequency", type=float, default=220.0)
    pure_parser.add_argument("--density-resolution", type=int, default=4000)
    pure_parser.add_argument("--include-bounds", dest="include_bounds", action="store_true")
    pure_parser.add_argument("--no-include-bounds", dest="include_bounds", action="store_false")
    pure_parser.set_defaults(include_bounds=True)

    args = parser.parse_args()

    if args.scale_type == "terrain":
        generate_terrain_scale(
            prime_count=args.prime_count,
            base_frequency=args.base_frequency,
            num_notes=args.num_notes,
            window_size=args.window_size,
            density_resolution=args.density_resolution,
            mode=args.mode,
            include_bounds=args.include_bounds,
            weight_curve=args.weight_curve
        )

    elif args.scale_type == "gap":
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

    elif args.scale_type == "pure":
        generate_pure_prime_scale(
            prime_count=args.prime_count,
            base_frequency=args.base_frequency,
            include_bounds=args.include_bounds,
            density_resolution=args.density_resolution
        )

if __name__ == "__main__":
    main()
