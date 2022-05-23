import sys

N = int(sys.stdin.readline())
ans = 0
for i in range(1, N+1):
    if i + sum(map(int,list(str(i)))) == N:
        ans = i
        break
print(ans)