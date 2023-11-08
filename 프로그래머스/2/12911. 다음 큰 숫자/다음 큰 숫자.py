def solution(n):
    tmp = n 
    bin_n = bin(n).replace('0b', '')
    cnt_n = bin_n.count('1')
    while True:
        tmp += 1
        bin_tmp = bin(tmp).replace('0b', '')
        cnt_tmp = bin_tmp.count('1')
        
        if cnt_tmp == cnt_n:
            break
            
    return tmp