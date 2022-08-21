from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
board = [[0 for j in range(N)] for i in range(N)]
apple_l = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
move_l = [input().split() for i in range(L)]
dic = {int(key) : value for key, value in move_l}
snake = deque([[0,0]])
direction = {"right" : {"L" : "up", "D" : "down"}, "left" : {"L" : "down", "D" : "up"},
             "down" : {"L" : "right", "D" : "left"}, "up" : {"L" : "left", "D" : "right"}}

x = 0
y = 0
time = 0
state = "right"
while True:
    if time in dic:
        state = direction[state][dic[time]]
    if state == "right": y += 1
    elif state == "left": y -= 1
    elif state == "down": x += 1
    else: x -= 1
    time += 1
    if [x, y] in snake or (x >= N or x < 0 or y >= N or y < 0):
        break
    snake.append([x, y])
    if [x+1, y+1] in apple_l:
        apple_l.remove([x+1, y+1])
    else: snake.popleft()

print(time)