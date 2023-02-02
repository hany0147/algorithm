W_score_lst = []
K_score_lst = []

for _ in range(1, 11):
    score = int(input())
    W_score_lst.append(score)

for _ in range(11, 21):
    score = int(input())
    K_score_lst.append(score)

W_score_lst.sort(reverse = True)
K_score_lst.sort(reverse = True)

print(sum(W_score_lst[:3]), sum(K_score_lst[:3]))