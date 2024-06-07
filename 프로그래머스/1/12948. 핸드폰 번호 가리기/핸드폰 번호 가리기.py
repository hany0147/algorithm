def solution(phone_number):
    answer = phone_number[-4:]
    tmp = "*" * (len(phone_number) - 4)
    answer = tmp + answer
        
    return answer