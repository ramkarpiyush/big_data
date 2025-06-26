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
string = "AbCabXYZbbccc"
count = {}

input = string.lower()

for i in input:
    if i in count:
        count[i] = count[i]+1
    else:
        count[i] = 1

print(count)

