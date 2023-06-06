import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
sum_ = lst[0]
start = 0
end = 1
cnt = 0

while True:
    if sum_ < m:
        if end < n:
            sum_ += lst[end]
            end += 1
        else:
            break
    elif sum_ == m:
        cnt += 1
        sum_ -= lst[start]
        start += 1
    else:
        sum_ -= lst[start]
        start += 1
print(cnt)