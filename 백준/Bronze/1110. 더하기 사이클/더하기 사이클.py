N = input()
res = 0
cnt = 0
copy_N = int(N)

if int(N) == 0:
    print(1)
else:
    while int(N) != int(res):
        if copy_N < 10:
            copy_N = "0" + str(copy_N)           
        num = 0 
        n_list = [] 
        for n in str(copy_N): 
            n_list.append(n)
        num = int(n_list[0]) + int(n_list[1])
        res = n_list[1] + str(num)[-1]
        cnt += 1
        copy_N = int(res)
        
    print(cnt)