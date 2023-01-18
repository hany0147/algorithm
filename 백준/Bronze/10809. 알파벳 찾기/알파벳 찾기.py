strings = input()
alp_list = []

for i in range(97, 123):
    alp = chr(i)
    if alp in strings:
        alp_list.append(strings.find(alp))
    else:
        alp_list.append(-1)


print(*alp_list, sep = " ")