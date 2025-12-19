
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

# Example
list1 = [1, [1, 2], 3, 4]
list2 = [1, [1,2], 3, [1,2,[1,2,3]], 4]
# print(get_flatten_list(list1))  # [1, 1, 2, 3, 4]

def get_flattened_list(nested):
    flat_list = []
    for i in nested:
        if type(i) is list:
            flat_list.extend(i)
        else:
            flat_list.append(i)
    return flat_list

# print(get_flattened_list(list2))
        


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
