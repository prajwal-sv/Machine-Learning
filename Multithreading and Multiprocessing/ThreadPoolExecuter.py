#multithradding with Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)  # Simulate a time-consuming task
    return f"Number: {number}"

numbers = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 10]

with ThreadPoolExecutor(max_workers=3) as executor:
    results =executor.map(print_number, numbers) 

for result in results:
    print(result)
# Output will be printed as the threads complete their tasks

#Number: 1
#Number: 2
#Number: 3
#Number: 4
#Number: 5
#Number: 6
#Number: 7
#Number: 8
#Number: 9
#Number: 10