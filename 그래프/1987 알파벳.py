from collections import deque
import sys
input = sys.stdin.readline

# 상 하 좌 우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
m = 0
def search(start, alpha_l, cnt):
    global m
    m = max(m, cnt)
    for i in range(4):
        nx = start[0] + dx[i]
        ny = start[1] + dy[i]
        if nx >= R or nx < 0 or ny >= C or ny < 0 or alpha_l[ord(board[nx][ny]) - ord('A')] or visited[nx][ny]:
            continue

        alpha_l[ord(board[nx][ny]) - ord('A')] = True
        visited[nx][ny] = True
        search((nx, ny), alpha_l, cnt + 1)
        alpha_l[ord(board[nx][ny]) - ord('A')] = False
        visited[nx][ny] = False

R, C = map(int, input().split())
board = [list(input().strip()) for i in range(R)]
dic = [0] * 26
visited = [[False for __ in range(C)] for _ in range(R)]
visited[0][0] = True
dic[ord(board[0][0]) - ord('A')] = 1
search((0,0), dic, 1)
print(m)