import sys
import copy
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
memo = copy.deepcopy(l)
for i in range(1, n):
    memo[i] = max(memo[i], memo[i-1] + memo[i])

print(max(memo))
