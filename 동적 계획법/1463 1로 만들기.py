import sys
input = sys.stdin.readline

N = int(input().strip())

memo = [0 for i in range(N+1)]
memo[1] = 0

for i in range(2, N+1):
    memo[i] = memo[i-1] + 1
    if not i % 3:
        memo[i] = min(memo[i], memo[i//3] + 1)
    if not i % 2:
        memo[i] = min(memo[i], memo[i//2] + 1)
print(memo[-1])