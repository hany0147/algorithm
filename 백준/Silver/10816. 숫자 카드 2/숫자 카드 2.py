import sys
N = int(input()) # 가지고 있는 숫자 카드의 개수
cards = list(map(int, sys.stdin.readline().split())) # 숫자 카드에 적혀 있는 정수
M = int(input()) # 확인해야 할 카드 개수
checks = list(map(int, sys.stdin.readline().split())) # 확인할 숫자


# 시간 초과
# for check in checks:
#     print(cards.count(check), end = " ")


# 딕셔너리 활용
# 1. 각 숫자 세기
deck = {}
for card in cards:
    if card in deck:
        deck[card] += 1
    else:
        deck[card] = 1
    # 없는 경우는?

# print(deck)

# 2. 출력하기

for check in checks:
    if check not in deck.keys():
        deck[check] = 0
    print(deck[check], end = " ")