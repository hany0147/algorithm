a_deck = list(map(int, input().split()))
b_deck = list(map(int, input().split()))
a_score = 0
b_score = 0
checklist = []

# 각 라운드 마다 승리, 패배, 무승무 점수를 매긴다.
# 각 라운드 마다 승패를 체크한다.

for n in range(10):
    # A가 이길 경우
    if a_deck[n] > b_deck[n]:
        a_score += 3
        checklist.append('a')
    # B가 이길 경우
    elif a_deck[n] < b_deck[n]:
        b_score += 3
        checklist.append('b')
    # 무승부일 경우
    else:
        a_score += 1
        b_score += 1
        checklist.append('d')

print(a_score, b_score) # 두 사람의 총합 출력
 
# 총합을 비교한다.
if a_score > b_score:
    print('A')
elif a_score < b_score:
    print('B')
# 무승부라면
else:
    while True: # d가 체크리스트에서 없어 질때까지 돌린다.
        check = checklist.pop()
        if check == 'a':
            print('A')
            break
        elif check == 'b':
            print('B')
            break
    
        if not checklist:
            print('D')
            break