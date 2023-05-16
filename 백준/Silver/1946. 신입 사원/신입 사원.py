
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    test = []
    n = int(input())
    for _ in range(n):
        paper, review = map(int, input().split())
        test.append((paper, review))

    test.sort()
    # print(test)

    win = test[0][1]
    cnt = 1
    for i in range(1, n):
        if test[i][1] < win:
            win = test[i][1]
            cnt += 1
    print(cnt)