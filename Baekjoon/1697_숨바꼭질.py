from collections import deque


def bfs():
    while Q:
        n = Q.popleft()
        if n == K:
            return arr[K]
        for i in[n-1, n+1, n*2]:
            if 0 <= i <= 100000 and not arr[i]:
                arr[i] = arr[n] + 1
                Q.append(i)


N, K = map(int, input().split())
Q = deque()
Q.append(N)
arr = [0] * 100001
print(bfs())