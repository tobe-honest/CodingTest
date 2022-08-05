import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

memo_l = [1 for i in range(N)]
memo_h = [1 for i in range(N)]


for i in range(N):
    for j in range(i):
            if A[i] > A[j]:
                memo_l[i] = max(memo_l[j] + 1, memo_l[i])
            
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j]:
            memo_h[i] = max(memo_h[j] + 1, memo_h[i])

maximum = 0
for l, h in zip(memo_l, memo_h):
    if l + h > maximum:
        maximum = l + h

print(maximum-1)