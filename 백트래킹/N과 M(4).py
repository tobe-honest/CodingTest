import sys
from itertools import combinations_with_replacement
N, M = map(int, sys.stdin.readline().split())
ar = [str(i+1) for i in range(N)]

a = combinations_with_replacement(''.join(ar), r=M)
for i in a:
    for idx, j in enumerate(i):
        if idx == len(i)-1:
            print(j)
        else:
            print(j, end=" ")