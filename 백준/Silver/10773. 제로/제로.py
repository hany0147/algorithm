K = int(input())
lst = []

for k in range(K):
    num = int(input())
   
    if num != 0:
        lst.append(num)
    elif num == 0:
        lst.pop()
    
sum_lst = sum(lst)
print(sum_lst)