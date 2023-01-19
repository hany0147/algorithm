N = int(input())

name_dict = {}

for i in range(N):
    s = input().split()
    name_dict[s[0]] = s[1]

for key in sorted(name_dict, reverse = True):
    if name_dict[key] == 'enter':
        print(key, sep = '\n')