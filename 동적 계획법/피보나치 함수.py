import sys

input = sys.stdin.readline

T = int(input())
cashing_fibo = {0 : 0, 1 : 1}
cashing_01 = {0 : (1, 0), 1 : (1, 1)}
for _ in range(T):
    n = int(input())
    if n == 0:
        print("1 0")
        continue
    if n == 1:
        print("0 1")
        continue

    for i in range(2, n+1):
        cnt_0 = 0
        cnt_1 = 0
        if i not in cashing_fibo:
            cashing_fibo[i] = cashing_fibo[i-2] + cashing_fibo[i-1]
            tmp = list(map(int, list(str(i))))
            for j in tmp:
                if j == 0:
                    cnt_0 += 1
                if j == 1:
                    cnt_1 += 1
            cashing_01[i] = (cashing_01[i-1][0] + cnt_0, cashing_01[i-1][1] + cnt_1)
    print(cashing_fibo[i-1], cashing_fibo[i])