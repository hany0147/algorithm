def solution(n):
    ans = 1
    for i in range(1, n // 2 + 1):
        total = 0
        while total < n:
            total += i
            # a가 n이 되는 순간 멈춰라.
            if total == n:
                ans += 1
                break
            i += 1
            
    return ans
