'''
i열 미만이면 j행의 값을 따르고
i열 이상일경우, i행의 값을 따른다.
'''


def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        a = i // n
        b = i % n
        if a >= b:
            answer.append(a + 1)
        else:
            answer.append(b + 1)


    return answer