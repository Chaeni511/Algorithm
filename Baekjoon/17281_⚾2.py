from itertools import permutations


def play(z):
    global score, out, b1, b2, b3
    if z == 0:
        out += 1
    elif z == 1:
        score += b3
        b3, b2, b1 = b2, b1, 1
    elif z == 2:
        score += b3 + b2
        b3, b2, b1 = b1, 1, 0
    elif z == 3:
        score += b3 + b2 + b1
        b3, b2, b1 = 1, 0, 0
    else:
        score += b3 + b2 + b1 + 1
        b3 = b2 = b1 = 0


N = int(input())    # 이닝 수
players = [list(map(int, input().split())) for _ in range(N)]
b1 = b2 = b3 = 0
result = 0

for p in permutations([1, 2, 3, 4, 5, 6, 7, 8], 8):     # 게임
    score = 0
    start_batter = 0
    for i in range(N):  # 이닝
        out = 0
        batter = start_batter
        while out < 3:
                # 1-3번 타자
                if batter < 3:
                    play(players[i][p[batter]])

                # 4번 타자
                elif batter == 3:
                    play(players[i][0])

                # 5-9번 타자
                else:
                    play(players[i][p[batter-1]])

                if batter == 8:
                    batter = 0
                else:
                    batter += 1

        start_batter = batter

    result = max(result, score)
    if result == 48:
        print(p)
print(result)
