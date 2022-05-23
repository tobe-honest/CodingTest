from collections import deque
def DFS(graph, visited_DFS, V, DFS_l):
    queue = deque([])
    queue.append(V)

    while queue:
        v = queue.pop()
        visited_DFS[v] = True
        DFS_l.append(v)
        for i in graph[v]:
            if not visited_DFS[i]:
                DFS(graph, visited_DFS, i, DFS_l)

def BFS(graph, visited_BFS, V, BFS_l):
    queue = deque([])
    queue.append(V)

    while queue:
        v = queue.popleft()
        if not visited_BFS[v]:
            visited_BFS[v] = True
            BFS_l.append(v)
        for i in graph[v]:
            if not visited_BFS[i]:
                visited_BFS[i] =True
                BFS_l.append(i)
                queue.append(i)


N, M, V = map(int, input().split())
graph = {i : [] for i in range(1, N+1)}
visited_DFS = [False] * (N + 1)
visited_BFS = [False] * (N + 1)
DFS_l = []
BFS_l = []

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    graph[i].sort()

DFS(graph, visited_DFS, V, DFS_l)
BFS(graph, visited_BFS, V, BFS_l)

for idx, i in enumerate(DFS_l):
    if idx == len(DFS_l) - 1: print(i)
    else: print(i, end=" ")

for idx, i in enumerate(BFS_l):
    if idx == len(BFS_l) - 1: print(i)
    else: print(i, end=" ")