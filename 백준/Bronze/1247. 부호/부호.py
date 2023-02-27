import sys
input = sys.stdin.readline


for _ in range(3):
    fin = 0
    N = int(input())
    for _ in range(N):
        n = int(input())
        fin += n
    if fin == 0:
        print(0)
    elif fin > 0:
        print('+')
    else:
        print('-')