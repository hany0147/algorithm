def solution(s):
    length = len(s)
    if length % 2 == 0:
        return s[(len(s) // 2) - 1: (len(s) // 2) + 1]
    else:
        return s[len(s) // 2]