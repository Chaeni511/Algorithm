for tc in range(1, 11):
    T = int(input())
    code = list(map(int, input().split()))
    arr = [1] # 암호에서 뺄 값을 담을 리스트(1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...)
    for i in arr:
        # 암호를 만들기 위해 i를 뺌
        code[0] -= i
        code.append(code.pop(0))

        # for문으로 무한 루프 생성/다음에 빼줄 값을 정해서 arr에 append
        if i == 5:
            arr.append(1)
        else:
            arr.append(i+1)

        # 암호 도출 조건
        if code[7] <= 0:
            code[7] = 0
            break

    print(f'#{tc} {" ".join(map(str, code))}')
