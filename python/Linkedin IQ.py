# 1. Find the last name from from full name 
full_name = "Name Middle Surname"

_a = full_name.split()[-1]
print(_a)


# 2. Find last word from a list
list = ["SQL", "Python", "Databricks", "AWS", "Spark"]

last_word = list[-1]
print(last_word)

# 3. Find vowels in each word from a list
list = ["SQL", "Python", "Databricks", "AWS", "Spark"]
vowels = "aeiou"

# Method 1
for i in list:
    for k in i.lower():
        if k in vowels:
            print(k)
        else:
            pass

# Method 2
for i in list:
    for alpha in i.lower():
        if alpha in vowels:
            print(alpha)

    print()

# 4. Reverse each element in a list and make a new list
list = ["SQL", "Python", "Databricks", "AWS", "Spark"]

# Methos 1
new_list = []
for i in list:
    new_list.append(i[::-1])

print(new_list)

# Method 2
reversed_word = [i[::-1] for i in list]
print(reversed_word)

# 5. Find a first vowel and its index
word = "Piyush"
vowels = "aeiou"

# Method 1:
for i in word.lower():
    if i in vowels:
        _index = word.index(i)
        print(i, _index)
        break
        
# Method 2:
for i, j in enumerate(word):
    if j in vowels:
        print(i,j)
        break

# Method 3:
word = "Piyush"
vowels = "aeiou"
list = []

for i,j in enumerate(word):
    if j in vowels:
        list.append((i,j))
        break
print(list)

# Method 4:
word = "Piyush"
vowels = "aeiou"
dic = {}

for i in range(len(word)):
    alpha = word[i]
    if alpha in vowels:
        dic[alpha] = i
        break

print(dic)

# Method 5:
dic2 = {}
for i in range(len(word)):
    alpha = word[i]
    if alpha in vowels:
        if alpha in dic2:
            dic2[alpha].append(i)
        else:
            dic2[alpha] = i
        break

print(dic2)


# 6. Find word in sentence and count repetitions
sentence = "Data is power. Data drives decisions. Data matters"
res = {}

for i in sentence.split():
    if i in res:
        res[i] +=1
    else:
        res[i] = 1

print(res)

def word_count(sentence):
    res = {}
    for i in sentence.split():
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    result = print(res)
    return result

word_count("Data is a new oil, Data is evrywhere")