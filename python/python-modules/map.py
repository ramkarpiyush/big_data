# map() function:
# map() is a built-in function that:
# Applies a function to each item of an iterable (like list, tuple, etc) and returns a map object (iterable).
# 
# Syntax:
# map(function, iterable)
# 

arr = input()
# print(type(arr))        #  The input() function always returns a string by default
# print(arr)
# Input: 2 3 6 6 5
# Output: 
# <class 'str'>
# 2 3 6 6 5

arr = input().split()
# print(arr)
# Input: 2 3 6 6 5
# Output: ['2', '3', '6', '6', '5']
# 
# Convert input string into a list of strings

arr = map(int, input().split())
# print(arr)
# Input: 2 3 6 6 5
# Output: <map object at 0x000001753BEAF190>
# 
# Applies int() to each element
# Convert strings to integers
# map() does not return a list. It returns a map object (iterator)
# 
# arr is an object in memory
# 0x000001753BEAF190 is its memory address
# 
# A map object does not store all values
# It generates values one by one when needed
# This is called lazy evaluation


# Example:
a = [1, 2, 3]
b = [4, 5, 6]

res = map(lambda x,y: x+y, a, b)
print(res)              # <map object at 0x000002338A0D4D00>
print(list(res))        # [5, 7, 9]



res = []
for i in range(len(a)):
    res.append(a[i] + b[i])
print(res)              # [5, 7, 9]
