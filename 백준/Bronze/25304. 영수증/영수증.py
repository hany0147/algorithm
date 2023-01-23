X = int(input())
N = int(input())
sum_prices = 0

for n in range(N):
    a, b = list(map(int, input().split()))
    each_price = a * b
    sum_prices += each_price
    

if sum_prices == X:
        print('Yes')
else:
        print('No')