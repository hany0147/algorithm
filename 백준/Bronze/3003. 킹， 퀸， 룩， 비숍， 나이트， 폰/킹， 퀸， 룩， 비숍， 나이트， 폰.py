
nums = list(map(int, input().split()))

need_things = [(1 - nums[0]), (1 - nums[1]), (2 - nums[2]), (2 - nums[3]), (2 - nums[4]), (8 - nums[5])]

print(*need_things)