# Find the second largest number in the list
# if the list has fewer than two unique elements, return None.
# Dont use python built-in sorting functions e.g. sorted(), .sort()

# Example:
# input:
nums = [10, 4, 7, 9, 12]
# # Output:
# 10
# Explanation:
# The largest number is 12.
# The second largest distinct number is 10.


def second_largest_num(nums: list):
    nums = list(set(nums))
    if len(nums)<2:
        return None
    print(nums.sort())
    return nums[-2]

second_largest_num(nums=nums)
