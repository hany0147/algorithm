from itertools import combinations

def solution(nums):
    answer = 0
    nums = list(map(lambda x: sum(x), combinations(nums, 3)))

    for num in nums:
        answer += is_prime(num)


    return answer

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True