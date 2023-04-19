TC = int(input())
for tc in range(1, TC+1):
    A, B = map(int, input().split())
    cnt = 0
    for i in range(A, B+1):
        num = i ** 0.5
        # num이 1.0 같이 int면 회문이지만 float이라 회문으로 인식이 안되는 걸 방지
        if num - int(num) == 0:
            num = str(int(num))
        else:
            num = str(num)
        
        # 회문 검사
        i = str(i)
        if i == i[::-1] and num == num[::-1]:
            cnt += 1

    print(f'#{tc} {cnt}')

