n = int(input())
res = 0
for _ in range(n):
    strings = input()
    memory_lst = []
    cnt = 0
    for string in strings:
        if string not in memory_lst:
            cnt += 1
            memory_lst.append(string)
        elif string in memory_lst and memory_lst[-1] != string:
            cnt = 0
            break
    if cnt > 0:
        res += 1

print(res)