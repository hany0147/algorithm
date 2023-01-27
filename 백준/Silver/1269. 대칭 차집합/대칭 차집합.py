# set 이용
# 입력

A_num, B_num = list(map(int, input().split())) # 집합 A의 원소의 개수와 집합 B의 원소의 개수

A = set(input().split()) # 집합 A의 모든 원소
B = set(input().split()) # 집합 B의 모든 원소
# print(A, B) {'4', '2', '1'} {'6', '2', '5', '4', '3'}

print(len(A ^ B))