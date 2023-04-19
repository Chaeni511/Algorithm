from collections import deque


def bfs(x, y):
    width = 0
    Q.append((x, y))
    while Q:
        x, y = Q.popleft()
        width += 1
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                visited[nx][ny] = 1
                Q.append((nx, ny))
    return width


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())    # col, row
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = max_width = 0
Q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] and not visited[i][j]:
            visited[i][j] = 1
            max_width = max(max_width, bfs(i, j))
            cnt += 1
print(cnt)
print(max_width)
