
def solution(storey):
    answer = 0
    
    while storey != 0:
        reminder = storey % 10
        
        # 5보다 크면
        if reminder > 5:
            answer += (10 - reminder)
            storey += 10
        # 5보다 작다면
        elif reminder < 5:
            answer += reminder
        # 5와 같다면
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += reminder
        
        storey //= 10
        
        
    return answer