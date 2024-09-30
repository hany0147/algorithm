def solution(my_string, is_suffix):
    answer = ''
    for idx in range(len(my_string)):
        answer = ''
        if idx == len(my_string) - 1:
            answer = my_string[-1]
        else:
            answer = my_string[idx + 1 : len(my_string)]
        
        if answer == is_suffix:
            return 1
        
    return 0