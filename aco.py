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

def ant_colony_optimization(cities, n_ants=20, n_iter=100, alpha=1, beta=5, rho=0.5):
    n = len(cities)
    pheromone = [[1.0 for _ in range(n)] for _ in range(n)]
    best_tour = None
    best_length = float('inf')

    start_time = time.time()

    for _ in range(n_iter):
        all_tours = []
        all_lengths = []

        for _ in range(n_ants):
            start = random.randint(0, n - 1)
            tour = [start]
            unvisited = set(range(n))
            unvisited.remove(start)

            while unvisited:
                current = tour[-1]
                probs = []
                total_prob = 0

                for city in unvisited:
                    tau = pheromone[current][city] ** alpha
                    eta = (1 / distance(cities[current], cities[city])) ** beta
                    prob = tau * eta
                    probs.append((city, prob))
                    total_prob += prob

                r = random.uniform(0, total_prob)
                cumulative = 0
                for city, prob in probs:
                    cumulative += prob
                    if cumulative >= r:
                        next_city = city
                        break

                tour.append(next_city)
                unvisited.remove(next_city)

            length = total_distance(tour, cities)
            all_tours.append(tour)
            all_lengths.append(length)

            if length < best_length:
                best_length = length
                best_tour = tour

        # Evaporation
        for i in range(n):
            for j in range(n):
                pheromone[i][j] *= (1 - rho)

        # Reinforcement (best tour only)
        for i in range(len(best_tour)):
            a = best_tour[i]
            b = best_tour[(i + 1) % n]
            pheromone[a][b] += 1 / best_length
            pheromone[b][a] += 1 / best_length

    runtime = time.time() - start_time
    return best_tour, best_length, runtime
