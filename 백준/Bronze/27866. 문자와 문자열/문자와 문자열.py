strings = input()
n = int(input())
cnt = 0
for string in strings:
    cnt += 1
    if cnt == n:
        print(string)
        break