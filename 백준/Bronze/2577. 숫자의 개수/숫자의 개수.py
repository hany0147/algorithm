# 입력
A = int(input())
B = int(input())
C = int(input())

# 다 곱하기

multi_str_num = str(A * B * C)

# 출력
for i in range(10):
    print(multi_str_num.count(str(i)))