person_cnt_by_meter, place = list(map(int, input().split()))
standard = person_cnt_by_meter * place

arr = list(map(int, input().split())) 
res_lst = []

for i in arr:
    res = i - standard
    res_lst.append(res)

print(*res_lst)