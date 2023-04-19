T = int(input())
for i in range(T):
    num = int(input())
    price = list(map(int, input().split()))
    max_price = price[-1]
    result = 0

    for p in list(reversed(range(num))):
        if max_price > price[p]:
            result += (max_price - price[p])

    print(f'#{i + 1} {result}')

