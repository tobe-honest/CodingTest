import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
N = int(sys.stdin.readline())

def BFS(start, visited):
    queue = deque([start])
    visited[start[0]][start[1]] = False

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == True:
                visited[ny][nx] = False
                queue.append((ny,nx))

arr = []
max_h = 0
for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    arr.append(tmp)
    max_h = max(max_h, max(tmp))

result = []
for h in range(max_h+1):
    cnt = 0
    visited = [ [False for _ in range(N)] for __ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > h: visited[i][j] = True

    for i in range(N):
        for j in range(N):
            if not visited[i][j]: continue
            BFS((i,j), visited)
            cnt+=1

    result.append(cnt)

print(max(result))