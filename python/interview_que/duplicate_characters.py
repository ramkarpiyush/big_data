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
print(emp_dic)

# Solution 1:
res = []
for i,j in emp_dic.items():
    if j>1:
        print(f"{i}: {j}")
        res.append(i)
print(res)
print(", ".join(res))

# OR

filtered = {key for key, value in emp_dic.items() if value > 1}
print(", ".join(filtered))


# Solution 2:        
duplicate_dic = {}
for i in emp_dic:
    if emp_dic[i]>1:
        duplicate_dic[i]=emp_dic[i]
print(duplicate_dic)
            
# Approach 2: Using a set while scanning 

def duplicates_set_scan(s: str):
    seen = set()   # characters seen at least once
    added = set()  # duplicates we've already appended to result
    dupes = []     # output list of duplicates in "second-occurrence" order

    for ch in s:
        if ch in seen:              # We've seen this character before → it's a duplicate now.
            if ch not in added:
                dupes.append(ch)    # record the character once
                added.add(ch)       # mark it as recorded
        else:
            # First time we see this character
            seen.add(ch)

    return dupes

# Example
s = "programming"
print(", ".join(duplicates_set_scan(s)))  # Output: r, m, g

