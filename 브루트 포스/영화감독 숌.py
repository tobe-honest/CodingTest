import sys
import re
N = int(sys.stdin.readline())
base = 1666
cnt = 1

while True:
    if N == 1:
        print(666)
        break
    if re.findall('666+',str(base)):
        cnt += 1
    if cnt == N:
        print(base)
        break
    base += 1