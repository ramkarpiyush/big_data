_list = ["Piyush", "Shivani", "Akanksha"]
res = []

for i in _list:
    a = i.split('h')
    # res.append(a)
    res.extend(a)
# _list.append(res)

print(res)
_list.extend(res)
print(_list)



# out = ['Piyush', 'Shivani', 'Akanksha', 'Piyus', '', 'S', 'ivani', 'Akanks', 'a']