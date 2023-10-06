string = input()
res = ''
for i in string:
    if 65 <= ord(i) <= 90:
        res += i.lower()
    elif 97 <= ord(i) <= 122:
        res += i.upper() 
print(res)