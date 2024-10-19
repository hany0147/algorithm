def solution(n):

    trinary = make_trinary(n)

    return make_reverse_tri(trinary)

def make_trinary(num):
    lst = []
    while num > 0:
        tmp = num % 3
        num //= 3
        lst.append(tmp)
    return lst

def make_reverse_tri(lst):
    lst = lst[::-1]
    res = 0
    for idx in range(len(lst)):
        res += (lst[idx] * (3 ** idx))      
    return res

