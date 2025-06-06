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
sublist = my_list[1:3]	        # Get sublist [20, 30]
print(f"Slice list: {sublist}")

# 5. Modify element	
my_list[0] = 99	                # Change item at index 0
print(my_list)

# 6. Append element	
my_list.append(40)	            # Add item to end
print(f"Output: append 40 in my_list= {my_list}")

# Insert at index	
my_list.insert(1, 15)	        # Add item at specific position
print("Insert at index:", my_list)

# Remove by value	
my_list.remove(20)	            # Remove first matching value

del my_list[2]	                # Delete item at index
print("updated_list:", my_list)

# Pop element	
item = my_list.pop()            # Remove and return last item
print("Pop element:", item)

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

# Sort list	
_list = [10, 20, 30, 5, -75]
_list.sort()                    # Sort in ascending order
print(_list)

sorted_fun = sorted(_list)
print(sorted_fun)

# Reverse list	
_list.reverse()	            # Reverse the list in place
print(_list)

