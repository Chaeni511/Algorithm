for tc in range(1, 11):
    no = input()
    table = []
    for _ in range(100):
        table.append(list(map(int, input().split())))

    # 교착상태는 무조건 1로 시작해서 2로 끝남
    result = 0
    for c in range(100):
        r = 0
        stack = []
        while r < 100:
            if len(stack) == 0 and table[r][c] == 1:
                stack.append(table[r][c])
            elif len(stack) > 0 and table[r][c] == 2:
                result += stack.pop()
            r += 1
    print(f'#{tc} {result}')

