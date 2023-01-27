duck = input()
question_lst = []
while True:

    answer = input()
    if answer == '문제':
        question_lst.append('문제')
    elif answer == '고무오리':
        if '문제' in question_lst:
            question_lst.pop()
        else:
            question_lst.append('문제')
            question_lst.append('문제')
    elif answer == '고무오리 디버깅 끝':
        break
        
    # 문제가 리스트 안에 있는지?
    # 없다면 문제를 리스트에 두 개 추가하라.
    # 있다면 문제를 제거하라.

# question_lst 안에 아무것도 없으면 '고무오리야 사랑해' 출력
# print(question_lst)
if len(question_lst) == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')