a, b = map(int, input().split())
a -= 1
tmp_a = 0

tmp_a += a

for i in range(1, 99):
    tmp_a += (a // (2 ** i)) * ((2 ** i) - (2 ** (i - 1)))


tmp_b = 0

tmp_b += b

for i in range(1, 99):
    tmp_b += (b // (2 ** i)) * ((2 ** i) - (2 ** (i - 1)))

print(tmp_b - tmp_a)