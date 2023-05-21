import sys
input = sys.stdin.readline

n = int(input())
friends = []
for _ in range(n):
    friends.append(list(input().rstrip()))
# print(friends)
visited = [[0] * n for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            if friends[a][b] == 'Y' or (friends[a][k] == 'Y' and friends[k][b] == 'Y'):
                visited[a][b] = 1

res = 0
for a in range(n):
    cnt = 0
    for b in range(n):
        if visited[a][b] == 1:
            cnt += 1
    res = max(res, cnt)
print(res)