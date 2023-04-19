N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
direction = list(map(int, input().split()))
dice = [0]*6


# dice index    East     West     North     South
#     3          3        3         0         5
#   2 0 1      0 1 5    5 2 0     2 4 1     2 3 1
#     4          4        4         5         0
#     5          2        1         3         4
# dice index는 기본 전개도에  index 번호를 붙인 것
# dice index를 기준로 각 방향으로 굴러갔을 때 숫자 변화

def roll(d):
    global dice
    global x, y
    # 동
    if d == 1:
        if 0 <= y+1 < M:
            dice = [dice[1], dice[5], dice[0], dice[3], dice[4], dice[2]]
            y += 1
        else:
            return
    # 서
    elif d == 2:
        if 0 <= y - 1 < M:
            dice = [dice[2], dice[0], dice[5], dice[3], dice[4], dice[1]]
            y -= 1
        else:
            return
    # 북
    elif d == 3:
        if 0 <= x - 1 < N:
            dice = [dice[4], dice[1], dice[2], dice[0], dice[5], dice[3]]
            x -= 1
        else:
            return
    # 남
    else:
        if 0 <= x + 1 < N:
            dice = [dice[3], dice[1], dice[2], dice[5], dice[0], dice[4]]
            x += 1
        else:
            return

    print(dice[0])

    # 이동한 칸의 수가 0일 때
    if board[x][y] == 0:
        board[x][y] = dice[5]
    # 0이 아닐 때
    else:
        dice[5], board[x][y] = board[x][y], 0


dice[5] = board[x][y]

for i in direction:
    roll(i)



# a = b = c = d = e = f = 0
# if 0 <= x-2 < N:
#     a = board[x-2][y]
#     if 0 <= y+1 < N:
#         b = board[x-2][y+1]
#     if 0 <= y - 1 < N:
#         c = board[x-2][y-1]
# if 0 <= x - 3 < N:
#     d = board[x-3][y]
# if 0 <= x-1 < N:
#     e = board[x-1][y]
# f = board[x][y]