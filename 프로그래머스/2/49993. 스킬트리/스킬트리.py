def solution(skill, skill_trees):

    # 결과
    res = 0
    
    for skill_tree in skill_trees:
        # 통과한 선행스킬을 담는 통
        past_skill = []
        # cnt = 0
        
        for chosen_skill in skill_tree:
            # 선행 스킬 안에 포함됐는가?
            #포함되지 않았다면, 스킵
            if chosen_skill not in skill:
                # cnt += 1
                continue

            # 포함됐다면,
            # fast_skill에 선행스킬이 존재하는가?
            # 만약, 첫 타자라면
            if skill.index(chosen_skill) == 0:
                past_skill.append(chosen_skill)
                # cnt += 1
            # 첫 타자가 아니고, 존재하지 않는다면, 아웃  
            elif skill[skill.index(chosen_skill) - 1] not in past_skill:
                break
            else:
                # 존재한다면, 통과
                # 그리고 past_skill에 저장
                past_skill.append(chosen_skill)
                # cnt += 1
        else:
            res += 1    
        # 전부 통과하면
        # if cnt == len(skill_tree):
        #     res += 1
    
    return res