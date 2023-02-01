N = int(input())
max_n = 0
for n in range(4, N + 1):
    str_n = str(n)
    if '1' not in str_n and '2' not in str_n and '3' not in str_n and '5' not in str_n and '6' not in str_n and '8' not in str_n and '9' not in str_n and '0' not in str_n:
        if max_n < n <= N:
                max_n = n

print(max_n)