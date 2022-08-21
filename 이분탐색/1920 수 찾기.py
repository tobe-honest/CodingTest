import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
result = []
A.sort()

for target in B:
    left = 0
    right = len(A)-1
    while right >= left:
        mid = (right + left) // 2
        if target < A[mid]:
            right = mid - 1
        elif target > A[mid]:
            left = mid + 1
        else:
            result.append(1)
            break
    if right < left:
        result.append(0)

for e in result:
    print(e)