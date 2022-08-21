import sys
input = sys.stdin.readline

N = int(input())
memo = [0 for _ in range(N+1)]
T = [0 for _ in range(N+1)]
P = [0 for _ in range(N+1)]
for _ in range(1, N+1):
    t, p = map(int, input().split())
    T[_] = t
    P[_] = p
    memo[_] = p

for i in range(2, N+1):
    for j in range(1, i):
        # print(i, j, memo[i])
        if i - j >= T[j] and T[j] + i <= N:
            print(i, j, T[j], P[j], T[i], P[i])
            memo[i] = max(memo[i-1], P[i] + memo[i+T[j]])
            
        # else: memo[i] = 0
print(memo)
print(T)
print(P)