"""
TASK:
Reverse the list with the first character of each element capitalized,
and remove any duplicate
.

Codition: Without using reverse and capitalize function
"""

# SOlution:

data = ["sql", "scala", "pyTHon", "javA", "java" "pyspark"]

# Method 1:
# Step 1: Reverse list manually using slicing
reversed_data = data[::-1]

# Step 2: Remove duplicates while preserving order
unique_data = []
for item in reversed_data:
    if item.lower() not in unique_data:
        unique_data.append(item)

# Step 3: Capitalize first letter manually (without using capitalize())
final_data = []
for word in unique_data:
    formatted = word[0].upper() + word[1:].lower()
    final_data.append(formatted)

print(final_data)

#==================================================================================================#
# Method 2:
def list_reverse(l): 
    n = len(l)-1
    rev = []
    for i in range(n,-1,-1):
        char = l[i][0].upper() + l[i][1:].lower()
        if char not in rev: 
            rev.append(char)

    print(rev)

list_reverse(data)