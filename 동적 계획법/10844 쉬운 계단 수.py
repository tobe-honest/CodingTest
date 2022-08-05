import sys
input = sys.stdin.readline

N = int(input())
memo = [[0 for j in range(10)] for i in range(101)]
memo[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            memo[i][0] = memo[i-1][1] # 0이 맨 뒤에 올 때는 앞에 1밖에 못오니까 앞에 1이 오는 경우만 생각
        elif j == 9:
            memo[i][9] = memo[i-1][8] # 9가 맨 뒤에 올 때는 앞에 8밖에 못오니까 앞에 8이 오는 경우만 생각
        else:
            # 1~8이 맨 뒤에 오면 앞에 올 수 있는 수가 2개씩 존재
            # 그 2개는 현재 자신의 수-1, 자신의 수+1
            # 따라서 두 수가 오는 경우를 합해줘야 함
            memo[i][j] = memo[i-1][j-1] + memo[i-1][j+1]
print(sum(memo[N]) % 1000000000)