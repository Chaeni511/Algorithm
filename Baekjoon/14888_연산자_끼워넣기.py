import sys
from itertools import permutations
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
O = list(map(int, sys.stdin.readline().split()))      # + _ * /
operator = []
for i in range(4):
    for j in range(O[i]):
        operator.append(i)

max_result = 0
min_result = 987654321
for i in permutations(operator):
    temp = A[0]
    for j in range(len(i)):
        if i[j] == 0:
            temp += A[j+1]
        elif i[j] == 1:
            temp -= A[j + 1]
        elif i[j] == 2:
            temp *= A[j + 1]
        else:
            if A[j + 1] > 0:
                temp //= A[j + 1]
            else:
                temp //= abs(A[j + 1])
                temp *= -1



    if temp > max_result:
        max_result = temp
    if temp < min_result:
        min_result = temp

print(max_result)
print(min_result)
