# 최소의 비용
n = int(input()) # 도시의 개수
roads = list(map(int, input().split())) # 두 도시를 연결하는 각 도로의 길이
prices = list(map(int, input().split())) # 각 도시의 리터당 가격
roads.append(0)

pay = 0 # 기름값

min_price = 1000000001
# roads와 prices의 인덱스가 동일하고 각 인덱스는 도시를 대표한다.
# 해당 도시의 가격이 다음 도시의 가격보다 싸다면 그 다음 도시와 비교한다.

for idx in range(n):
    if idx == n - 1:
        break

    if min_price > prices[idx]:
        min_price = prices[idx]
    pay += (min_price * roads[idx])
print(pay)