'''
prices: 배열(주식가격)
가격이 떨어지지 않은 기간 몇 초인가.
기준 초 
-> 기준 초보다 떨어지지않으면 cnt를 올린다.



'''
from collections import deque

def solution(prices):
    prices = deque(prices)
    answer = []
    
    while prices:
        price = prices.popleft()
        sec = 0
        for p in prices:
            sec += 1
            if price > p:
        
                break
        answer.append(sec)
            
    return answer


    # answer = []
    # for i in range(len(prices)):
    #     cnt = 0
    #     for j in range(i + 1, len(prices)):
    #         if prices[i] <= prices[j]:
    #             cnt += 1
    #     answer.append(cnt)
