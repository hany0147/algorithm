# 입력
A = int(input())
B = int(input())
C = int(input())


if (A + B + C) == 180: # 180 이라면
    # 각이 모두 같으면
    if A == B == C:
        print('Equilateral')
    # 두 각이 같은 경우
    elif (A == B) or (A == C) or (B == C):
        print('Isosceles')
    else:
        print('Scalene')

else: # 180이 아니면 삼각형이 아니다.
    print('Error') 