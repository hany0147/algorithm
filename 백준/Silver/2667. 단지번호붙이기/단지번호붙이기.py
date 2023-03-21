from pprint import pprint
import sys
input = sys.stdin.readline

N = int(input())
group = []

for _ in range(N):
    group.append(list(map(int, input().rstrip())))
# pprint(group)


def dfs(x, y, i):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if group[x][y] == 1:
        i.append('house')
        group[x][y] = 0
        dfs(x, y + 1, i)
        dfs(x, y - 1, i)
        dfs(x + 1, y, i)
        dfs(x - 1, y, i)
        return True
    return False
result = 0
house_num_lst = []
calculation_lst = []
fin_lst = []
for x in range(N):
    for y in range(N):
        if dfs(x, y, house_num_lst) == True:
            result += 1
            calculation_lst.append(len(house_num_lst))
print(result)

for n in range(len(calculation_lst)):
    if calculation_lst[n] != calculation_lst[0]:
        fin_lst.append(calculation_lst[n] - calculation_lst[n - 1])
    else:
        fin_lst.append(calculation_lst[n])

fin_lst.sort()
for _ in fin_lst:
    print(_)