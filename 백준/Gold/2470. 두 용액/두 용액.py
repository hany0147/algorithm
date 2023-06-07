import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

start = 0
end = n - 1
ans = abs(liquid[start] + liquid[end])
res = [liquid[start], liquid[end]]

while start < end:
    temp_start = liquid[start]
    temp_end = liquid[end]
    temp_sum = temp_start + temp_end

    if abs(temp_sum) < ans:
        ans = abs(temp_sum)
        res = [temp_start, temp_end]
        if ans == 0:
            break
    
    if temp_sum < 0:
        start += 1
    else:
        end -= 1
print(res[0], res[1])