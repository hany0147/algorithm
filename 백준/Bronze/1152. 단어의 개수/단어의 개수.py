string = input()
if string != ' ':
    lst_string = list(string.strip().split(' '))
    print(len(lst_string))
else:
    print(0)