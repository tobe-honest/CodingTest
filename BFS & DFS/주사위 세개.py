dice_l = list(map(int, input().split()))
prize = 0

if dice_l[0] == dice_l[1] == dice_l[2]: prize = 10000 + dice_l[0] * 1000
elif dice_l[0] == dice_l[1]: prize = 1000 + dice_l[0] * 100 
elif dice_l[0] == dice_l[2]: prize = 1000 + dice_l[0] * 100
elif dice_l[1] == dice_l[2]: prize = 1000 + dice_l[1] * 100
else: prize = max(dice_l) * 100

print(prize)