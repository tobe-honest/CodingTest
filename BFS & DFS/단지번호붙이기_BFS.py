from collections import deque
import sys
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def BFS(graph, start):
    queue = deque([start])
    a, b = start
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    return count


N = int(sys.stdin.readline())
graph = [ list(map(int, list(sys.stdin.readline())[:-1])) for i in range(N)]
result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            result.append(BFS(graph, (i,j)))

print(len(result))
for i in sorted(result):
    print(i)