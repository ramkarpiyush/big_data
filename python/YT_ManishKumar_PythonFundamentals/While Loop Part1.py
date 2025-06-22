import time
from datetime import datetime

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0

while i < len(numbers):
    if numbers[i] % 2 != 0:
        print(f"{i} is odd number {datetime.now()}")
    elif numbers[i] % 2 == 0: 
        print(f"{i} is even number {datetime.now()}")
    elif numbers[i]>len(numbers):
        print("Numbers not available...")
    else:
        continue

    # time.sleep(5)
    i =i+1


