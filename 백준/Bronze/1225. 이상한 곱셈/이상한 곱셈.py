A, B = input().split()
A = list(A)
B = list(B)
B = sum(list(map(int, B)))
fin_sum_num = 0
for a in A:
    a = int(a)
    sum_n = a * B
    fin_sum_num += sum_n

print(fin_sum_num)