from collections import deque

def bfs():
    Q = deque()
    Q.append((0, 0))
    while Q:
        x, y = Q.popleft()

        if x == N-1 and y == M-1:
            return arr[x][y]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                Q. append((nx, ny))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int, input().split())    # x, y
arr = [list(map(int, input())) for _ in range(N)]

print(bfs())