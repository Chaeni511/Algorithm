T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    mid = int(N//2) + 1

    print(f'#{tc}')

    if M == 1:
        for i in range(1, N+1):
            if i <= mid:
                print('*' * i)
            else:
                print('*' * (N-i+1))

    elif M == 2:
        for i in range(1, N+1):
            if i <= mid:
                print(' ' * (mid-i) + '*' * i)
            else:
                print(' ' * (mid-N+i-1) + '*' * (N-i+1))

    elif M == 3:
        print(f'#{tc}')
        x = N
        for i in range(1, N+1):
            if i <= N//2:
                while x > 0:
                    print(' ' * ((N-x)//2) + '*' * x + ' ' * ((N-x)//2))
                    x -= 2
            else:
                while x < N:
                    x += 2
                    print(' ' * ((N-x)//2) + '*' * x + ' ' * ((N-x)//2))

    else:
        print(f'#{tc}')
        x = mid
        y = 0
        for i in range(1, N+1):
            if i <= mid:
                while x > 0:
                    print(' ' * y + '*' * x + ' ' * (N - mid))
                    x -= 1
                    y += 1
            else:
                while x <= mid:
                    y -= 1
                    x += 1
                    print(' ' * (N - mid) + '*' * x + ' ' * y)