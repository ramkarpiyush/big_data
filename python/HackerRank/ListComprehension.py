# Problem:

x = 1
y = 1
z = 2 
n = 3

# Solution 1:
# By using nested loops:
res = []
for i in range(0,x+1,1):
    for j in range(0,y+1,1):
        for k in range(0,z+1,1):
            if (i+j+k)!=n:
                res.append([i,j,k])
            else:
                continue
print(res)

# Solution 2:
# By using list comprehension
list_compre = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n]
print(list_compre)

