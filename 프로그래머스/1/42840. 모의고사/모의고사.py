# 수열 만드는 함수
def make_arr(arr):
    arr = (arr * (cnt // len(arr))) + arr[:cnt % len(arr)]
    return arr


def solution(answers):
    tmp = []
    global cnt
    cnt = len(answers)
    
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    first = make_arr(first)
    second = make_arr(second)
    third = make_arr(third)
    
    
    # 문제를 채점하는 함수
    def is_correct(arr):
        count = 0;
        for idx in range(cnt):
            if arr[idx] == answers[idx]:
                count += 1
        return count
    
    for people in [first, second, third]:
        tmp.append(is_correct(people))
        
    answer = []
    
    max_num = max(tmp)
    
    for idx, success_cnt in enumerate(tmp):
        if success_cnt == max_num:
            answer.append(idx + 1)
    return answer




    
    
    