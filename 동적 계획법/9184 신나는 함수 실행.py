import sys
input = sys.stdin.readline

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        if memo[20][20][20] == -1:
            return w(20, 20, 20)
        else: return memo[20][20][20]

    elif a < b < c:
        if memo[a][b][c] == -1:
            memo[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return memo[a][b][c]
    else:
        if memo[a][b][c] == -1:
            memo[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return memo[a][b][c]

memo = [[[-1 for k in range(22)] for j in range(22)] for i in range(22)]

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1: break
    else:
        print(f"w({a}, {b}, {c}) = {w(a, b, c)}")