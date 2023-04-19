# 부분수열의 합
import sys
from itertools import combinations
N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in range(1, N+1):
    n = list(combinations(arr, i))
    for j in range(len(n)):
        if sum(n[j]) == S:
            cnt += 1
print(cnt)

'''
5 0
-7 -3 -2 5 8

[(-7,), (-3,), (-2,), (5,), (8,)]
[(-7, -3), (-7, -2), (-7, 5), (-7, 8), (-3, -2), (-3, 5), (-3, 8), (-2, 5), (-2, 8), (5, 8)]
[(-7, -3, -2), (-7, -3, 5), (-7, -3, 8), (-7, -2, 5), (-7, -2, 8), (-7, 5, 8), (-3, -2, 5), (-3, -2, 8), (-3, 5, 8), (-2, 5, 8)]
[(-7, -3, -2, 5), (-7, -3, -2, 8), (-7, -3, 5, 8), (-7, -2, 5, 8), (-3, -2, 5, 8)]
[(-7, -3, -2, 5, 8)]
'''