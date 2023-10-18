n = int(input())
f = int(input())

tmp = n - (n % 100)
res = 0

for i in range(100):
    if (tmp + i) % f == 0:
        res = i
        break

if res == 0:
    print('00')
elif 0 < res < 10:
    print(f'0{res}')
else:
    print(res)