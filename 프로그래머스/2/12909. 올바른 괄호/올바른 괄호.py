def solution(items):
    stack = []
    for item in items:
        if item == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True