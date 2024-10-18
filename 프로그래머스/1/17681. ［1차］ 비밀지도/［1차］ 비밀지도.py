def solution(n, arr1, arr2):
    new_arr = []
    
    def make_bin(num):
        tmp = []
        while num >= 1:
            tmp.append(num % 2)
            num //= 2

        need_zero = n - len(tmp)
        
        if need_zero > 0:
            for i in range(need_zero):
                tmp.append(0)
        
        return tmp[::-1]
    
    for num1, num2 in zip(arr1, arr2):
        tmp_str = ""
        for new_num1, new_num2 in zip(make_bin(num1), make_bin(num2)):
            if new_num1 + new_num2 >= 1:
                tmp_str += "#"
            else:
                tmp_str += " "
    
        new_arr.append(tmp_str)

    return new_arr

