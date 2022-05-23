import sys
from itertools import permutations
N, M = map(int, sys.stdin.readline().split())

a = list(permutations(range(1, N+1), M))
for i in a:
    for idx, j in enumerate(i):
        if idx == len(i)-1:
            print(j)
        else:
            print(j, end=" ")