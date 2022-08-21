import sys
input = sys.stdin.readline

cnt = 0
def ncr(row, col, n):
    global cnt
    if r == row and C == col:
        print(cnt)
        exit()
    if n == 1:
        cnt += 1
        return
    if row <= r < row + n and col <= C < col + n:
        ncr(row, col, n//2)
        ncr(row, col + n//2, n//2)
        ncr(row + n//2, col, n//2)
        ncr(row + n//2, col + n//2, n//2)
    else:
        cnt += n * n
        return
N, r, C = map(int,input().split())
# l = [[0 for j in range(2**(N))] for i in range(2**(N))]
# tmp = 2**(N-1)
ncr(0, 0, 2**(N))