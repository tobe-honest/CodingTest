import sys
sys.setrecursionlimit(10**4)

def possible(x, y):
    candidate = []
    col = []
    square = []
    # col create
    for i in range(9):
        col.append(arr[i][x])
    # square create    
    for i in range(y//3*3, y//3*3+3):
        for j in range(x//3*3, x//3*3+3):
            square.append(arr[i][j])
    # inspection
    for i in range(1, 10):
        if i not in arr[y] and i not in col and i not in square:
            candidate.append(i)
    return candidate

def solution(n):
    if n == len(zero_pos):
        [print(*row) for row in arr]
        exit()
    x, y = zero_pos[n]
    candidate = possible(x, y)
    for c in candidate:
        arr[y][x] = c
        solution(n+1)
        arr[y][x] = 0

# 1, 4 -> 0,3 ~ 2, 5
#* 1 // 3 * 3 , 4 // 3 * 3 ~ 0 // 3 * 3 + 2, 4 // 3 * 3 + 2
# *#    
# 6, 6 -> 6, 6 ~ 8, 8
# generalized : y, x -> y // 3 * 3, x // 3 * 3 ~ y // 3 * 3 + 2, x // 3 * 3 + 2
    
arr = []
cnt = [0]
zero_pos = []
for y in range(9):
    tmp = list(map(int, sys.stdin.readline().split()))
    for x, x_val in enumerate(tmp):
        if x_val == 0: zero_pos.append((x, y))
    arr.append(tmp)

solution(0)