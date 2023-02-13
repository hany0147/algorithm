def rev(int_i):
    strings = str(int_i)
    new_string = ''
    for string in strings[::-1]:
        new_string += string
    return int(new_string)


a, b = list(map(int, input().split()))

if rev(a) > rev(b):
    print(rev(a))
elif rev(a) < rev(b):
    print(rev(b))
