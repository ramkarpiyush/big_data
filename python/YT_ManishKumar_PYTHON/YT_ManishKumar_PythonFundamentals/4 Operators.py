from loguru import logger

'''
# Modulo Operator (%):
- The modulo operator (%) returns the remainder after dividing one number by another.
- In Python, modulo always gives a non-negative result when the divisor is positive even with negative numbers
'''
print(10 % 3)  # Output: 1
print(15 % 4)  # Output: 3
print(9 % 3)   # Output: 0
print(-10 % 3) # Output: 2


_res = 15%6
logger.info(_res)


'''
# Integer (Floor) Division (//):
- Integer division in Python is done using the // operator.
- It returns the largest whole number (integer) less than or equal to the result of division — also called the floor of the division.
- It divides two numbers and discards the decimal part.
'''
print(10 // 3)   # Output: 3       → 10 ÷ 3 = 3.33 → floor is 3
print(15 // 4)   # Output: 3       → 15 ÷ 4 = 3.75 → floor is 3
print(5 // 2)    # Output: 2       → 5 ÷ 2 = 2.5   → floor is 2
print(-10 // 3)  # Output: -4      → -10 ÷ 3 = -3.33 → floor is -4
print(10 // -3)  # Output: -4


import math

'''
# Ceiling Value:

'''
print(15/7)
print(math.ceil(15/7))          # math.ceil() returns the smallest integer greater than or equal to the number.
print(math.floor(15/7))         # math.floor() returns the largest integer less than or equal to the number.


'''
# truediv and floordiv operators:
'''

from operator import truediv, floordiv
a = 5
b = 3
import math
print(a / b)                # 2.5

print(truediv(a, b))        # 2.5

print(a // b)               # 2

print(floordiv(a, b))       # 2