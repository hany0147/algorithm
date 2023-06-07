n = int(input())
string = list(input())
dict = {}
result = [0, 0]
start = 0
end = 0

while start < len(string) and end < len(string):

    if string[end] not in dict:
        dict[string[end]] = 1
    else:
        dict[string[end]] += 1

    if len(dict) > n:
        while start <= end and len(dict) > n:
            if dict[string[start]] == 1:
                dict.pop(string[start])
            else:
                dict[string[start]] -= 1
            start += 1

    if len(dict) <= n:
        # 최대길이로 갱신해주자~
        if result[1] - result[0] < end - start:
            result[0] = start
            result[1] = end
    end += 1
 
print(result[1] - result[0] + 1)