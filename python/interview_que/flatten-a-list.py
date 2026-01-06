# Solution 1:
def flatten_list(nested):
    out = []
    for item in nested:
        if isinstance(item, list):              # change: recurse if it's a list
            out.extend(flatten_list(item))      # change: flatten deeper first
        else:
            out.append(item)
    return out
# The isinstance() function in Python is used to check 
# whether an object is an instance of a specific class or a tuple of classes.

# Solution 2:
def get_flatten_list2(nested):
    flat = []
    for item in nested:
        if type(item)==list:
            # Calls the same function recursively to flatten the nested item, 
            # then appends each element of the flattened result into flat.
            for sub in get_flatten_list2(item):
                flat.append(sub)
        else:
            # Not iterable -> treat as a scalar
            flat.append(item)
    return flat

###--- OR ---###

def get_flatten_list(nested):
    flat = []
    for item in nested:
        try:
            # Try to iterate; if item is a list (or other iterable), recurse
            for sub in get_flatten_list(item):
                flat.append(sub)
        except TypeError:
            # Not iterable -> treat as a scalar
            flat.append(item)
    return flat


# Solution 3:
def get_flattened_list3(nested):
    flat_list = []
    for i in nested:
        if type(i) is list:
            flat_list.extend(i)
        else:
            flat_list.append(i)
    return flat_list



list2 = [1, [1,2], 3, [1,2,[1,2,3]], 1]
list3 = [1, [1,2], 3, [1,2,[3, 4, 5]], 1, [1,2,[1,[1, 2, 2], 1]]]

print(flatten_list(list3))  
print(get_flatten_list(list3))
print(get_flatten_list2(list3))
print(get_flattened_list3(list3))


print("Test...")




