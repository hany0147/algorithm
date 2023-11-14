from collections import deque

def solution(s):
    def check(s):
        # [, (, { 가 들어오면, stack에 쌓는다.
        # ], ), } 가 들어오면 stack[-1]과 일치할 경우, stack[-1]을 제거한다.
        # 끝까지 stack이 비지 않는다면, return 0, 빈 다면, return 1을 하라.
        stack = []
        for i in s:
            if i == '[' or i == '(' or i == '{':
                stack.append(i)
            else:
                if stack:
                    if i == ']' and stack[-1] == '[':
                        stack.pop()
                    elif i == ')' and stack[-1] == '(':
                        stack.pop()
                    elif i == '}' and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        else:
            return True
    
    cnt = 0
    s = deque(s)
    x = len(s)
    
    for num in range(x):
        if num > 0:
            s.append(s.popleft())
        if check(s):
            cnt += 1
        
    return cnt