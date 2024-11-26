from functools import reduce

def solution(num_list):
    len_lst = len(num_list)
    if len_lst >= 11:
        return sum(num_list)
    else:
        return reduce(lambda x, y: x * y, num_list)
    