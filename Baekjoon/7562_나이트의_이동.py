from collections import deque

def bfs(x, y):
    Q = deque()
    Q.append((x, y))

    while Q:
        i, j = Q.popleft()

        if (i, j) == (gi, gj):
            return visited[i][j]

        for d in range(8):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < l and 0 <= nj < l and not visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                Q.append((ni, nj))


di = [-2, -2, -1, -1, 1, 1, 2, 2]
dj = [-1, 1, -2, 2, -2, 2, -1, 1]

T = int(input())

for tc in range(T):
    l = int(input())
    si, sj = map(int, input().split())
    gi, gj = map(int, input().split())
    visited = [[0] * l for _ in range(l)]

    print(bfs(si, sj))
