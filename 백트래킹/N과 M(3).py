import sys
from itertools import permutations
N, M = map(int, sys.stdin.readline().split())
ar = [str(i+1) for i in range(N)]

a = permutations(''.join(ar), repeat=M)
for i in a:
    for idx, j in enumerate(i):
        if idx == len(i)-1:
            print(j)
        else:
            print(j, end=" ")