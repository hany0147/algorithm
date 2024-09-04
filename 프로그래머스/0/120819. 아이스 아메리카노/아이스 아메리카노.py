def solution(money):
    answer = []
    coffee = money // 5500
    return_money = money % 5500
    answer.append(coffee)
    answer.append(return_money)
    return answer