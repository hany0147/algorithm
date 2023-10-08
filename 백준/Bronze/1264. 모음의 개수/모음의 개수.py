str = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    tmp = input()
    if tmp == '#':
        break
    cnt = 0
    for i in tmp:
        if i in str:
            cnt += 1
    print(cnt)