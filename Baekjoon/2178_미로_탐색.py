from collections import deque

def bfs():
    global min_cnt
    Q = deque()
    Q.append((0, 0, 0))
    while Q:
        x, y, c = Q.popleft()

        if x == N - 1 and y == M - 1:
            c += 1
            if c < min_cnt:
                min_cnt = c

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                Q.append((nx, ny, c + 1))
                # maze[nx][ny] = 0


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

min_cnt = 987654321
bfs()
print(min_cnt)



