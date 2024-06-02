def solution(seq, k):
    start, end = 0, 0
    answer = [0, len(seq)]
    num = seq[0]
    
    while True:
        if num < k:
            end += 1
            if end == len(seq):
                break
            num += seq[end]
        else:
            if num == k:
                if end - start < answer[1] - answer[0]:
                    answer = [start, end]
            num -= seq[start]
            start += 1

    return answer