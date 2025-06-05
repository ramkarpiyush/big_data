"""
You are given a list of strings, create a program that groups anagrams together. 
An anagram is a word formed by rearranging the letters of another word. 
For example the string ‘row’ has the following anagrams: ‘rwo’, ‘orw’, ‘owr’, ‘wor’, ‘wro’
Example:
Input: ["row", "a", "wor", "test", "ttes", "tset"]
Output: [["row", "wor"], ["a"], ["test", "ttes", "tset"]]
"""

def group_anagrams(words):
    anagram_dict = {}  
    
    for word in words:
        # Create the sorted key
        sorted_word = ''.join(sorted(word))
        print(sorted_word)
        # Check if the key exists
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    
    return list(anagram_dict.values())

# Example usage
input_words = ["row", "a", "wor", "test", "ttes", "tset"]
output = group_anagrams(input_words)
print(output)

