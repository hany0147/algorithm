def solution(board, moves):
    bucket = []
    cnt = 0
    moves = list(map(lambda x: x - 1, moves))
    
    # 연산하기 쉽게 보드판 새로 짜기
    new_board = []
    for i in range(len(board)):
        tmp = []
        for j in range(len(board)):
            tmp.append(board[j][i]) 
        new_board.append(tmp)    
    
    # 인형뽑기 실행
    for move in moves:
        for i in range(len(new_board[move])):
            if new_board[move][i] != 0:
                if len(bucket) > 0 and bucket[-1] == new_board[move][i]:
                    bucket.pop()
                    cnt += 2
                else:
                    bucket.append(new_board[move][i])
                new_board[move][i] = 0
                break

    return cnt