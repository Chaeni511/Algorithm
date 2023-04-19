import sys
N, M = map(int, sys.stdin.readline().split())
# N 세로 M 가로
maze = [list(sys.stdin.readline()) for _ in range(N)]
key = []
sn, sm = 0, 0
for i in range(N):
    for j in range(M):
        if maze[i][j] == 0:
            sn, sm = i, j

dn = [-1, 1, 0, 0]
dm = [0, 0, -1, 1]
cnt = 0
while maze[sn][sm] != 1:
    for i in range(4):
        if 0 <= sn+dn[i] < N and 0 <= sm+dm[i] < M:
            point = maze[sn+dn[i]][sm+dm[i]]
            if point == 1:
                cnt += 1
                print(cnt)
            elif point == '.':
                pass
            elif point.islower():
                key.append(point.upper())
                point = '?'
            elif point.isupper() and point is key:
                point = '?'
            cnt += 1
