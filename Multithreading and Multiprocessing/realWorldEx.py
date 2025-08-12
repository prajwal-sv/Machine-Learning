

import multiprocessing
import math
import sys
import time



#increse the maximum number of digits in an integer
#this is useful for large numbers in multiprocessing
sys.set_int_max_str_digits(100000)

#fuction to calculate the factorial of a number
def factorial(n):
    print(f"Calculating factorial of {n} in process {multiprocessing.current_process().name}")
    result = math.factorial(n)
    print(f"Factorial of {n} is {result} in process {multiprocessing.current_process().name}")
    return result

if __name__ == "__main__":
    # Create a list of numbers to calculate factorial
    numbers = [5, 10, 15, 20, 25]

    start_time = time.time()
    print("Starting factorial calculations...")

    # Create a pool of processes
    with multiprocessing.Pool() as pool:
        # Map the factorial function to the list of numbers
        results = pool.map(factorial, numbers)
    end_time = time.time()

    print("Factorial calculations completed.")
    print("Results:", results)

    print(f"Time taken: {end_time - start_time} seconds")
    print("Main process finished.")