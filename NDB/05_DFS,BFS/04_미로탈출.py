'''
5 6
101010
111111
000001
111111
111111
ans = 10
'''
import sys
from collections import deque
def out(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if not maze[nx][ny]:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx, ny))
    return maze[N-1][M-1]


N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False]*M for _ in range(N)]
print(out(0, 0))
