import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())

coins = []
for _ in range(N):
    coins.append(int(input().rstrip()))
# print(coins)
result = 0
remainder = K
for coin in coins[::-1]:
    if coin <= K:
        result += remainder // coin # 몫
        remainder = remainder % coin
print(result)