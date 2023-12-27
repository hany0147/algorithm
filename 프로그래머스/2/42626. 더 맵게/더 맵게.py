# 가장 맵지 않은 => 최소힙

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        # 모든 음식이 K값 이상 일때
        if scoville[0] >= K:
            return answer
        # scoville이 하나 남은 경우
        if len(scoville) == 1:
            return -1
        
        # 아니라면,
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new = first + (second * 2)
        heapq.heappush(scoville, new)
        answer += 1
        
            
    return answer