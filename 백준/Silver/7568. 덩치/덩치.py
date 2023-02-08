N = int(input()) # 사람 수
people_dict = {} # 명단 별 저장.
for n in range(1, N + 1):
    x, y = list(map(int, input().split())) # 몸무게와 키
    people_dict[n] = (x, y)
# print(people_dict)


# 데이터를 어떻게 비교할 것인가?
## if문 
## x도 크고 y도 크면 카운팅한다.
# 이중 for문으로 비교
fin_dict = {}
for num, people in people_dict.items():
    cnt = 1
    for _, compare_p in people_dict.items():
        if people[0] < compare_p[0]:
            if people[1] < compare_p[1]:
                cnt += 1
    fin_dict[num] = cnt 
print(*fin_dict.values())