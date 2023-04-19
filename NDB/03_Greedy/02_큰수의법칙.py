N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
result = 0
m = M
while m > M % (K+1):
    result += arr[0] * K + arr[1]
    m -= K+1
result += arr[0] * m
print(result)