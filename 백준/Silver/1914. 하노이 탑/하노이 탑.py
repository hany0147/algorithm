def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return
    hanoi(n - 1, start, 6-start-end) # 1개를 제외한 나머지 (n-1) 원판은 2번으로 옮겨야 한다.
    print(start, end)
    hanoi(n - 1, 6-start-end, end)

n = int(input())
result = 2**n -1
print(result)
if n <= 20:
    hanoi(n, 1, 3)