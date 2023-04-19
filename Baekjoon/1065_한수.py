N = int(input())
res = 0
for i in range(1, N+1):
    String = str(i)         # int -> str
    Length = len(String)    # str 길이
    if Length == 1:
        res += 1
    else:
        gap = int(String[1]) - int(String[0])   # 차이값
        for j in range(1, Length-1):
            if int(String[j+1]) - int(String[j]) != gap:
                break
        else:
            res += 1
print(res)