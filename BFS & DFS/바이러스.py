from collections import deque
import sys

def DFS(graph, start, visited):
    queue = deque([start])   
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                DFS(graph, i, visited)

n_com = int(sys.stdin.readline())
n_line = int(sys.stdin.readline())

graph = {i+1 : [] for i in range(n_com)}
visited = [False] * (n_com + 1)
for i in range(n_line):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    graph[i].sort()

DFS(graph, 1, visited)
print(sum(visited)-1)