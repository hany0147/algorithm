N = int(input())
star = '*'
empty = ' ' * (N - 1)
string = star + empty
# print(string)
for n in range(N):
    new_string = string.replace(' ', '*', n)
    rev_strings = list(reversed(new_string))
    print(*rev_strings, sep = '')