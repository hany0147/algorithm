def solution(s):
    bin_cnt = 0
    zero_cnt = 0
    
    while s != '1':
        zero_cnt += s.count('0')
        s = str(s).replace('0', '')
        s = bin(len(s)).replace('0b', '')
        bin_cnt += 1
    
    answer = [bin_cnt, zero_cnt]
    return answer