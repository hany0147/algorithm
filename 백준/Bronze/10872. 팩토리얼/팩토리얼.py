N = int(input())
fin = 1
if N > 0:
    while N > 0:
        fin = fin * N
        N = N - 1
    print(fin)
else:
    print(1)