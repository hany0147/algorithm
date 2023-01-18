strings = input()
alp_list = []

for i in range(97, 123):
    alp = chr(i)
    alp_list.append(strings.find(alp))


print(*alp_list, sep = " ")