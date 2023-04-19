import sys
def H(n, r, k, s):
    global cnt
    if k == r:
        if sum(T) == N:
            cnt += 1
        return
    else:
        for i in range(s, n):
            T[k] = A[i]
            H(n, r, k+1, i)

T = int(sys.stdin.readline())
for tc in range(1, T+1):
    N = int(sys.stdin.readline())
    A = [1, 2, 3]
    r = 0
    T = [0] * (N+1)
    cnt = 0
    for i in range(1, 5):
        H(3, i, 0, 0)
    print(cnt)