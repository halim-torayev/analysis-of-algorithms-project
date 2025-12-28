from tsp_utils import generate_cities, brute_force_tsp
from aco import ant_colony_optimization
from sa import simulated_annealing

def run():
    instances = {
        "Small (8 cities)": 8,
        "Medium (30 cities)": 30,
        "Large (60 cities)": 60
    }

    for name, n in instances.items():
        print(f"\n{name}")
        cities = generate_cities(n)

        if n <= 8:
            optimal = brute_force_tsp(cities)
            print(f"Optimal (brute force): {optimal:.2f}")
        else:
            optimal = None

        aco_tour, aco_len, aco_time = ant_colony_optimization(cities)
        print(f"ACO -> Length: {aco_len:.2f}, Time: {aco_time:.2f}s")

        sa_tour, sa_len, sa_time = simulated_annealing(cities)
        print(f"SA  -> Length: {sa_len:.2f}, Time: {sa_time:.2f}s")

        if optimal:
            print(f"ACO ratio: {aco_len / optimal:.2f}")
            print(f"SA ratio : {sa_len / optimal:.2f}")

if __name__ == "__main__":
    run()
