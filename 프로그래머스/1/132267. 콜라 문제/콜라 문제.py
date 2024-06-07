def solution(a, b, n):
    answer = 0
    
    while n >= a:
        tmp = (n // a) * b
        remain = n % a
        answer += tmp
        n = tmp + remain
        
    
    
    return answer