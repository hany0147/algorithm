def solution(arr, divisor):
    answer = [i for i in sorted(arr) if i % divisor == 0]
    
    if len(answer) == 0:
        return [-1]
    
    return answer