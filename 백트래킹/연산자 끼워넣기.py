import sys

def solution(idx, result, add, sub, mul, div):

    if add + sub + mul + div == 0:
        if result > maxmin[0]: maxmin[0] = result
        if result < maxmin[1]: maxmin[1] = result
        return
    
    if add:
        solution(idx+1,result+nums[idx], add-1, sub, mul, div)
    if sub:
        solution(idx+1,result-nums[idx], add, sub-1, mul, div)
    if mul:
        solution(idx+1,result*nums[idx], add, sub, mul-1, div)
    if div:
        solution(idx+1, int(result/nums[idx]), add, sub, mul, div-1)

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())
maxmin = [-1e9, 1e9]

solution(1, nums[0], add, sub, mul, div)
print(maxmin[0])
print(maxmin[1])