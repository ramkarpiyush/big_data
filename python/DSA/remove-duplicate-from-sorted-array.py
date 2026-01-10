# Remove Duplicate from Sorted Array
# Input:
nums = [1, 1, 2]
# Output: 2
#
# Array is sorted
# All duplicate are adjacent
# We must do it in-place (no extra array)

def remove_duplicate(nums):
    if not nums:
        return 0
    
    k = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[k]:
            k = k+1
            nums[k] = nums[i]
    return k+1

print(remove_duplicate(nums=nums))
# print(nums)