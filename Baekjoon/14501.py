import sys
from itertools import combinations

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
revenue = 0
schedule = [0] * N
for i in range(1, N+1):
    n = list(combinations(arr, i))  # 원소가 i개인 조합을 모은 리스트 n
    for j in n:                     # n에 들어있는 각 리스트 j
        temp = 0
        schedule = [0] * N
        for k in len(j):                 # j에 담긴 리스트의 인덱스 번호 k
            print(k)
            if k[] + arr[k][0] < N:
                for s in range(k, k + arr[k][0]):
                    if s < N and schedule[s] == 0:
                        schedule[s] == 1
                else:
                    temp += arr[k][1]
        if temp > revenue:
            revenue = temp
print(revenue)
