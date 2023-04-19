def multiply(N, M):
    if M == 1:
        return N
    return N * multiply(N, M - 1)

for s in range(10):
    tc = int(input())
    N, M = map(int, input().split())
    print(f'#{s+1} {multiply(N, M)}')
    