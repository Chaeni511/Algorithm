'''
1
5 4
1 2
2 3
2 5
5 4
'''
import sys

def travel(country, cnt):
    visited[country] = 1
    for i in airline[country]:
        if visited[i] == 0:
            cnt = travel(i, cnt + 1)
    return cnt


T = int(sys.stdin.readline())
for tc in range(1, T+1):
    N, M = map(int, sys.stdin.readline().split())
    airline = [[] for _ in range(N + 1)]

    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        if b is not airline[a]:
            airline[a].append(b)
        if a is not airline[b]:
            airline[b].append(a)

    visited = [0] * (N + 1)
    cnt = travel(1, 0)
    print(cnt)
