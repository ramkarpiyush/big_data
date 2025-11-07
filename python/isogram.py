# ISOGRAM:
# An isogram is a word or phrase with no repeating letters — each letter appears only once.

# Method 1: Using a Dictionary
def is_isogram_dic(input)-> bool:
    print(f"Function name: {is_isogram_dic}")   
    res = {}
    for i in input.lower():
        if i.isalpha():    
            if i in res:
                return False
            else:
                res[i]=True     # It just means we’re recording that this character was seen.

    return True                 # The final return True happens only if no duplicate was found.

print(is_isogram_dic('machine'))

"""
# Case 1: with res[i] = True
This means:
- You are adding an entry to your dictionary.
- It does not stop the function — the loop continues to check other characters.

# Case 2: with return True
That means:
- The function immediately exits and returns True right there.
- The rest of the string will never be checked.
"""
from loguru import logger

# Method 2: Using a Set
def is_isogram_set(input: str)-> bool:

    print(f"Function name: {is_isogram_set.__name__}")
    logger.info(type(input).__name__)
    
    res = set()
    for i in input.lower():
        if i.isalpha():    
            if i in res:
                return False
            else:
                res.add(i)
    
    return True

print(is_isogram_set('Data'))


"""
Case 1 — Directly printing the function
This prints the function object itself — including its memory address — not just the plain name.

Case 2 — Using is_isogram_set.__name__
This gives you only the function name as a clean string, not the memory address or the <function ...> wrapper.

# Why __name__ exists?
    __name__ is a special built-in attribute in Python that stores the identifier name of the function or module.

"""