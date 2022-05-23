import sys
from collections import deque

dx = [0, 0, -1, 1, 1, -1, 1, -1]
dy = [-1, 1, 0, 0, 1, 1, -1, -1]

def BFS(start):
    queue = deque([start])
    arr[start[0]][start[1]] = 0

    while queue:
        y, x = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < w and 0 <= ny < h and arr[ny][nx]:
                arr[ny][nx] = 0
                queue.append((ny,nx))
result = []
while True:
    w, h = map(int, sys.stdin.readline().split())
    if not w and not h: break
    
    arr = []
    for _ in range(h):
        arr.append(list(map(int, sys.stdin.readline().split())))
    
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 0: continue
            BFS((i,j))
            cnt+=1
    result.append(cnt)

for i in result:
    print(i)