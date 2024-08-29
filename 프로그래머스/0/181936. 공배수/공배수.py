def solution(number, n, m):
    max_num = max(n, m)
    min_num = min(n, m)
    if max_num % min_num == 0:
        tmp = max_num
    else:
        tmp = n * m
    if number % tmp == 0:
        return 1
    return 0