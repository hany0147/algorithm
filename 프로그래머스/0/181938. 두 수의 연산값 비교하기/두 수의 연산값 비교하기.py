def solution(a, b):
    something = int(str(a) + str(b))
    the_other = 2 * a * b
    
    return max(something, the_other)