import sys

def search():
    print()

N, M = map(int, sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(list(sys.stdin.readline())[:-1])

result = []
for i in range(N-7):
    for j in range(M-7):
        cnt1 = 0
        cnt2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if arr[a][b] != 'W': cnt1 += 1
                    if arr[a][b] != 'B': cnt2 += 1
                else:
                    if arr[a][b] != 'B': cnt1 += 1
                    if arr[a][b] != 'W': cnt2 += 1
        result.append(min(cnt1, cnt2))
print(min(result))