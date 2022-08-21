import sys
input = sys.stdin.readline
import heapq
from queue import PriorityQueue

N = int(input())
num = int(input())
l = PriorityQueue()
l.put(num)
print()
# for i in range(N-1):
#     # print(l[(len(l)-1) // 2])
#     num = int(input())
#     l.put(num)
#     print(f"list : {l}")
#     # left = 0
#     # right = len(l)-1
#     # while left <= right:
#     #     mid = (left + right) // 2
#     #     if l[mid] <= num:
#     #         left = mid + 1
#     #     else:
#     #         right = mid - 1
#     # l = l[:right+1] + [num] + l[right+1:]
# print(l[(len(l)-1) // 2])

# # [1, 2, 5, 10] 4
# # [1, 2, 4, 5, 10] 3


