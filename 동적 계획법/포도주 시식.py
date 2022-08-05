import sys
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]

# n이 1이면 l[0]이 최대값
dp[0] = l[0]

# n이 2이면 l[0] + l[1]이 최대값
if n > 1:
    dp[1] = l[0] + l[1]

# n이 3이면
# max(l[0] + l[1], l[0] + l[2], l[1] + l[2])가 최대값
if n > 2:
    dp[2] = max(l[2]+l[1], l[2]+l[0], dp[1])

# n이 4이상이면 
# max(이전까지 고른 2잔(이번 잔 안고름), 전전전잔 + 이전잔 + 이번잔, 전전잔 + 이번잔)
# ex) 1, 2, 3, 4가 있을 때
# max( 2 + 3, 1 + 3 + 4, 2 + 4 )
for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-3]+l[i-1]+l[i], dp[i-2]+l[i])
print(dp[n-1])