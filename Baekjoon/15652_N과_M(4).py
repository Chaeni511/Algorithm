def dfs(c):
    if len(res) == M:
        print(' '.join(map(str, res)))
        return
    for i in range(c, N+1):
        res.append(i)
        dfs(i)
        res.pop()

N, M = map(int, input().split())
res = []
dfs(1)
