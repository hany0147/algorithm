while True:
    strings = input()
    
    if strings == '.':
        break
    
    stack = []
    for string in strings:
        if string == '[' or string == '(':
            stack.append(string)
        elif string == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        elif string == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        
    if not stack:
        print('yes')
    else:
        print('no')