score_lst = []
sum_mush = 0
mush_lst = []
for _ in range(10):
    mush_lst.append(int(input()))


for mushroom in mush_lst:
    sum_mush += mushroom
    score_lst.append(sum_mush)
    if sum_mush >= 100:
        break

# print(score_lst)

if len(score_lst) >= 2:
    score_lst.sort(reverse = True)

    fin1 = abs(100 - score_lst[0])
    fin2 = abs(100 - score_lst[1])
    # print(fin1, fin2)

    if fin1 > fin2:
        print(score_lst[1])
    elif fin1 < fin2:
        print(score_lst[0])
    elif fin1 == fin2:
        print(score_lst[0])
else:
    print(score_lst[0])