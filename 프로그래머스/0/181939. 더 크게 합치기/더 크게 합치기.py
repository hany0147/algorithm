def solution(a, b):
    _a = cal(a, b)
    _b = cal(b, a)
    
    if _a >= _b:
        return _a
    else:
        return _b



def cal(a, b):
    return int(str(a) + str(b))