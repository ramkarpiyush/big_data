# Problem: Group the anagrams together.
# An anagram is a word formed by rearranging the letters of another word, using all original letters exactly once.

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagram_dict = {}
for word in words:
    # Create the sorted key
    sorted_word = ''.join(sorted(word))         # ''.join(...) → turns list into string
                                                # sorted() → gives list of sorted letters
    # Check if the key exists
    if sorted_word in anagram_dict:
        anagram_dict[sorted_word].append(word)
    else:
        anagram_dict[sorted_word] = [word]
print(anagram_dict)


def get_group_anagram(input_list):
    anagram_dict = {}
    for i in input_list:
        sorted_word = "".join(sorted(i))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(i)
        else:
            anagram_dict[sorted_word] = [i]
    return anagram_dict

print(get_group_anagram(words))


