import sys
from collections import Counter

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline())for _ in range(N)]
arr.sort()

# 산술 평균
a = round(sum(arr)/N)

# 중앙값
# b = numpy.median(arr)
b = arr[N//2]

# 최빈값
c = 0
# c_arr = Counter(arr).most_common()
# temp = []
# if len(c_arr) == 1:
#     c = c_arr[0][0]
# else:
#     for i in range(len(c_arr)):
#         temp.append(c_arr[i][0])
#         if i+1 < len(c_arr) and c_arr[i][1] != c_arr[i+1][1]:
#             break
#     if len(temp) > 1:
#         temp.sort()
#         c = temp[1]
#     else:
#         c = temp[0]
count = {}
for i in range(1, N+1):     # {1: [], 2:[], 3:[], 4:[]} key는 []안에 든 각 값의 개수
    count[i] = []
temp = 0
for i in range(N):
    if i+1 < N and arr[i] == arr[i+1]:
        temp += 1
    else:
        temp += 1
        count[temp].append(arr[i])
        temp = 0
for i in range(N, 0, -1):
    if len(count[i]) == 1:
        c = count[i][0]
        break
    elif len(count[i]) > 1:
        count[i].sort()
        c = count[i][1]
        break

# 범위
d = arr[-1] - arr[0]

for i in [a, b, c, d]:
    print(i)
