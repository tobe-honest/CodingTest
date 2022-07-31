import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, visited):
    global cnt
    visited[start] = [True, cnt]
    for i in graph[start]:
        if not visited[i][0]:
            cnt += 1
            visited[i][0] = True
            dfs(i, visited)


N, M, R = map(int, input().split())
graph = {i+1:[] for i in range(N)}
visited = [[False, 0] for i in range(N+1)]

cnt = 1
for i in range(M):
    f, t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)

for i in range(N):
    if graph[i+1]: graph[i+1] = sorted(list(set(graph[i+1])))

dfs(R, visited)

for _, order in visited[1:]:
    print(order)