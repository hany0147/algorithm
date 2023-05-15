import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    x = input().rstrip()
    arr.append(x)

for i in range(n - 1):
    for j in range(i + 1, n):
        # 짧은 게 먼저
        if len(arr[i]) > len(arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
        # 같다면
        elif len(arr[i]) == len(arr[j]):
            sum_x = 0
            sum_y = 0
            # print(list(zip(arr[i], arr[j])))
            for x, y in zip(arr[i], arr[j]):
                if x.isdigit():
                    sum_x += int(x)
                if y.isdigit():
                    sum_y += int(y)
            if sum_x > sum_y:
                arr[i], arr[j] = arr[j], arr[i]        
            elif sum_x == sum_y:
                for x, y in zip(arr[i], arr[j]):
                    if x > y:
                        arr[i], arr[j] = arr[j], arr[i]
                        break
                    elif x < y:
                        break
for a in arr:
    print(a)