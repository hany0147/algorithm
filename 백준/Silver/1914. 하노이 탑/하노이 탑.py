def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
        return
    hanoi(n - 1, a, c, b) # n-1개의 원판은 b로 이동
    # 맨 아래 마지막으로 남은 원판은 c로 이동
    print(a, c)
    # b에 있는 원반 n - 1개를 c로 이동시켜라
    hanoi(n - 1, b, a, c)

n = int(input())
result = 2**n -1
print(result)
if n <= 20:
    hanoi(n, 1, 2, 3)
