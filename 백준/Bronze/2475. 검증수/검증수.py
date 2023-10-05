arr = list(map(int, input().split()))

sum_arr = sum(list(map(lambda x: x * x, arr)))
print(sum_arr % 10)