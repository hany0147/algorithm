from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    cards = list(input().split())
    # print(ord('A'))

    standard = cards.pop(0)
    ans = deque()
    ans.append(standard)
    # print(cards)
    for card in cards:
        # 뽑은 카드의 아스키 코드가 크다면
        if ord(standard) < ord(card):
            ans.append(card)
        elif ord(standard) >= ord(card):
            ans.appendleft(card)
            standard = card
    ans = list(ans)
    for a in ans:
        print(a, end="")
    print()