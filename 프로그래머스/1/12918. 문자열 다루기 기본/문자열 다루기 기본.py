def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False;
    if not s.isnumeric():
        return False
    return True