def solution(number, limit, power):
    answer = 0
    
    
    def 약수(num):
        tmp = 0
        double = 0
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                tmp += 2
            if num ** 0.5 == i:
                double += 1
        return tmp - double
    
    for num in range(1, number + 1):
        attack = 약수(num)
        
        if attack > limit:
            attack = power
        answer += attack
        
    return answer