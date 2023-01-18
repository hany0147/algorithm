T = int(input())

for t in range(T):
    strings = input().split()
    sort_str = [strings[i][::-1] for i in range(len(strings))]
    print(*sort_str, sep=" ")