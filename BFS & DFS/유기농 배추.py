import sys
from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS(graph, start):
    queue = deque([start])
    a, b = start
    graph[a][b] = 0

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((ny, nx))

T = int(sys.stdin.readline())
for _ in range(T):
    cnt = 0
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0]*M for i in range(N)]
    
    for __ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                BFS(graph, (y, x))
                cnt += 1
    print(cnt)