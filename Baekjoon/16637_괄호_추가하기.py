def dfs(idx, val):
    global res
    if idx == N - 1:
        res = max(res, val)
        return
    if idx + 2 < N:
        dfs(idx + 2, operate(val, S[idx + 1], int(S[idx + 2])))
    if idx + 4 < N:
        dfs(idx + 4, operate(val, S[idx + 1], operate(int(S[idx + 2]), S[idx + 3], int(S[idx + 4]))))



# 사칙연산 함수
def operate(num1, op, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2


N = int(input())
S = input() # 스트링으로 처리
res = -987654321
# res = -1 * sys.maxsize    # 시스템 상에서 가능한 가장 큰 수 반환

dfs(0, int(S[0]))
print(res)
