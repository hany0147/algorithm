x, y, w, h = map(int, input().split())

res = min(abs(x - w), abs(y - h), x, y)
print(res)