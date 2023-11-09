from collections import defaultdict

def solution(n, words):
    answer = []
    people = defaultdict(int)
    done = []
    for idx, word in enumerate(words):
        # 기존에 썼던 단어가 아니어야 하고
        if word not in done:
            
            # 첫번째 시작이 아니면서, 기존 단어의 뒷글자와 일치해야 함.
            if idx !=0:
                if word[0] == done[-1][-1]:
                    done.append(word)
                    people[idx % n] += 1
                else:
                    people[idx % n] += 1
                    return [idx % n + 1, people[idx % n]]
            else:
                done.append(word)
                people[idx % n] += 1
        else:
            people[idx % n] += 1
            return [idx % n + 1, people[idx % n]]
            

    return [0, 0]