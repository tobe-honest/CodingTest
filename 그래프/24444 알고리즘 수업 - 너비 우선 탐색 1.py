import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start, visited):
    cnt = 1
    q = deque([start])
    visited[start] = [True, 1]
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i][0]:
                # print(i)
                cnt += 1
                visited[i] = [True, cnt]
                q.append(i)

N, M, R = map(int, input().split())
graph = {i+1 : [] for i in range(N)}
visited = [[False, 0] for i in range(N+1)]
for i in range(M):
    f, t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)

graph = {i+1 : sorted(v) for i, v in enumerate(list(graph.values()))}
bfs(graph, R, visited)

for _, order in visited[1:]:
    print(order)