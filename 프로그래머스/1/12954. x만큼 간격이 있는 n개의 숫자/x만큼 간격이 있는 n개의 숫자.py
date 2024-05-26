def solution(x, n):
    ans = [x]
    a = x
    for i in range(1, n):
        a += x
        ans.append(a)
    return ans