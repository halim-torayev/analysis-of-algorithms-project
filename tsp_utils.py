import random
import math

def generate_cities(n, size=100):
    return [(random.uniform(0, size), random.uniform(0, size)) for _ in range(n)]

def brute_force_tsp(cities):
    from itertools import permutations
    best = float('inf')
    n = len(cities)

    def dist(p1, p2):
        return math.dist(p1, p2)

    for perm in permutations(range(n)):
        length = 0
        for i in range(n):
            length += dist(cities[perm[i]], cities[perm[(i + 1) % n]])
        best = min(best, length)

    return best
