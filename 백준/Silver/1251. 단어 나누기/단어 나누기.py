words = input()
N = len(words) # arrested , N = 8
# 두 번 나눠야 한다. -> 두 번 포문을 돌린다.
# 그리고 해당 i, j가 자르는 부분이 되고, [:]로 그 범위를 설정한다.

# 두 개로 자르기.

sum_ = []
for i in range(1, N - 1):
    for j in range(i+1, N):
        word1 = words[:i]
        word2 = words[i:j]
        word3 = words[j:]
        
        r_word2 = word2[::-1]
        r_word1 = word1[::-1]
        r_word3 = word3[::-1]

        sum_.append(r_word1 + r_word2 + r_word3)

        sum_.sort()

print(sum_[0])