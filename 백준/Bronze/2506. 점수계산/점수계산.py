N = int(input())
checks = list(map(int, input().split()))
prev_check_num = 0
result = []
prev_sum_score = 0
# 초기값 설정.

for check_num in checks:
    score = 0
    if check_num == 1: # 이번 점수를 맞췄다면
        if prev_check_num == False: # 이전 점수가 틀렸다면
            score = check_num # 스코어는 1점.
            result.append(score)
            prev_sum_score = 0
        elif prev_check_num == 1: # 이전 점수가 맞았다면
            prev_sum_score += 1
            score = check_num + prev_sum_score # 최종 점수는 '이전 합친 점수' + 현 점수
            result.append(score)
    else:
        result.append(check_num)
    prev_check_num = check_num

print(sum(result))