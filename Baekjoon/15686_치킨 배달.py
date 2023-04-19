from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))

for c in combinations(chicken, M):

