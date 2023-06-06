import sys
from collections import defaultdict
input = sys.stdin.readline

n, d, k, c = map(int, input().split()) # n: 접시수, d: 초밥가짓수, k:연속 먹는 접시 수, c: 쿠폰 번호
sushi = []
for _ in range(n):
    sushi.append(int(input()))
sushi.extend(sushi)

start = 0
end = 0
dict = defaultdict(int)
res = 0

dict[c] += 1

while end < k:
    dict[sushi[end]] += 1
    end += 1

while end < len(sushi):
    res = max(res, len(dict))

    dict[sushi[start]] -= 1
    if dict[sushi[start]] == 0:
        del dict[sushi[start]]
    dict[sushi[end]] += 1
    start += 1
    end += 1
print(res)