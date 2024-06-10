from math import floor


def solution(str1, str2):
    adjust_str1 = adjust_str(str1)
    adjust_str2 = adjust_str(str2)
    same = set()
    same_set = 0
    
    for word in adjust_str1:
        if word in adjust_str2:
            same.add(word)
    
    for s in same:
        same_set += min(adjust_str1.count(s), adjust_str2.count(s))
        
    sum_set = len(adjust_str1) + len(adjust_str2) - same_set

    if same_set == 0 and sum_set == 0:
        tmp = 1
    else:
        tmp = same_set / sum_set
    
    answer = floor(tmp * 65536)
    
    return answer

def adjust_str(string):
    tmp_lst = []
    
    for i in range(1, len(string)):
        tmp = (string[i - 1] + string[i]).upper()
        if tmp.isalpha():
            tmp_lst.append(tmp)
    
    return tmp_lst
