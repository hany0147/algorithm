def solution(arr):
    tmp = 1
    com = 0
    i = 2
        # 종료조건 
        # 1. i보다 모든 수가 작으면, 끝낸다.
    while True:
        if com == len(arr):
            break
            
        cnt = 0
        com = 0
        for idx in range(len(arr)):
            if arr[idx] % i == 0:
                arr[idx] = arr[idx] // i
                cnt += 1
            if arr[idx] < i:
                com += 1
        if cnt > 0:
            tmp *= i
            
        else:
            i += 1
            
    for idx in range(len(arr)):
        tmp *= arr[idx]
            

    return tmp