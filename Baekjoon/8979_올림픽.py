N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))
res = 0
for i in range(N):
    if arr[i][0] == K:
        res = i
        break
for i in range(res):
    if arr[i][1:] == arr[res][1:]:
        res -= 1
print(res+1)