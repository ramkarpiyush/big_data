arr = [1, 2, 3, 4, 5, 6, 7]
import time

def get_sum(arr):
    start = time.process_time()
    total_sum = 0
    iteration = 0
    for i in arr:
        iteration = iteration+1
        print("iteration",iteration)
        total_sum= total_sum+i
    end =  time.process_time()    
    return total_sum, f"{end-start:.2f}"

# print(get_sum(arr=arr))

# print(arr[0])

arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 11, 12]
target_ele = 2

def linear_search(arr, target):
    iteration = 0
    for i in range(len(arr)):
        iteration = iteration+1
        print("iteration", iteration)
        if arr[i] == target:
            return i
        
# print(linear_search(arr2, target_ele))

transactions = [101, 203, 101, 405, 203]

def get_duplicate_nums(nums):
    duplicate = []
    iteration = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            iteration=iteration+1
            print("iteration", iteration)
            if nums[i] == nums[j]:
                duplicate.append((i,j))

    return duplicate

# print(get_duplicate_nums(transactions))




def binary_search(_list, target):
    left = 0
    iteration = 0
    right = len(_list)-1

    while left<=right:
        iteration = iteration+1
        print("iteration", iteration)
        
        mid = (left+right)//2

        if _list[mid] == target:
            return mid
        elif _list[mid]<target:
            left=mid+1
        else:
            right=mid-1

_list = [1,3,5,7,8,10,13,20,21,30,33,40,50,70,90]
print(binary_search(_list,20))


