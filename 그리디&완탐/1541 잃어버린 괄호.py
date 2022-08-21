import sys
input = sys.stdin.readline

s = input().strip()
result = ''
cnt = 0
for c in s:
    if c == '-' or c =='+':
        result = int(result)
        break
    result += c
    cnt += 1

num = '0'
minus = 0
for idx, c in enumerate(s[cnt:]):
    if c == '-' and not minus:
        minus = 1
        result += int(num)
        num = '0'
    elif c == '-' and minus:
        result -= int(num)
        num = '0'
    elif c == '+' and minus:
        result -= int(num)
        num = '0'
    elif c == '+' and not minus:
        result += int(num)
        num = '0'
    elif c != '-' and c != '+':
        num += c
    if idx == len(s[cnt:])-1:
        if minus: result -= int(num)
        else: result += int(num)
print(result)