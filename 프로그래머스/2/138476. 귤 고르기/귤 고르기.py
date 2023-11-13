from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    n = max(tangerine)
    lst = [[_ , 0]  for _ in range(n + 1)]

    for i in tangerine:
        lst[i][1] += 1 

    lst.sort(key=lambda x: x[1], reverse=True)

    tmp = []
    
    for idx, cnt in lst:
        if k <= 0:
            break
        k -= cnt
        tmp.append(idx)

    return(len(tmp))