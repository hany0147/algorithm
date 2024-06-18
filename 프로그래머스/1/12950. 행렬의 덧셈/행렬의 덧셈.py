def solution(arr1, arr2):
    answer = [[0] * len(arr1[0]) for _ in range(len(arr1))]

    for x in range(len(arr1)):
        for y in range(len(arr1[0])):
            answer[x][y] = arr1[x][y] + arr2[x][y]
    return answer