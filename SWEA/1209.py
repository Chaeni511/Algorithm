for t in range(10):
    case_num = int(input())
    num = list(map(int, input().split('\n'))) # 한줄씩 리스트로 인풋이 안됨..
    result = 0
    arr = []
    for i in range(100):
        arr.append(list(num[i:i+10]))
        i += 10
    print(num)