N = int(input())
nums = list(map(int, input().split()))
v = int(input())
cnt = 0
for num in nums:
    if num == v:
        cnt += 1
print(cnt)