import sys
input = sys.stdin.readline

N = int(input())
l = [-1] + list(map(int, input().split()))
student_n = int(input())
student_info = [list(map(int, input().split())) for i in range(student_n)]

for sex, number in student_info:
    if sex == 1:
        i = 1
        while number * i <= N:
            l[number * i] = l[number * i] - 1 if l[number * i] else l[number * i] + 1
            i += 1
    if sex == 2:
        left = number - 1
        right = number + 1
        while True:
            if left < 1 or right > N or l[left] != l[right] :
                left += 1
                right -= 1
                break
            left -= 1
            right += 1
        
        if number == 1 or number == N:
            l[number] = l[number] -1 if l[number] else l[number] + 1
            continue
        
        for i in range(left, right+1):
            l[i] = l[i] -1 if l[i] else l[i] + 1


for idx, v in enumerate(l[1:]):
    if idx == N-1 or (idx % 20 == 19 and idx != 0):
        print(v)
    else: print(v, end=" ")