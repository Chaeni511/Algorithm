# L min
# U max
# X excercise
# I

T = int(input())
for i in range(T):
    L, U, X = map(int,(input().split()))
    if X < L:
        print(f'#{i+1} {L - X}')
    elif X > U:
        print(f'#{i+1} -1')
    else:
        print(f'#{i+1} 0')

