set_num = set() # 서로 다름 값이 몇 개 있는 지 출력하기 위해선 중복값을 제거하는 자료구조 필요

for _ in range(10):
    num = int(input())
    fin = num % 42
    set_num.add(fin)

print(len(set_num))