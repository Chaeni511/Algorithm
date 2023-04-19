# 시간초과
from collections import deque
from itertools import permutations

def play(z):
    global score
    base.append(1)
    for _ in range(z):
        b = base.popleft()
        base.append(0)
        if b:
            score += 1


N = int(input())    # 이닝 수
players = [list(map(int, input().split())) for _ in range(N)]

base = deque()
for _ in range(3):
    base.append(0)

result = 0

for p in permutations([1, 2, 3, 4, 5, 6, 7, 8], 8):     # 게임
    score = 0
    batter = 0
    for i in range(N):  # 이닝
        out = 0
        while out < 3:
            for j in range(batter, 9):  # 타순, p의 인덱스 번호 조절 필요
                # 1-3번 타자
                if j < 3:
                    if players[i][p[j]]:    # 출루
                        play(players[i][p[j]])
                    else:
                        out += 1

                # 4번 타자
                if j == 3:
                    if players[i][0]:
                        play(players[i][0])
                    else:
                        out += 1

                # 5-9번 타자
                if j > 3:
                    if players[i][p[j-1]]:
                        play(players[i][p[j-1]])
                    else:
                        out += 1

                batter = j  # 타순 기록

    result = max(result, score)

print(result)
