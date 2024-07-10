from collections import defaultdict

def solution(weights):
    answer = 0
    siso = defaultdict(int)
    
    for w in weights:
        answer += siso[w] + siso[w * 2] + siso[w / 2] + siso[w * 2 / 3] + siso[w * 3 / 2] + siso[w * 3 / 4] + siso[w * 4 / 3]
        siso[w] += 1
    
    return answer