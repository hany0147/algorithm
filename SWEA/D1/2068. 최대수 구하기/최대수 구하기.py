T2 = int(input())

for t2 in range(1, T2 + 1):
    result = 0
    nums = list(map(int, input().split()))
    for i in nums:
        if i > result:
            result = i
    print(f'#{t2} {result}')