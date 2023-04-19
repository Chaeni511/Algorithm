def I(x, y, s):
    i = 0
    while i < y:
        original_code.insert(x+i, s[i])
        i += 1

def D(x, y):
    del original_code[x-1:x+y-1]

def A(y, s):
    for i in range(1, y):
        original_code.append(i)


for tc in range(1, 11):
    N = int(input()) # 원문 암호 길이
    original_code = list(map(int, input().split()))
    M = int(input()) # 명령어 개수
    temp = list(input().split())
    command =[]

    t = 0
    while t < len(temp):
        c = []
        if temp[t].isalpha() == True:
            c.append(temp[t])
            t += 1
            while t < len(temp) and temp[t].isdigit() == True:
                c.append(int(temp[t]))
                t += 1
        command.append(c)
    # print(command)
    for m in range(M):
        if command[m][0] == 'I':
            x = int(command[m][1])
            y = int(command[m][2])
            s = []
            for j in range(3, 3+y):
                s.append(int(command[m][j]))
            I(x, y, s)
        elif command[m][0] == 'D':
            x = int(command[m][1])
            y = int(command[m][2])
            D(x,y)
        else:
            y = int(command[m][1])
            s = []
            for j in range(2, 2 + y):
                s.append(int(command[m][j]))
            A(y, x)
    print(f'#{tc} {" ".join(map(str, original_code[0:10]))}')