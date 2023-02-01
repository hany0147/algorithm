h, m = list(map(int, input().split()))
c = int(input())
sum_m = m + c

# if m + LT >= 60: h = (m + LT) // 60 + h , m = (m + LT) % 60
# if h == 23: h = 0

if sum_m >= 60:
    t = (sum_m // 60) + h
    m = sum_m % 60
    if t >= 24:
        t = t - 24
        print(t, m)
    else:
        print(t,m)

else:
    m = sum_m
    print(h, m)