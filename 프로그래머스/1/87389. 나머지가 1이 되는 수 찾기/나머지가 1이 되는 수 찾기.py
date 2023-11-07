def solution(n):
    for x in range(1, 1_000_001):
        if n % x == 1:
            answer = x
            break
    return answer