import sys
input = sys.stdin.readline
k, n = map(int, input().split()) # k: 기존 랜선 개수, n: 필요 랜선 개수 (k<=n)
cables = [int(input()) for _ in range(k)]

start = 1
end = max(cables)

while True:
    if end < start:
        break
    mid = (start + end) // 2
    cnt = 0
    for cable in cables:
        cnt += cable // mid
        
    # 만약 cnt의 개수가 n보다 작다면, end를 왼쪽으로 옮기고
    if cnt < n:
        end = mid - 1
    # cnt의 개수가 n보다 크거나 같으면 start를 오른쪽으로 옮긴다.
    else:
        start = mid + 1
print(end)