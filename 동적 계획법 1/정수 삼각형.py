import sys
input = sys.stdin.readline
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

dp = [l[0]]
for i in range(1, n):
    tmp = []
    for j in range(len(l[i])):
        if j == 0:
            tmp.append(dp[i-1][j] + l[i][j])
        elif j == (len(l[i]) -1):
            tmp.append(dp[i-1][j-1] + l[i][j])
        else:
            cal_num = max(dp[i-1][j-1] + l[i][j], dp[i-1][j] + l[i][j])
            tmp.append(cal_num)
    dp.append(tmp)

print(max(dp[-1]))