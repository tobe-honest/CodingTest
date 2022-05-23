import sys
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(graph, start):
    queue = deque([start])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= len(graph[0]) or ny >= len(graph):
                continue
            if graph[ny][nx] == 1:
                queue.append((ny,nx))
                graph[ny][nx] = graph[y][x] + 1

N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, list(sys.stdin.readline())[:-1])) for i in range(N)]
BFS(graph, (0,0))
print(graph[N-1][M-1])