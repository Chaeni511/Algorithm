dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

R, C, N = map(int, input().split())
arr = [list(input()) for _ in range(R)]

i = 1
for r in range(R):
    for c in range(C):
        if arr[r][c] == 'O':
            arr[r][c] = i

i += 1
for r in range(R):
    for c in range(C):
        if arr[r][c] == '.':
            arr[r][c] = i
i += 1

while i <= N:
    # visited = [[False]*C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if arr[r][c] == i-2:
                arr[r][c] = '.'
                # visited[r][c] = True
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < R and 0 <= nc < C:
                        arr[nr][nc] = '.'
                        # visited[nr][nc] = True
    for r in range(R):
        for c in range(C):
            if arr[r][c] == '.':
                arr[r][c] = i
    i += 1

for r in range(R):
    for c in range(C):
        if arr[r][c] != '.':
            arr[r][c] = 'O'
for r in range(R):
    print(*arr[r])
# dr = [0, 0, 1, -1]
# dc = [1, -1, 0, 0]
#
# R, C, N = map(int, input().split())
# arr = [list(input()) for _ in range(R)]
#
# i = 1
# for r in range(R):
#     for c in range(C):
#         if arr[r][c] == 'O':
#             arr[r][c] = i
#
# i += 1
# for r in range(R):
#     for c in range(C):
#         if arr[r][c] == '.':
#             arr[r][c] = i
# i += 1
#
# while i <= N:
#     visited = [[False]*C for _ in range(R)]
#     for r in range(R):
#         for c in range(C):
#             if not visited[r][c] and arr[r][c] == '.':
#                 arr[r][c] = i
#
#             elif arr[r][c] == i-2:
#                 arr[r][c] = '.'
#                 visited[r][c] = True
#                 for d in range(4):
#                     nr, nc = r + dr[d], c + dc[d]
#                     if 0 <= nr < R and 0 <= nc < C:
#                         arr[nr][nc] = '.'
#                         visited[nr][nc] = True
#
#     i += 1
#
# for r in range(R):
#     for c in range(C):
#         if arr[r][c] != '.':
#             arr[r][c] = 'O'
# for r in range(R):
#     print(*arr[r])