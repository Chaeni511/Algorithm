N = int(input())
distance = list(map(int, input().split()))
oil = list(map(int, input().split()))

city = res = 0
for i in range(1, N):
    if i == N-1:
        res += sum(distance[city:i]) * oil[city]
        break
    if i > city and oil[i] < oil[city]:
        res += sum(distance[city:i]) * oil[city]
        city = i
print(res)