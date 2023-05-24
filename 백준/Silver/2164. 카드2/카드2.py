from collections import deque

n = int(input())
d = deque([])
for i in range(1, n + 1):
    d.append(i)

while True:
    if len(d) == 1:
        break
    d.popleft()
    d.append(d.popleft())

print(*d)