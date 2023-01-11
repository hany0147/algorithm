N = int(input())
result = 0
# N // 10 # 몫
# N % 10 # 나머지

while N > 0:
    result = result + N % 10 # N을 10으로 나눈 나머지를 계속 합치는 것 
    N = N // 10 # N을 10으로 나눈 몫을 다시 N으로 할당
    
    # 둘이 순서 주의.

print(result)

# 반복해야한다. 하지만 int이므로 for문은 불가. while문 가능.
# 종료 조건 설정해야 함. N값이 0보다 클 때까지만 돌린다.
