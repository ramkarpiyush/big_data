# Move all zeroes to end of array using Two-Pointers:
# Input: 
arr=[8, 9, 0, 1, 2, 0, 3]
# Output: [8, 9, 1, 2, 3, 0, 0]


### [Naive Approach] Using Temporary Array - O(n) Time and O(n) Space
# The idea is to create a temporary array of same size as the input array arr[].
# Approach:
# 1. First, copy all non-zero elements from arr[] to the temporary array.
# 2. Then, fill all the remaining positions in temporary array with 0.
# 3. Finally, copy all the elements from temporary array to arr[].

def pushZerosToEnd(arr):
    n = len(arr)
    temp = [0] * n  
    j = 0    # to keep track of the index in temp[]

    # Copy non-zero elements to temp[]
    for i in range(n):
        if arr[i] != 0:
            temp[j] = arr[i]
            j += 1

    # Fill remaining positions in temp[] with zeros
    while j < n:
        temp[j] = 0
        j += 1

    # Copy all the elements from temp[] to arr[]
    for i in range(n):
        arr[i] = temp[i]

if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    pushZerosToEnd(arr)

    for num in arr:
        print(num, end=" ")


# Two-pointer (write index) — In-place, Stable
# Scan the array, write non-zero elements forward, then fill the remainder with zeros.
def move_zeros_end(nums):
    write = 0
    for read in range(len(nums)):

        if nums[read] != 0:
            nums[write] = nums[read]    # modifies the list in place.
                                        # we overwrite the element at index write with the value from index read.
            write += 1

    # Fill the rest with zeros
    for i in range(write, len(nums)):
        nums[i] = 0
    return nums
# Example
arr = [0, 1, 0, 3, 12]
move_zeros_end(arr)
print(arr)  # [1, 3, 12, 0, 0]

