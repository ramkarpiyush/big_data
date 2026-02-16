# Input Format:
# The first line contains N. The second line contains an array A[] of  integers each separated by a space.
N = 5
A = [2, 3, 6, 6, 5]


tuple_a = sorted(tuple(A), reverse=True)
# print(tuple_a[1])

set_a = sorted(set(A), reverse=True)
# print(set_a[1])

def get_runnerup_score(n, A):
    A = list(map(int, A.split()))
    unique_scores = sorted(set(A), reverse=True)
    if n < 2:
        return unique_scores[0]
    else:
        return unique_scores[1]


A="2 3 6 6 5"
N=5
res = get_runnerup_score(n=N, A=A)
print(res)