import sys
N = list(sys.stdin.readline())
N.pop()
arr = [0]*9
for n in N:
    if n == '9':
        arr[6] += 1
    else:
        arr[int(n)] += 1
if arr[6] % 2 == 0:
    arr[6] //= 2
else:
    arr[6] //= 2
    arr[6] += 1
print(max(arr))


# import sys
# N = list(sys.stdin.readline())
# N.pop()
# arr = [0]*10
# for n in N:
#     arr[int(n)] += 1
# if arr[6] >= arr[9]:
#     while arr[6] >= arr[9]:
#         arr[6] -= 1
#         arr[9] += 1
# else:
#     while arr[6] < arr[9]:
#         arr[6] += 1
#         arr[9] -= 1
# print(max(arr))