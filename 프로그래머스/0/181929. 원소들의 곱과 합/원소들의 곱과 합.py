def solution(num_list):
    multi = 1
    for n in num_list:
        multi *= n
    
    _sum = sum(num_list) ** 2
    
    if multi < _sum:
        return 1
    else:
        
        return 0