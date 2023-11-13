
def solution(n,a,b):
    cnt = 1
    a, b = min(a, b), max(a, b)
    while True:
        # 종료조건: a는 홀수, b는 짝수 그리고 a와 b는 1씩 차이나야함
        if a % 2 == 1 and b % 2 == 0 and a + 1 == b:
            break
        cnt += 1
        a = a // 2 + a % 2
        b = b // 2 + b % 2
        
    return cnt