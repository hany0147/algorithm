N, M = list(map(int, input().split()))

# 1. 카드덱을 만든다.

card = list(map(int, input().split()))
# print(card)

# 2. 모든 경우의 수로 3개를 뽑아내서 21과 가장 가까운 숫자를 뽑아 낸다(합 <= 21, min(len(21 - 합)) )

# 2-1 모든 경우의 수 만들기.

max_card = 0 # 큰 값 초기설정

for x in range(N - 2):
    for y in range(x + 1 , N - 1):
        for z in range(y + 1, N):
            sum_card = card[x] + card[y] + card[z]
            
            # 2-2 card 총합이 M보다 작거나 같아야 하며, 그 합이 가장 커야함. (MAX 구현)

            if max_card < sum_card <= M:
                max_card = sum_card

            if max_card == M:
                break


print(max_card)