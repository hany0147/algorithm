N = int(input())
mv_cnt = 0

# 완전 탐색

for i in range(666,2666800):
    str_i = str(i)
    if '666' in str_i:
        mv_cnt += 1

    if mv_cnt == N:
        break

print(i)