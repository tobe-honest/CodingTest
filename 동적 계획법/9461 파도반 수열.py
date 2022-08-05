import sys
input = sys.stdin.readline

memo  = [0 for i in range(101)]

memo[1] = 1
memo[2] = 1
memo[3] = 1

T = int(input())
for i in range(T):
    N = int(input())
    for i in range(4, N+1):
        memo[i] = memo[i-3] + memo[i-2]
    print(memo[N])