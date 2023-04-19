for t in range(10):
    D = int(input())
    box = list(map(int,input().split()))
    
    i = 0

    while i < D:
        box[box.index(max(box))] -= 1
        box[box.index(min(box))] += 1
        i += 1

    case_num = int(t + 1)
    result = max(box) -  min(box)
    print(f'#{case_num} {result}')