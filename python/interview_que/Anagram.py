# Anagram:
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagram_dict = {}

for word in words:
    # Create the sorted key
    sorted_word = ''.join(sorted(word))         # ''.join(...) → turns list into string
                                                # sorted() → gives list of sorted letters
    print(sorted_word)

    # Check if the key exists
    if sorted_word in anagram_dict:
        anagram_dict[sorted_word].append(word)
    else:
        anagram_dict[sorted_word] = [word]
print(anagram_dict)


