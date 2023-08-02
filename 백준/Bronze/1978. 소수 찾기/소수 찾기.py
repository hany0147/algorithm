
n = int(input())
lst = list(map(int, input().split()))

cnt = 0
for number in lst:
    if number == 1:
        continue
    flag = True
    for i in range(2, number):
        if number % i == 0:
            flag = False
    if flag == True:
        cnt += 1

print(cnt)