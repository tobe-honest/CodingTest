import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))
summation = [0, l[0]]

for i in range(1, n):
    summation.append(summation[-1] + l[i])
print(summation)
for i in range(m):
    f, t = map(int, input().split())
    print(summation[t]-summation[f-1])