T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    if M == 1:
        print(f'#{tc}')
        for i in range(1, N+1):
            print('*' * i)
    
    elif M == 2:
        print(f'#{tc}')
        for i in range(N, 0, -1):
            print('*' * i)
    
    else:
        print(f'#{tc}')
        for i in range(1, 2*N, 2):
            print(' ' * ((2*N-1-i)//2) + '*' * i + ' ' * ((2*N-1-i)//2))