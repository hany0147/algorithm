from pprint import pprint

# 델타검색을 위한 dict
dir_dict = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (1, 0),
    'T': (-1, 0),
    'RT': (-1, 1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (1, -1)
}

# 입력
king, stone, N = input().split()
kx, ky = 8 - int(king[1]), ord(king[0]) - 65
sx, sy = 8 - int(stone[1]), ord(stone[0]) - 65

# 체스판 초기 설정
chess = [[0]* 8 for _ in range(8)]
# pprint(chess)

# 두 체스 위치 선정
chess[kx][ky] = 1
chess[sx][sy] = 1
# pprint(chess)

N = int(N)
for _ in range(N):
    dir = dir_dict[input()] # 방향 입력
    # print(dir[0], dir[1])

    # 왕이 움직일 곳이 범위 밖인가? 그렇다면 continue
    if kx + dir[0] == 8 or kx + dir[0] == -1 or ky + dir[1] == 8 or ky + dir[1] == -1:
        continue
    else: # 아니라면
        # 해당 곳에 돌이 있는가?
        if kx + dir[0] == sx and ky + dir[1] == sy: # 있다면,
            # 돌이 움직여야 할 곳이 범위 밖인 가?
            if sx + dir[0] == 8 or sx + dir[0] == -1 or sy + dir[1] == 8 or sy + dir[1] == -1:
                continue
            else:
                chess[sx + dir[0]][sy + dir[1]] = 1
                chess[kx][ky] = 0
                kx = kx + dir[0]
                ky = ky + dir[1]
                sx = sx + dir[0]
                sy = sy + dir[1]
        else: # 돌이 없다면
            chess[kx + dir[0]][ky + dir[1]] = 1
            chess[kx][ky] = 0

            kx = kx + dir[0]
            ky = ky + dir[1]
    # pprint(chess)
 
real_kx, real_ky = str(8 - kx), chr(65 + ky)
real_sx, real_sy = str(8 - sx), chr(65 + sy)

print(real_ky + real_kx)
print(real_sy + real_sx)