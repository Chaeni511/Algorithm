for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N-2):
        if arr[i] > arr[i-1] and arr[i] > arr[i-2] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:            
            max = arr[i-2]
            for j in [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]:
                if j > max:
                    max = j
            cnt += (arr[i] - max)

    print(f'#{tc} {cnt}')

# import time
# from datetime import timedelta

# start = time.process_time()

# f = open('1206_input.txt')
# lines = f.readlines()

# t = 0
# while t < 20:
#     n = int(lines[t])
#     apt = list(map(int, lines[t+1].rstrip(' \n').split(' ')))
    
#     result = 0
#     i = 2
#     while i < n - 2:
#         right = 0
#         left = 0
#         final = 0
    
#         if apt[i-2] > apt[i-1]:
#             left = apt[i-2]
#         else:
#             left =  apt[i-1]

#         if apt[i+1] > apt[i+2]:
#             right =  apt[i+1]
#         else:
#             right = apt[i+2]
    
#         if left > right:
#             final = left
#         else:
#             final = right
    
#         if apt[i] > final:
#             result = result + apt[i] - final
#         i += 1

#     print(f'#{int(t/2 + 1)} {result}')
        
#     t += 2

# end = time.process_time()
# #1 691
# #2 9092
# #3 8998
# #4 9597
# #5 8757
# #6 10008
# #7 10194
# #8 10188
# #9 9940
# #10 8684
# print("Time elapsed: ", end - start)

