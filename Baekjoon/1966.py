import sys
T = int(sys.stdin.readline())
for tc in range(T):
    N, M = map(int, sys.stdin.readline().split())
    arr = [e for e in range(N)]     # 중요도의 index로 만든 Queue
    importance = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    while len(arr) > 0:
        j = importance[arr[0]]      # Queue맨 앞에 위치한 중요도
        for i in range(1, len(arr)):
            if importance[arr[i]] > j:
                arr.append(arr.pop(0))
                break
        else:
            m = arr.pop(0)
            cnt += 1
            if m == M:
                print(cnt)
                break
