T = int(input())

for _ in range(T):
    quiz = input()
    sum_score = 0
    cnt = 0
    # o가 나오면 카운팅을 시작하고, 

    # o가 또 나온다면 누적 카운팅을하며,

    # x가 나온다면 기존의 cnt를 리셋한다.

    for answer in quiz:
        if answer == 'O':
            cnt += 1
            sum_score += cnt
        elif answer == 'X':
            cnt = 0

    print(sum_score)