def solution(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    
    answer = len(s1 & s2)
    return answer