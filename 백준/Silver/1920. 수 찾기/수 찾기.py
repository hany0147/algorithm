import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
targets= list(map(int, input().split()))

# 타겟을 하나씩 뽑아서
# 이진탐색 while문에 집어 넣는다.
# start, mid, end
def binary_search(arr, target, start, end):
    # 끝이 스타트보다 작으면 멈춰라
    while start <= end:
        mid = (start + end) // 2
        # 중간값이 목표값과 같으면 중간값을 산출하고 종료
        if arr[mid] == target:
            return 1
        # 중간값이 목표값보다 크면 end 왼쪽으로 이동
        elif arr[mid] > target:
            end = mid - 1
        # 중간값이 목표값보다 작으면 start 오른쪽으로 이동
        else:
            start = mid + 1
    # while문이 끝나도 없으면 0 산출
    return 0

for target in targets:
    print(binary_search(arr, target, 0, n - 1))