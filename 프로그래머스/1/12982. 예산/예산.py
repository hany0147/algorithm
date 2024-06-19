def solution(d, budget):
    tmp = 0
    cnt = 0
    d.sort()
    for i in d:
        if tmp + i > budget:
            break
        tmp += i
        cnt += 1
     
    return cnt