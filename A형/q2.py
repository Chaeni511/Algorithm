T = int(input())
for tc in range(1, T+1):
    Ms, Ma = map(int, input().split())
    N, L = map(int, input().split())
    origin = Ms + Ma * L
    arr = [list(map(int, input().split())) for _ in range(N)]
    gap = [[0] for _ in range(N)]

    # gap
    for i in range(N):
        for j in range(L):
            gap[i].append(arr[i][j+1] - arr[i][j])

    money = Ms
    cnt = []
    field = []
    # month
    for i in range(1, L+2):
        for n in range(len(cnt)):
            money += cnt[n] * arr[field[n]][i-1]
        if i == L+1:
            break
        cnt = []
        field = []
        temp = []
        # field
        for j in range(N):
            temp.append((gap[j][i], j, i))
        temp.sort(reverse=True)
        for t in temp:
            p, x, y = t
            if p <= 0:
                break
            else:
                if money // arr[x][y-1] > 0:
                    cnt.append(money // arr[x][y-1])
                    field.append(x)
                    money -= (money // arr[x][y-1]) * arr[x][y-1]

        money += Ma
    print(f'#{tc} {money - origin}')

