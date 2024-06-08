def solution(babbling):
    can = ['aya', 'ye', 'woo', 'ma']
    cnt = 0
    # 단어 하나를 담는 tmp 리스트
    for babble in babbling:
        tmp = []
        string = ""
        for word in babble:
            string += word
            if string in can:
                
                if len(tmp) > 0 and tmp[-1] == string:
                    break
                
                tmp.append(string)
                string = ""
                
        if len(tmp) > 0:
            tmp = "".join(tmp)
            if len(babble) == len(tmp):
                cnt += 1
            
    print(cnt)
        
    return cnt