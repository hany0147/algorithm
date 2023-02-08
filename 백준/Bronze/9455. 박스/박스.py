T = int(input())

for t in range(T):

    M, N = list(map(int, input().split()))
    box = [list(map(int, input().split())) for _ in range(M)]
    # pprint(box)

    # 역-열 순회
    cnt = 0

    for y in range(N):    
        for x in range(M - 1, -1, -1):

            # 0. 박스를 찾았다.
            if box[x][y] == 1:

            # 1. 박스를 이동하라.
                while True:

                    # 2. 범위 체크
                    if x + 1 == M:
                        break
                    
                    # 3. 다음이 비어있는지
                    if box[x+1][y] == 1:
                        break

                    box[x][y] = 0
                    box[x+1][y] = 1
                    cnt += 1

                    x += 1
    print(cnt)