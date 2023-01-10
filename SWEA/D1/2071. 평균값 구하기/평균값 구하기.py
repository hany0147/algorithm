T = int(input())

for t in range(1, T + 1):
    nums = list(map(int, input().split()))
    average = round(sum(nums) / 10) 
    print(f'#{t} {average}')
