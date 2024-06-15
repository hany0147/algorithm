def solution(price, money, count):
    total_count = sum([i for i in range(1, count + 1)])
    total_price = total_count * price
    answer = total_price - money
    if answer <= 0:
        return 0
    return answer