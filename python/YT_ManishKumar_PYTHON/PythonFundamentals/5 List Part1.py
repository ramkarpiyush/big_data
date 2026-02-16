
'''
# List:
- List is a built-in (mutable, ordered) collection of items. 
- Lists can hold elements of different data types and are defined using square brackets [].
- List can contain duplicate items.
- List in Python are Mutable. Hence, we can modify, replace or delete the items.
- List are ordered. It maintain the order of elements based on how they are added.
- Accessing items in List can be done directly using their position (index), starting from 0.
'''

from loguru import logger

# Common List Operations:

# 1. Create a list	
my_list = [10, 20, 30]	        # Define a list
print("my_list", my_list)

# 2. Access element	
nth_num = my_list[0]	        # Get first item (indexing starts at 0)
print("Nth element from my_list:", nth_num)

# 3. Negative index	
last_num = my_list[-1]	        # Get last item
print(f"Last num is {last_num}")

# 4. Slice list	
"""
The syntax for slicing is:
string[start:stop:step]
where,
    start: where the slice starts (default is 0 if not specified).
    stop: where the slice ends (not included).
    step: how many characters to move forward (or backward if negative).
            e.g. -1 → means move one step backward.
"""
sublist = my_list[1:3]	        # Get sublist [20, 30]
print(f"Slice list: {sublist}")

# Reverse each element in a list and make a new list
list = ["SQL", "Python", "Databricks", "AWS", "Spark"]
new_list = []
for i in list:
    print(i[::-1])

# 5. Modify element	
my_list[0] = 99	                # Change item at index 0
print(my_list)

# 6. Append element: 
# Adds a single element to the end of the list.
# It modifies the list in place, It returns None
# Adds x as a single item to the end of the list. 
# If x is a list, it adds the whole list as one element (nested list).
app_list = [10, 20]
app_list.append(40)	            # Add item to end
print(f"Output: append 40 in my_list= {app_list}")

nw_ls = [100, 200]
app_list.append(nw_ls)
print(app_list)	

# list.extend(iterable):
# Adds each element of iterable individually to the list (flattens one level).
# Adds multiple elements from an iterable (like a list, tuple, set) to the end of the list.
ex_list = ["Impetus", "Python"]
names = ["Piyush", "Dell"]

ex_list.extend(names)
print(ex_list)

# Insert at index [list.insert(i, x)]:
my_list.insert(1, 15)	        # Add item at specific position
print("Insert at index:", my_list)

# Note: all three methods — append(), extend(), and insert() — 
# modify the list in-place, and they all return None.


# Remove by value [list.remove(x)]:
my_list.remove(20)	            # Remove first matching value

del my_list[2]	                # Delete item at index
print("updated_list:", my_list)

# Remove all items from the list:
list_ = [1, 2, 3, 4, 5]
print(list_)
list_.clear()
print(list_)

# Pop element:	
# Syntax: list.pop(index)       
# index (optional): Position of the element to remove.
# If no index is given, pop() removes the last element.

item = my_list.pop()            # Remove and return last item
print("Pop element:", item)

numbers = [10, 20, 30, 40]
# Remove last element
removed = numbers.pop()
print(removed)      # 40
print(numbers)      # [10, 20, 30]

# Remove element at index 1
removed = numbers.pop(1)
print(removed)      # 20
print(numbers)      # [10, 30]


# Length of list	
len_list = len(my_list)	        # Count of items
len_list2 = len(my_list)+1	    # Count of items

print(f'''Length of len_list: {len_list} 
Length of len_list2: {len_list2}''')

# Check existence:	
num = 10
chk_list = num in my_list	    # Returns True if 10 is in list
print(f"Check {num} in my_list: {chk_list}")

# Loop through list	
for item in my_list:
    print(item)	                # Iterate over elements

'''
# list.sort(*, key=None, reverse=False):	
- Parameters:
    key: (Optional) A function to customize the sort order (e.g., key=str.lower to sort case-insensitively).
    reverse: (Optional) If True, sorts the list in descending order. Default is False (ascending).
- list.sort() method in Python, which is used to sort a list in-place (i.e., it modifies the original list).
- This method modifies the original list and returns None.

'''
_list = [10, 20, 30, 5, -75]

_list.sort()                    # Sort in ascending order
print(_list)

_list.sort(key= None, reverse= True)
print(_list)

'''
# sorted(iterable, *, key=None, reverse=False):

- Parameter	:
    iterable: The data to be sorted (e.g., list, tuple, set, dict, string).
    key	(Optional): A function that serves as a sort key.
    reverse	(Optional): If True, the list is sorted in descending order. Default is False.

- Returns a new sorted list, leaving the original unchanged.
- Works on: Any iterable (lists, tuples, sets, dict keys).    
'''
sorted_fun = sorted(_list)
print(sorted_fun)

print(sorted(_list, reverse= True))

names = ["Alice", "bob", "Charlie", "Piyush"]
result = sorted(names)
print(result)      # Output: ['Alice', 'Charlie', 'bob']

# Sort case-insensitively:
result = sorted(names, key=str.lower)
print(result)      # Output: ['Alice', 'bob', 'Charlie']

# Sort by length of strings:
result = sorted(names, key=len)
print(result)



# Reverse list	
_list.reverse()	            # Reverse the list in place
print(_list)

'''
# list.index(x[, start[, end]]):
- The list.index() method in Python is used to find the index of the first occurrence of an element in a list.
- Return zero-based index in the list of the first item whose value is equal to x. 
- Raises a ValueError if there is no such item.
- Parameters:
    x: The value to search for.
    start (optional): The index to start searching from.
    end (optional): The index to stop searching (exclusive).
'''
list_num = [3, 4, 5, 0, 1, 2, 5, 6, 7, 8, 9, 10]
out = list_num.index(21)
print(out)             # output: ValueError: 21 is not in list

list_num = [3, 4, 5, 0, 1, 2, 5, 6, 7, 8, 9, 10]
out = list_num.index(1)
print(out)             # output: 4

list_num = [3, 4, 5, 0, 1, 2, 5, 6, 7, 8, 9, 10]
out2 = list_num.index(1, 5, 10)
print(out2)            # output: ValueError: 1 is not in list

list_num = [3, 4, 5, 0, 1, 2, 5, 6, 7, 8, 9, 10]
out2 = list_num.index(5, 5, 10)
print(out2)            # output: 6

# list.count(x): Return the number of times x appears in the list
list_num = [3, 4, 5, 4, 1, 2, 5, 6, 7, 8, 9, 10, 4]
print(list_num.count(4))        # output: 3





# Split method:


