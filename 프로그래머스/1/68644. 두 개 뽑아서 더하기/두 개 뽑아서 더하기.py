def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            answer.add(numbers[i] + numbers[j])
    return sorted(list(answer))