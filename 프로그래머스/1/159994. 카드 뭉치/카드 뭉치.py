from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    
    for g in goal:
        if len(cards1) != 0 and g == cards1[0]:
            cards1.popleft()
            continue
        if len(cards2) != 0 and g == cards2[0]:
            cards2.popleft()
            continue
        return "No"
    else:
        return "Yes"
            