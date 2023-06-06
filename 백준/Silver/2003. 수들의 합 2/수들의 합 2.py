import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
sum_ = lst[0]
left = 0
right = 1
cnt = 0

while True:
    if sum_ < m:
        if right < n:
            sum_ += lst[right]
            right += 1
        else:
            break
    elif sum_ == m:
        cnt += 1
        sum_ -= lst[left]
        left += 1
    else:
        sum_ -= lst[left]
        left += 1
print(cnt)