import sys
from collections import deque

def BFS():
    queue = deque([])
    queue.append(N)
    while queue:
        x = queue.popleft()
        # print(x)
        if x == K:
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 10 ** 5 and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)

N, K = map(int, sys.stdin.readline().split())
dist = [0] * (10 ** 5 + 1)

BFS()