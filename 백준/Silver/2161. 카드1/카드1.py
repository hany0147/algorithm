N = int(input())
discard_lst = []
card_lst = [i for i in range(1, N + 1)] # 리스트 컴프리헨션
# card_lst = list(range(1, N + 1))

# 리스트에 카드 하나 남기 전까지
while len(card_lst) > 1:
    discard_lst.append(card_lst.pop(0))
# 첫번째 카드를 버린다(pop(0)). 버리는 리스트 만들고 (append)
    card_lst.append(card_lst.pop(0))
# 그 다음 카드를 뒤로 넘긴다. (pop(0)하고 append 한다)
# 반복

print(*discard_lst, *card_lst)