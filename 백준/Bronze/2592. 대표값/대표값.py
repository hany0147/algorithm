freq_dict = {}
sum_num = 0

for i in range(10):
    num = int(input())
    sum_num += num
    if num not in freq_dict:
        freq_dict[num] = 1
    else:
        freq_dict[num] += 1

print(int(sum_num / 10))

freq_lst = []
for key, value in freq_dict.items():
    freq_lst.append((key, value))
freq_lst.sort(key = lambda x : x[1], reverse = True)
print(freq_lst[0][0])