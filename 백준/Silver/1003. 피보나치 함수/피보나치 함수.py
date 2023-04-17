t = int(input())
zero = [1, 0, 1]
first = [0, 1, 1]

def fibonacci(n):
    if n >= len(zero):
        for i in range(len(zero), n + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            first.append(first[i - 1] + first[i - 2])
    print(zero[n], first[n])

for _ in range(t):
    n = int(input())
    fibonacci(n)