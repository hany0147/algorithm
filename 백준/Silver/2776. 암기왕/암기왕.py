import sys
input = sys.stdin.readline

def bs(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
    return 0

t = int(input())
for _ in range(t):
    n = int(input()) 
    arr = sorted(list(map(int, input().split()))) #수첩1(arr)
    m = int(input()) #수첩2(targets)
    targets = list(map(int, input().split()))
    for target in targets:
        print(bs(arr, target, 0, n - 1))