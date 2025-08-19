from concurrent.futures import ProcessPoolExecutor
import time




def square_number(number):
    time.sleep(1)  # Simulate a time-consuming task
    return number * number
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)

    for result in results:
        print(result)# Output will be printed as the processes complete their tasks



# Output:# 1
# 4
# 9
# 16    
# 25
# 36
# 49
# 64
# 81
# 100   
