list_a = [1,2,3,4,5, 2, 2, 2]
list_b = [1,2,2,6,7,8,5]

res = []

for i in list_a:
    if i in list_b:
        res.append(i)

print(res)

