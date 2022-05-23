import sys
from collections import deque
from typing import Tuple

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

def BFS(start, target):
    queue = deque([start])
    board[start[0]][start[1]] = 1
    if start == target:
        print(board[target[0]][target[1]]-1)
        return
    while queue:
        x, y = queue.popleft()
        t_x, t_y = target

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < L and 0 <= ny < L and not board[nx][ny]:
                    board[nx][ny] = board[x][y] + 1
                    if nx == t_x and ny == t_y:
                        print(board[nx][ny]-1)
                        return
                    queue.append((nx, ny))
T = int(sys.stdin.readline())

for _ in range(T):
    L = int(sys.stdin.readline())
    board = [[0] * L for _ in range(L)]
    start = tuple(map(int, sys.stdin.readline().split()))
    target = tuple(map(int, sys.stdin.readline().split()))

    BFS(start, target)