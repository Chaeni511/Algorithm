from collections import deque
import copy

# A, B, C
arr = list(map(int, input().split()))
q = deque()
res = set()
check = []


def dfs(w):
    if w[0] == 0:
        res.add(w[2])

    if str(w) in check:
        return
    else:
        check.append(str(w))
        q.append(w)


def pour(i, j, ww):
    water = copy.deepcopy(ww)

    water[i], water[j] = max(0, water[i] - (arr[j] - water[j])), min(water[j] + water[i], arr[j])

    dfs(water)


q.append([0, 0, arr[2]])
check.append(f'[0, 0, {arr[2]}]')

while q:
    temp = q.popleft()

    pour(0, 1, temp)
    pour(0, 2, temp)
    pour(1, 0, temp)
    pour(1, 2, temp)
    pour(2, 0, temp)
    pour(2, 1, temp)


print(" ".join(map(str, sorted(res))))
