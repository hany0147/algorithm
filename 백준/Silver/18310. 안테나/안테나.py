import sys
input = sys.stdin.readline
n = int(input())
houses = sorted(list(map(int, input().split())))
print(houses[(n - 1) // 2])