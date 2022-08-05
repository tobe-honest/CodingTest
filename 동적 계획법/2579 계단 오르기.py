import sys
input = sys.stdin.readline

N = int(input())
l = [int(input()) for i in range(N)]

memo = [0 for i in range(301)]
memo[0] += l[0]
if N > 1:
    memo[1] = l[0] + l[1]
if N > 2:
    memo[2] = max(l[1] + l[2], l[0] + l[2])
for i in range(3, N):
    memo[i] = max(l[i] + l[i-1] + memo[i-3], memo[i-2] + l[i])

print(memo[N-1])