def Rev(strings):
    strings = str(strings)
    new_stirng = ''
    for string in strings[::-1]:
        new_stirng += string
    
    return int(new_stirng)


a, b = list(map(int, input().split()))

print(Rev(Rev(a) + Rev(b)))