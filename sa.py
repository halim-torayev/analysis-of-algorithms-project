import random
import math
import time

def distance(p1, p2):
    return math.dist(p1, p2)

def total_distance(tour, cities):
    dist = 0
    for i in range(len(tour)):
        dist += distance(cities[tour[i]], cities[tour[(i + 1) % len(tour)]])
    return dist

def simulated_annealing(cities, T0=1000, Tmin=1e-3, alpha=0.995, iters_per_T=100):
    n = len(cities)
    current = list(range(n))
    random.shuffle(current)
    current_cost = total_distance(current, cities)

    best = current[:]
    best_cost = current_cost

    T = T0
    start_time = time.time()

    while T > Tmin:
        for _ in range(iters_per_T):
            i, j = sorted(random.sample(range(n), 2))
            new = current[:]
            new[i:j] = reversed(new[i:j])
            new_cost = total_distance(new, cities)

            delta = new_cost - current_cost

            if delta < 0 or random.random() < math.exp(-delta / T):
                current = new
                current_cost = new_cost

                if current_cost < best_cost:
                    best = current[:]
                    best_cost = current_cost

        T *= alpha

    runtime = time.time() - start_time
    return best, best_cost, runtime
