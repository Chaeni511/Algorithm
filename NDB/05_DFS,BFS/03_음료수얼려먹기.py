'''
DFS

4 5
00110
00011
11111
00000
ans = 3

15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
ans = 8
'''
import sys
def icecream(x, y):
    if not (0 <= x < N and 0 <= y < M):
        return False

    if not ice[x][y]:
        ice[x][y] = True

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            icecream(nx, ny)
        return True
    return False


N, M = map(int, sys.stdin.readline().split())
ice = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if icecream(i, j):
            ans += 1

print(ans)

