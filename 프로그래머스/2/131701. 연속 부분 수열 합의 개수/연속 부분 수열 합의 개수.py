def solution(elements):
    lst = set()
    n = len(elements)
    elements += elements
    tmp = 0
    for idx, num in enumerate(elements):
        tmp = num
        lst.add(tmp)
        for i in elements[idx + 1: idx + n]:
            tmp += i
            lst.add(tmp)
    return len(lst)
        
