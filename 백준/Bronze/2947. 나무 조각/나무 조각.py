lst = list(map(int, input().split()))

# print(lst) # [2, 1, 5, 3, 4] -> 리스트이므로 인덱스 사용 가능(0~5)
# 나무 조각은 5개라고 정해져 있다. 

sort_lst = sorted(lst)
# print(sort_lst) # [1, 2, 3, 4, 5]


while sort_lst != lst:
    for i in range(5):
        try:
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                print(*lst, sep = " ")
        except IndexError:
            continue