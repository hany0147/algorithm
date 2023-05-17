import sys
input = sys.stdin.readline
n, k = map(int, input().split())
children = list(map(int, input().split()))
cost = []
for i in range(1, n):
    cost.append(children[i] - children[i - 1])
cost.sort(reverse=True)
# print(cost)
print(sum(cost[k - 1:]))