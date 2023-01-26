# 손님 입력
N = int(input())
clients = list(map(int, input().split()))

# 좌석여부
seat_list = []

# 거절 당한 수
cnt = 0

# 손님이 들어와서 말하는 좌석(입력값)이 리스트 안에 있다면, 카운트
for client in clients:
    if client in seat_list:
        cnt += 1
    else:
        seat_list.append(client)

print(cnt)