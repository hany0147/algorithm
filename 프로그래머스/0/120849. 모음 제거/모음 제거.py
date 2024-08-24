def solution(my_string):
    answer = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for string in my_string:
        if string not in vowels:
            answer += string
    return answer