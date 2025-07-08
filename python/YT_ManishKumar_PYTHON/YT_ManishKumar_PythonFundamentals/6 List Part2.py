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

from loguru import logger

out = ['Piyush', 'Shivani', 'Akanksha', 'Piyus', '', 'S', 'ivani', 'Akanks', 'a']

for i in range(len(out)):
    print(i, out[i])

    logger.info(f"My name is {out[i]} and My AIR is {i}.")


n = 5

for i in range(n):
    print((i+1) * "#")


for i in range(5, 0, -1):
    print(i * "#")

rows = 4

for i in range(1, rows + 1):
    spaces = ' ' * (rows - i)
    hashes = '#' * (2 * i - 1)
    print(spaces + hashes)
