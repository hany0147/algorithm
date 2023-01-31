N =  int(input())
room = [input() for _ in range(N)]
# print(room) # ['....X', '..XX.', '.....', '.XX..', 'X....'] 
# print(room[0][0]) # .

# 2. 행 / 열 순회

line_result = 0
column_result = 0
for x in range(N):
    line_cnt = 0
    column_cnt = 0
    for y in range(N):


        if room[x][y] == '.':
            line_cnt += 1
            if line_cnt == 2:
                line_result += 1
        else:
            line_cnt = 0

        if room[y][x] == '.':
            column_cnt += 1
            if column_cnt == 2:
                column_result += 1
        else:
            column_cnt = 0

print(line_result, column_result)