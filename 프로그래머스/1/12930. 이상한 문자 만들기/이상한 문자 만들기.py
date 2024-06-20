def solution(s):
    lst = s.split(" ")
    answer = ''
    for idx, word in enumerate(lst):
        
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
                
        if idx != len(lst) - 1:
            answer += ' '
                
    return answer