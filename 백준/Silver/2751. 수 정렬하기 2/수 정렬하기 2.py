import sys
input = sys.stdin.readline
sort_lst = []
n = int(input())
for _ in range(n):
    sort_lst.append(int(input()))
sort_lst.sort()
for i in sort_lst:
    print(i)