while True:
    nums = list(map(int, input().split()))
    if sum(nums) > 0:
        print(sum(nums))
    else:
        break