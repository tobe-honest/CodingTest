import sys

N = int(sys.stdin.readline())
arr = []
result = []
for _ in range(N):
    w, h = map(int, sys.stdin.readline().split())
    arr.append([w, h])

for i in range(len(arr)):
    cnt = 1
    base_w, base_h = arr[i]
    for j in range(len(arr)):
        comp_w, comp_h = arr[j]
        if base_w < comp_w and base_h < comp_h:
            cnt += 1
    result.append(cnt)

for idx, i in enumerate(result):
    if idx == len(result) -1:
        print(i)
    else:
        print(i, end=" ")