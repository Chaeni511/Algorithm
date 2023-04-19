for T in range(10):
    N = int(input())
    arr_h = [] 
    arr_w = []
    result = 0

    for i in range(8):
        arr_h.append(list(input()))

    arr_w += arr_h

    for e in range(8):
        arr_v = [s[e] for s in arr_h]
        arr_w.append(arr_v)

    for j in range(16):
        for r in range(8 - N + 1):
            if arr_w[j][r:r + N] == arr_w[j][r:r + N][::-1]:
                result += 1

    print(f'#{T+1} {result}')