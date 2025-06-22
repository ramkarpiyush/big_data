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