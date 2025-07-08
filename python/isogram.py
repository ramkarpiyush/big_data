def is_isogram(input):
    res = {}
    for i in input:
        if i in res:
            return True
        else:
            res[i] = 1

    return 1

print(is_isogram('Machinei'))