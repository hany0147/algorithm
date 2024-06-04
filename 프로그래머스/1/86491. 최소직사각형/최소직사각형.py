def solution(sizes):
    weight = []
    height = []

    for size in sizes:
        weight.append(max(size))
        height.append(min(size))
        
    return max(weight) * max(height);

 