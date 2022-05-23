import sys
from collections import deque

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

N, M = map(int, sys.stdin.readline().split())
graph = {i+1 : [] for i in range(N)}
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1, N+1):
    if visited[i]: continue
    bfs(graph, i, visited)
    cnt += 1

print(cnt)