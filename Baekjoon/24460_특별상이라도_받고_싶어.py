import sys
def f(x, y, n):
    if n == 1:
        return arr[x][y]
    else:
        temp = [f(x, y, n//2), f(x, y + n//2, n//2), f(x + n//2, y, n//2), f(x + n//2, y + n//2, n//2)]
        temp.sort()
        return temp[1]
N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(f(0, 0, N))

