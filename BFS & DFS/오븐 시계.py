h, m = map(int, input().split())
cooking_t = int(input())

print("{} {}".format((h + (cooking_t + m) // 60) % 24 , (cooking_t + m) % 60) )