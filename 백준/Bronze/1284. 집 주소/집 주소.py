while True:
    n = input()
    if n == '0':
        break
    n = list(map(int, n))
    cnt = 0
    for i in n:
        if i == 1:
            cnt += 2
        elif i == 0:
            cnt += 4
        else:
            cnt += 3

    cnt += (len(n) + 1)
    print(cnt)