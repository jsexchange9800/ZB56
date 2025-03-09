import time
import random

def run_benchmark():
    """ تست عملکرد سیستم """
    start_time = time.time()
    random_numbers = [random.randint(1, 1000000) for _ in range(1000000)]
    random_numbers.sort()
    end_time = time.time()
    print(f"Benchmark completed in {end_time - start_time} seconds.")

if __name__ == "__main__":
    run_benchmark()
