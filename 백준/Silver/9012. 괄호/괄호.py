T = int(input())


# 
for t in range(T):
    PS = input()

    # PS의 개수가 3

    while len(PS) > 1:
        if '()' in PS:
            strip_PS = PS.replace('()', "")
            PS = strip_PS
        else:
            break
        
    
    
    if PS == '()' or PS == '':
        print('YES')
    else:
        print('NO')