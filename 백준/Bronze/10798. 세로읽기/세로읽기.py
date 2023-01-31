from pprint import pprint

# 행렬 생성
matrix = []

for _ in range(5):
    lst = []
    words = input()

    for word in words:
        lst.append(word)
    # 매트릭스 열의 길이 중 가장 긴 것보다 짧은 매트릭스 열이 있다면 해당 열의 빈 자리에 '-'을 삽입하라.

    matrix.append(lst)
# pprint(matrix)


# 열의 길이 중 가장 길이가 긴 것을 구하는 법.
max_column = 0
for column in range(5):
    if max_column < len(matrix[column]):
        max_column = len(matrix[column])
# print(max_column)

# 긴 것보다 짧은 매트릭스 열이 있다면 해당 열의 빈 자리에 '-'을 삽입하라.
for column in range(5):
    if max_column > len(matrix[column]):
        for i in range(max_column - len(matrix[column])):
            matrix[column].append(' ')
# pprint(matrix)


# print(len(matrix)) # 행(5)
# print(len(matrix[i])) # 열(전부 다름)
 
# 열 순회
for y in range(len(matrix[0])):
    for x in range(len(matrix)):
        print(matrix[x][y].strip(), end = "")