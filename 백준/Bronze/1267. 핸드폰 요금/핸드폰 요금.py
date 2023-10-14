n = int(input())
arr = list(map(int, input().split()))

def Y_cost(cost):
    standard = 10
    pay_per = (cost // 30) + 1
    res = standard * pay_per
    return res
def M_cost(cost):
    standard = 15
    pay_per = (cost // 60) + 1
    res = standard * pay_per
    return res

Y = sum(list(map(lambda x: Y_cost(x), arr)))
M = sum(list(map(lambda x: M_cost(x), arr)))

if Y > M:
    print('M', M)
elif Y < M:
    print('Y', Y)
else:
    print('Y', 'M', M)