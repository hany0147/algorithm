def solution(arr):
    min_num = min(arr)
    tmp = []
    for i in arr:
        if i != min_num:
            tmp.append(i) 
    
    if len(tmp) == 0:
        return [-1]
    else:
        return tmp