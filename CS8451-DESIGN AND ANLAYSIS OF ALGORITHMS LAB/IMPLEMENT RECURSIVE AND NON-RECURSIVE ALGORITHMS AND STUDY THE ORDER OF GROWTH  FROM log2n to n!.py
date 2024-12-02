import time
import math

# Recursive Algorithm
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive_factorial(n - 1)

# Non-Recursive Algorithm
def non_recursive_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Measure time complexity
def measure_time_complexity(algorithm, n):
    start_time = time.time()
    algorithm(n)
    end_time = time.time()
    return end_time - start_time

# Main program
for i in range(1, 6):
    n = int(math.pow(2, i))
    recursive_time = measure_time_complexity(recursive_factorial, n)
    non_recursive_time = measure_time_complexity(non_recursive_factorial, n)
    print(f"n = 2^{i}")
    print(f"Recursive Time: {recursive_time}")
    print(f"Non-Recursive Time: {non_recursive_time}")
    print("------")
