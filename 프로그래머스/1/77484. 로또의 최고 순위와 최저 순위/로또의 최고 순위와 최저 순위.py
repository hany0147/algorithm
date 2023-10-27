  
def solution(lottos, win_nums):
    zero_count = lottos.count(0)
    cnt = 0
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
    min_answer = cnt
    max_answer = cnt + zero_count
    
    answer = [check_score(max_answer), check_score(min_answer)]
    return answer

def check_score(n):
    if n == 6:
        return 1
    elif n == 5:
        return 2
    elif n == 4:
        return 3
    elif n == 3:
        return 4
    elif n == 2:
        return 5
    else:
        return 6
