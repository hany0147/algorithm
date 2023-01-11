N = int(input())
num_list = []


for n in range(0, N + 1):
    num = 2**n
    num_list.append(num)

print(*num_list)