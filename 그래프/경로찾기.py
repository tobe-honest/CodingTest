import sys
from collections import deque
input = sys.stdin.readline

def search(i, visited):
    q = deque([])
    print(graph[i])
    for idx, g in enumerate(graph[i]):
        if g and not visited[i][idx]:
            visited[i][idx] = 1
            print(visited)
            q.append(idx)
            search(idx, visited)

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for __ in range(n)]

for i in range(n):
    search(i, visited)
    