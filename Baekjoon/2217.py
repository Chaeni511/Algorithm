import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]
arr.sort(reverse=True)
weight = []
for i in range(N):
    weight.append(arr[i] * (i + 1))

print(max(weight))

# max = 0
# for i in range(N):
#     cnt = 0
#     for j in range(N):
#         if arr[j] >= arr[i]:
#             cnt += arr[i]
#     if cnt > max:
#         max = cnt
#
# print(max)