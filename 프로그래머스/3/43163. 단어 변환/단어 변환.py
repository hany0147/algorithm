# set를 이용해서 차집합이 1이 나오는 경우를 찾는다.
# 이 방법은 안된다 -> 왜냐하면 위치마저 일치해야하기 때문...
from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = 0
    words = [begin] + words
    n = len(words)

    lst = [[] * n for _ in range(n)]
    for idx_a, word_a in enumerate(words):
        for idx_b, word_b in enumerate(words):
            if word_a == word_b:
                continue
            
            if sum(a != b for a, b in zip(word_a, word_b)) == 1:
                lst[idx_a].append(idx_b)
    
    
    visited = [False] * n
    
    q = deque([(0, 0)])
    visited[0] = True
    
    while q:
        cur, cnt = q.popleft()
        if words[cur] == target:
            return cnt
        for nxt in lst[cur]:
            if not visited[nxt]:
                q.append((nxt, cnt + 1))
                visited[nxt] = True
                
    
    return 0