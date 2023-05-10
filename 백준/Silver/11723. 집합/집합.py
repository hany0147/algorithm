import sys
input = sys.stdin.readline
s = set()
m = int(input())
for _ in range(m):
    lst = list(input().split())
    if len(lst) == 2:
        operation = lst[0]
        x = int(lst[1])
    elif len(lst) == 1:
        operation = lst[0]
        
    if operation == 'add':
        if x in s:
            continue
        else:
            s.add(x)
    elif operation == 'remove':
        if x not in s:
            continue
        else:
            s.remove(x)
    elif operation == 'check':
        if x in s:
            print(1)
        else:
            print(0)
    elif operation == 'toggle':
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    elif operation == 'all':
        s.clear()
        s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 ,20}
    elif operation == 'empty':
        s.clear()