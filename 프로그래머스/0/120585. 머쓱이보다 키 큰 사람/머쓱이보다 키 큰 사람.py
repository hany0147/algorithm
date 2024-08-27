def solution(array, height):
    answer = 0
    array.sort(reverse=True)
    for arr in array:
        if arr > height:
            answer += 1


    return answer