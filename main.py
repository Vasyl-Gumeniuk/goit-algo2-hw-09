import random
import math
from typing import List, Tuple, Callable

# Функція Сфери для мінімізації
def sphere_function(x: List[float]) -> float:
    """
    Обчислює значення функції Сфери для заданої точки.
    """
    return sum(xi ** 2 for xi in x)

# Алгоритм підйому на гору
def hill_climbing(func: Callable[[List[float]], float], bounds: List[Tuple[float, float]], 
                  iterations: int = 1000, epsilon: float = 1e-6) -> Tuple[List[float], float]:
    """
    Реалізація алгоритму підйому на гору для мінімізації функції.
    """
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)
    
    for _ in range(iterations):
        neighbor = [current[i] + random.uniform(-0.1, 0.1) for i in range(len(bounds))]
        neighbor = [max(min(neighbor[i], bounds[i][1]), bounds[i][0]) for i in range(len(bounds))]
        neighbor_value = func(neighbor)
        
        if abs(current_value - neighbor_value) < epsilon:
            break
        
        if neighbor_value < current_value:
            current, current_value = neighbor, neighbor_value
    
    return current, current_value

# Алгоритм випадкового локального пошуку
def random_local_search(func: Callable[[List[float]], float], bounds: List[Tuple[float, float]], 
                        iterations: int = 1000, epsilon: float = 1e-6) -> Tuple[List[float], float]:
    """
    Реалізація випадкового локального пошуку для мінімізації функції.
    """
    best = [random.uniform(b[0], b[1]) for b in bounds]
    best_value = func(best)
    
    for _ in range(iterations):
        candidate = [random.uniform(b[0], b[1]) for b in bounds]
        candidate_value = func(candidate)
        
        if abs(best_value - candidate_value) < epsilon:
            break
        
        if candidate_value < best_value:
            best, best_value = candidate, candidate_value
    
    return best, best_value

# Алгоритм імітації відпалу
def simulated_annealing(func: Callable[[List[float]], float], bounds: List[Tuple[float, float]], 
                        iterations: int = 1000, temp: float = 1000, cooling_rate: float = 0.95, 
                        epsilon: float = 1e-6) -> Tuple[List[float], float]:
    """
    Реалізація алгоритму імітації відпалу для мінімізації функції.
    """
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)
    
    for _ in range(iterations):
        temp *= cooling_rate
        if temp < epsilon:
            break
        
        neighbor = [current[i] + random.uniform(-0.1, 0.1) for i in range(len(bounds))]
        neighbor = [max(min(neighbor[i], bounds[i][1]), bounds[i][0]) for i in range(len(bounds))]
        neighbor_value = func(neighbor)
        
        if neighbor_value < current_value or random.uniform(0, 1) < math.exp((current_value - neighbor_value) / temp):
            current, current_value = neighbor, neighbor_value
    
    return current, current_value

if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]
    
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)
    
    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)
    
    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
