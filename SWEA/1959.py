def f(N, M , A, B):
    max = 0
    for i in range(M-N+1):
        sum = 0
        B_temp = []
        for j in range(i, i+N):
            B_temp.append(B[j])
        for k in range(N):
            sum += A[k] * B_temp[k]
        if sum > max:
            max = sum
    return max

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split( )))
    B = list(map(int, input().split( )))
    if N < M:
        print(f'#{tc} {f(N, M, A, B)}')
    else:
        print(f'#{tc} {f(M, N, B, A)}')