def solution(new_id):
    
    # 1단계: 소문자로 치환
    new_id = new_id.lower()
    
    # 2단계: 조건 문자외 제거
    revision_id = ''
    for i in new_id:
        if i.islower() or i.isdigit() or i in "-_.":
            revision_id += i
    
    # 3단계: . 2번 연속 나오면 하나만 남기기.
    while '..' in revision_id:
        revision_id = revision_id.replace('..', '.')
    
    # 4단계: .가 처음이나 끝에 위치한다면 제거
    if revision_id and revision_id[0] == '.':
        revision_id = revision_id[1:]

    if revision_id and revision_id[-1] == '.':
        revision_id = revision_id[:len(revision_id) - 1]

    # 5단계: 빈 문자열이면 a를 대입
    if not revision_id:
        revision_id += 'a'

    # 6단계: 길이가 16자 이상이면, 뒤에 빼기
    if len(revision_id) >= 16:
        revision_id = revision_id[:15]

    if revision_id and revision_id[-1] == '.':
        revision_id = revision_id[:len(revision_id) - 1]    

    # 7단계: 길이가 2자 이하면, 마지막 문자를 길이가 3이 될때까지 반복
    if len(revision_id) <=2:
        last = revision_id[-1]
        while True:
            if len(revision_id) == 3:
                break
            revision_id += last
    
    return revision_id