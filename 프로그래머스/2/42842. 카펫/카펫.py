def solution(brown, yellow):
    answer = 0
    for i in range(1, yellow // 2 + 2):
        if yellow % i == 0:
            if i != 1:
                j = yellow // i
            else:
                j = yellow
            if brown == 2 * i + 2 * j + 4:
                return [j + 2, i + 2]