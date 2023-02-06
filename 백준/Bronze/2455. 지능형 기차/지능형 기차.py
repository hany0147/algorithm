total = 0
lst = []
for _ in range(4):
    train_out, train_in = list(map(int, input().split()))
    total = total - train_out + train_in
    # print(f'#{_}: {total}')
    lst.append(total)

print(max(lst))