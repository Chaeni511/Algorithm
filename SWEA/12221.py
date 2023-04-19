def f(A, B):
    if 0 < A < 10 and 0 < B < 10:
        return A*B
    else: return -1

T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    print(f'#{tc} {f(A, B)}')