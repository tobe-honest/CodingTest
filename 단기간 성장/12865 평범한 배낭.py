import sys
input = sys.stdin.readline

N, K = map(int, input().split())

l = [list(map(int, input().split())) for i in range(N)]

print(l)