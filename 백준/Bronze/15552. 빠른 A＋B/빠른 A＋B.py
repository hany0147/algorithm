import sys

# sys.stdin = open('6.txt')
T = int(sys.stdin.readline())

for t in range(T):
    A, B = list(map(int, sys.stdin.readline().rstrip().split()))
    print(A + B)