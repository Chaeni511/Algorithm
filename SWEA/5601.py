from fractions import Fraction
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    p = '1'
    q = str(N)
    print(f'#{tc} {(p + "/" + q + " ")*N}')