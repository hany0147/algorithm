from collections import Counter
strs = input().upper()

if len(strs) != 1:

    lst_strs = Counter(strs)

    if lst_strs.most_common(2)[0][1] == lst_strs.most_common(2)[1][1]:
        print('?')
    else:
        print(lst_strs.most_common(1)[0][0])
else:
    print(strs)