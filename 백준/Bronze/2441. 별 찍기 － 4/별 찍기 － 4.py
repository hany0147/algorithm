N = int(input())
star = '*' * N
for n in range(N):
    new_star = star.replace('*', ' ', n)
    print(new_star)