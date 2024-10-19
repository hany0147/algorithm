def solution(nums):
    nums_set = set(nums)
    get_max_nums = len(set(nums))
    
    if get_max_nums > len(nums) // 2:
        return len(nums) // 2
    else:
        return get_max_nums