string = input().split('-')
res = 0
# 2. 각 부분들끼리 합하여라
for first in string[0].split('+'):
    res += int(first)
for etc in string[1::]:
    for second in etc.split('+'):
        res -= int(second)
print(res)
