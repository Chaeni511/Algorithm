T = int(input())
for tc in range(1, 11):
    N, K = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    arr += list(zip(*arr))

    result = 0
    for i in range(N*2):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 0:
                if cnt == K:
                    result += 1
                cnt = 0
            else:
                cnt += 1

        if cnt == K:
            result += 1

    print(f'#{tc} {result}')