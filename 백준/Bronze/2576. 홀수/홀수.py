num_lst = []
sum_num = 0
min_num_lst = []

for i in range(7):
    num = int(input())
    num_lst.append(num)

# print(num_list) # [12, 77, 38, 41, 53, 92, 85]

for num in num_lst:
    if num % 2 == 1:
        sum_num += num
        min_num_lst.append(num)
        
if sum_num == 0:
    print(-1)
else:
    print(sum_num, min(min_num_lst), sep = '\n')
