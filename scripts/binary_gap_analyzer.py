
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
