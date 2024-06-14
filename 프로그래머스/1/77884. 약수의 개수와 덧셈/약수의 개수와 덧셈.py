def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        cnt = divisor(i)
        
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer


def divisor(num):
    cnt_set = set()
    cnt_set.add(1)
    cnt_set.add(num)
    
    for i in range(2, int(num // 2) + 1):
        if num % i == 0:
            cnt_set.add(i)
            
    return len(cnt_set)