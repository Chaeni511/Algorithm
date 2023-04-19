# 14510

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))
    TREE = max(trees)
    one = 0
    two = 0
    three = 0
    result = 0

    for i in range(N):
        trees[i] = TREE - trees[i]

    for t in trees:
        if t % 3 == 0:
            three += t // 3
        elif t % 3 == 1:
            one += 1
            three += t // 3
        else:
            two += 1
            three += t // 3

    result += three * 2

    if one > two:
        result += two * 2
        if (one - two) % 2 == 0:
            result += ((one - two) // 3) * 2
            result += ((one - two) % 3) * 2 - 1
        else:
            result += ((one - two) // 3) * 2
            result += ((one - two) % 3) * 2

    elif one == two:
        result += one + two
    else:
        result += one * 2
        if (two - one) % 2 == 0:
            result += ((two - one) // 3) * 2 - 1
            result += ((two - one) % 3) * 2
        else:
            result += ((two - one) // 3) * 2 - 1
            result += ((two - one) % 3) * 2

    print(f'#{tc} {result}')


'''
5
2
5 5
2
4 2
2
3 4
4
2 3 10 5
4
1 2 3 4
'''
'''
#1 0
#2 2
#3 1
#4 18
#5 4
#6 244
#7 17
#8 26
#9 32
#10 282
#11 590
#12 31
#13 36
#14 34
#15 532
#16 1452
#17 55
#18 62
#19 62
#20 1312
#21 2726
#22 71
#23 98
#24 94
#25 2804
#26 6208
#27 115
#28 132
#29 122
#30 5774
'''