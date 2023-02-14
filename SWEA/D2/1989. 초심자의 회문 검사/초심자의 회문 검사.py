T = int(input())
for t in range(1, T + 1):
    word = input().rstrip()

    if word[::] == word[::-1]:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')