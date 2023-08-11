N, M = map(int, input().split())
arr = []

def recur(number, k):
    if number == M:
        print(*arr)
        return
    
    for i in range(k, N + 1):
        arr.append(i)
        recur(number + 1, i)
        arr.pop()

recur(0, 1)