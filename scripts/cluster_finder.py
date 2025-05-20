
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
