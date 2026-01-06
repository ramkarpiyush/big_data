# Find the count of each alphabet in the input string

Input = "My Name Is Piyush"

ls = []
for i in Input.upper():
    if i == " ":
        pass
    if i.isalpha():
        ls.append(i)
    else:
        pass

print(ls)

count_dict = {}

for i in ls:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1

print(count_dict)        

# Method 2:
string = "My Name Is Piyush" # "AbCabXYZbbccc"
count = {}

input = string.lower()

for i in input:
    if i in count:
        count[i] = count[i]+1
    else:
        count[i] = 1

print(count)


# Method 3:
print("Method 3:")
_data = "#Big Data Engineering @123"

print(len(_data))

empty_dic = {}
"""
for i in _data.lower():
    if i in empty_dic:
        empty_dic[i]= empty_dic[i]+1
    else:
        empty_dic[i] = 1

for i in _data.lower():
    if i in empty_dic:
        empty_dic[i]= empty_dic[i]+1
    else:
        empty_dic[i] = 1
"""
_data = "#Big Data Engineering @123"
        
for i in _data.lower():
    if i.isalpha():
        if i in empty_dic:
            empty_dic[i]=empty_dic[i]+1
        else:
            empty_dic[i]=1
    else:
        continue

print(empty_dic)