import sys
sys.setrecursionlimit(10**4)

def possible(cur):
    for i in range(cur):
        if arr[i] == arr[cur] or abs(cur - i) == abs(arr[cur] - arr[i]):
            return 0
    return 1

def n_queen(cur):
    if cur == N:
        cnt[0] += 1
        return
    for i in range(N):
        arr[cur] = i
        if possible(cur) == 1:
            n_queen(cur+1)

cnt = [0]
N = int(sys.stdin.readline())
arr = [0 for _ in range(N)]
n_queen(0)
print(cnt[0])