import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
cnt1 = 0
cnt2 = 0

def fib(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    else: return fib(n-1) + fib(n-2)

def fibonacci(n):
    global cnt2
    cnt2 = 0
    memo = [0 for i in range(n+1)]
    memo[1], memo[2] = 1, 1
    for i in range(3, n+1):
        memo[i] = memo[i-2] + memo[i-1]
        cnt2 += 1
    return memo[n]

N = int(input())
fib(N)
fibonacci(N)
print(cnt1, cnt2)

#                       fib(5)
#         fib(4)                         fib(3)
#    fib(3)      fib(2)                fib(2) fib(1)
# fib(2) fib(1)