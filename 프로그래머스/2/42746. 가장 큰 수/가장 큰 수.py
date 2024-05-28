# from itertools import permutations

def solution(numbers):
    numbers = list(map(str, numbers))
    
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    result = ''.join(numbers)
    return str(int(result)) 




    # numbers = list(map(str, numbers))
    # per = list(permutations(numbers))
    # max_num = max(''.join(p) for p in per)
    # print(max_num)