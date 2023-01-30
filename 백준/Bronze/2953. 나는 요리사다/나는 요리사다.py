score_dict = {}
max_score = 0

for i in range(1, 6):
    score = list(map(int, input().split()))
    score_dict[i] = sum(score)
    if max_score < sum(score):
        max_score = sum(score)

for key in score_dict:
    if score_dict[key] == max_score:
        print(key, max_score)