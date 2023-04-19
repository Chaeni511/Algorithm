N, M = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(N)]
result = 0
for card in cards:
    if min(card) > result:
        result = min(card)
print(result)