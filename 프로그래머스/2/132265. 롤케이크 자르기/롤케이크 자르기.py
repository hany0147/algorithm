from collections import Counter

def solution(topping):
    cnt = 0
    me = Counter(topping)
    brother = set()
    
    for i in topping:
        me[i] -= 1
        brother.add(i)
        if me[i] == 0:
            del me[i]
            
        if len(me) == len(brother):
            cnt += 1
    return cnt