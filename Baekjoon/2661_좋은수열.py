from itertools import permutations


def check(p):
    for i in range(N-1):
        temp = p[i:]
        for i in range(1, N//2+1):
            if temp[:i] == temp[i: i+i]:
                return False
    return True


N = int(input())
res = []
for i in range(1, 4):
    res.append(i)
    
# arr = [1] * (N//2 +1) + [2] * (N//2 +1) + [3] * (N//2 +1)
# for perm in permutations(arr, N):
#     flag = True
#     if check(perm):
#         print(''.join(map(str, perm)))
#         break
# N = 6
# check((1,2,3,1,2,1))