T = int(input())
for _ in range(T):
    nums = list(map(int, input().split())) 
    # nums[0]은 학생  수 / 나머지는 N명의 점수

    N = nums.pop(0)

    avg_score = sum(nums) / N
    cnt = 0
    for num in nums:
        if num > avg_score:
            cnt += 1
    result = cnt / N * 100
    print(f'{result:.3f}%')