numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

emp = []
emp2 = []

for i in numbers:
    if i%2==0:
        print("even")
        emp.append(i)
        emp2.extend([i])
    else:
        print("odd")

print(emp)
print(emp2)   

# Method 2:
new_list = []
new_list = [i for i in range(1, 11) if i%2==0]
print(new_list)


# Method 1:
new_list2 = []
for i in range(1, 11):
    if i%2 == 0:
        new_list2.append("Even")
    else:
        new_list2.append("Odd")
    
print(new_list2)

# Method 2:
new_list2 = []

new_list2= ["Even" if i%2==0 else "Odd" for i in range(1, 11)]
print(new_list2)