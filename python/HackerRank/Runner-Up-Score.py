

n = 5
arr = "2 3 6 6 5"

arr_split = (arr.split(" "))

arr_list = [int(i) for i in arr.split()]

# arr_set = set(sorted(arr_list, reverse=True))

sorted_list = sorted(set(arr_list), reverse=True)
print(sorted_list[1])
# print(arr_list.sort(reverse=True))

# Problem:
# Find the Runner-Up-Score:
_n = int(input())                    # 5
_arr = map(int, input().split())     # 2 3 6 6 5

_res = sorted(set([i for i in _arr]), reverse=True)
print(_res[1])