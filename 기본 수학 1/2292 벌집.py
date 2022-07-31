import sys 
input = sys.stdin.readline

n = int(input())
result = 0
i = 1
while True:
    if result >= n-1: break
    result += 6*i
    i+=1
print(i)