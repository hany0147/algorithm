def solution(n, arr1, arr2):
    
    arr1 = makeBinary(n, arr1)
    arr2 = makeBinary(n, arr2)
    
    new_arr = []
    
    for x in range(n):
        tmp = ""
        for y in range(n):
            if arr1[x][y] == 1 or arr2[x][y] == 1:
                tmp += "#" 
            else:
                tmp += " "
        new_arr.append(tmp)
        
    return new_arr


# 이진수 만드는 함수
def makeBinary(n, arr):
    res = []
    
    for i in arr:
        bin_arr = []
        while i >= 2:
            remain = i % 2
            i = i // 2
            bin_arr.append(remain)
        bin_arr.append(i)
        if len(bin_arr) != n:
            for _ in range(n - len(bin_arr)):
                bin_arr.append(0)
        bin_arr.reverse()
        res.append(bin_arr)

    return res