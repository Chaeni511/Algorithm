T = int(input())
for tc in range(1, T+1):
    s = list(input())
    a, b = 1, 1
    for i in s:
        if i == 'L':
            a, b = a, a+b
        else:
            a, b = a+b, b
    print(f'#{tc} {a} {b}')