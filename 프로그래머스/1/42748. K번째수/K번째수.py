def solution(array, commands):
    answer = []
    for command in commands:
        tmp = []
        i, j, k = command[0], command[1], command[2]
        tmp = sorted(array[i-1:j])
        answer.append(tmp[k-1])
    return answer