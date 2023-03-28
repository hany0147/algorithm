N, M = map(int, input().split())
answer = []

def back():
    if len(answer) == M: # 탈출조건
        print(" ".join(map(str, answer))) # 탈출할 때, 답을 도출하기 위함
        return # 함수에서 탈출
    for i in range(1, N + 1): # 1~N까지
        if i not in answer: # 중복확인
            answer.append(i) # 없으니 추가
            back() # 재귀
            answer.pop() #return으로 돌아오면 이게 실행됨. 1, 2, 3일 때 3을 없앰으로 전 단계로 돌아가는 것.
back()