import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from copy import deepcopy

# 0. 입력 및 초기값 설정
normal = []
jaejoon = []

n = int(input())
for _ in range(n):
    colors = input().rstrip()
    colors1 = list(colors)
    normal.append(colors1)
    colors = colors.replace('R', 'G')
    colors2 = list(colors)
    jaejoon.append(colors2)
# print(jaejoon)   
# print(normal)

def dfs(x, y, who, color):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if who[x][y] == color:
        who[x][y] = 0
        dfs(x, y + 1, who, color)
        dfs(x, y - 1, who, color)
        dfs(x + 1, y, who, color)
        dfs(x - 1, y, who, color)
        return True
    return False

result1 = 0
result2 = 0
result3 = 0
for x in range(n):
    for y in range(n):
        if dfs(x, y, normal, 'R') == True:
            result1 += 1
        elif dfs(x, y, normal, 'B') == True:
            result2 += 1
        elif dfs(x, y, normal, 'G') == True:
            result3 += 1
print(result1 + result2 + result3, end = " ")

result4 = 0
result5 = 0
result6 = 0
for x in range(n):
    for y in range(n):
        if dfs(x, y, jaejoon, 'R') == True:
            result4 += 1
        elif dfs(x, y, jaejoon, 'B') == True:
            result5 += 1
        elif dfs(x, y, jaejoon, 'G') == True:
            result6 += 1
print(result4 + result5 + result6)