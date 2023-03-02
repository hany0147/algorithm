import sys
input = sys.stdin.readline

N = int(input()) # 과목 개수
scores = list(map(int, input().split())) # 점수들


def new_avg(scores):
    sum_score = 0
    max_score = max(scores)
    for score in scores:
        new_score = score / max_score * 100
        sum_score += new_score
    
    avg_score = sum_score / N
    
    return avg_score

print(new_avg(scores))