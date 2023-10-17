a, b = map(int, input().split())
a -= 1
b -= 1
res = abs(a // 4 - b // 4) + abs(a % 4 - b % 4)
print(res)