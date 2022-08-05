import sys
input = sys.stdin.readline

N = int(input())
l = []

for i in range(N):
    l.append(list(map(int,(input().split()))))


result = [l[0]]
for i in range(1, N):
    tmp = []
    for j in range(3):
        if j == 0:
            cal_num = min(l[i][j] + result[i-1][j+1], l[i][j] + result[i-1][j+2])
            tmp.append(cal_num)
        elif j == 1:
            cal_num = min(l[i][j] + result[i-1][j-1], l[i][j] + result[i-1][j+1])
            tmp.append(cal_num)
        elif j == 2:
            cal_num = min(l[i][j] + result[i-1][j-1], l[i][j] + result[i-1][j-2])
            tmp.append(cal_num)
    result.append(tmp)

print(min(result[-1]))