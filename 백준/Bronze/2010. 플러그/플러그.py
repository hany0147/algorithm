import sys
input = sys.stdin.readline
N = int(input())
lst = []

for _ in range(N):
    lst.append(int(input()))


result = sum(lst) - (N - 1)
print(result)