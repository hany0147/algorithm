N, M = map(int, input().split()) # 바구니 N개, 공 M번 넣기

# 바구니 만들기
ball_lst = [0] * (N + 1)
# print(ball_lst)
for _ in range(M):
    i, j, k = map(int, input().split()) # i번부터 j번 바구니까지 k번 번호가 적힌 공 넣기
    for n in range(i, j + 1):
        ball_lst[n] = k

ball_lst.pop(0)
print(*ball_lst)