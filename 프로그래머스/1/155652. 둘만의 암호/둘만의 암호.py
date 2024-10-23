def solution(s, skip, index):
    answer = ''
    for char in s:
        count = 1
        new_char = ord(char)
        while count <= index:
            new_char += 1
            
            if new_char > ord('z'):
                new_char = ord('a')
                
            if chr(new_char) not in skip:
                count += 1

            
        answer += chr(new_char) 
        
    return answer