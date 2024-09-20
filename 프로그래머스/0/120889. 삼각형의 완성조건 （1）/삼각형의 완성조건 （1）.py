def solution(sides):
    sides.sort(reverse=True)
    longest = sides[0]
    other = sides[1:3]
    if longest < sum(other):
        return 1
    else:
        return 2
