_list = ["Piyush", "Ramkar", 30, "12-03-1995", "Pune", 177.50, 87.50]

print(_list)

for i in _list:
    print(f"Data Type of _list element {i} is {type(i)}")



from datetime import date, time, datetime

dob = date(1995, 3, 12)
_list2 = ["Piyush", "Ramkar", 30, dob, "Pune", 177.50, 87.50]
for i in _list2:
    print(f"Data Type of _list element {i} is {type(i)}")


from datetime import date, time, datetime

dob2 = datetime.strptime('12-03-1995', '%d-%m-%Y').date()
print(dob2)               # 1995-03-12
print(type(dob2))         # <class 'datetime.date'>
