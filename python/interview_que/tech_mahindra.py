# find the pairs of indices whose elements sum is zero                                                                                       zero
list_1=[-6,0,10,-4,5,4,-10, 6]
# Output: [(0, 7), (2, 6), (3, 5)]

def get_zero_sum_index_pairs(list):
    pairs = []
    for i in range(len(list_1)):
        for j in range(i+1, len(list_1)):
            if list_1[i] + list_1[j] == 0:
                pairs.append((i, j))
    return pairs

print(get_zero_sum_index_pairs(list=list_1))




		