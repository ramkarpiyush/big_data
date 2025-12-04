# Duplicate Characters:
# Find and print all duplicate characters in a string.

"""
Input:  "programming"
Output: g, r, m
"""

input = "programming"

emp_dic = {}

for i in input.lower():
    if i.isalpha():
        if i in emp_dic:
            emp_dic[i]=emp_dic[i]+1
        else:
            emp_dic[i]=1

# Solution 1:
for i,j in emp_dic.items():
    if j>1:
        print(f"{i}: {j}")
        
# Solution 2:        
duplicate_dic = {}
for i in emp_dic:
    if emp_dic[i]>1:
        duplicate_dic[i]=emp_dic[i]
print(duplicate_dic)
            