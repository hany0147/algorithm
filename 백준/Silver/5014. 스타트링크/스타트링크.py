# 0. 초기값 설정
f, s, g, u, d = map(int, input().split())
s = s - 1
g = g - 1
check = [False] * f
floors = [-1 for _ in range(f)]
moving = [u, -d]
floors[s] = 0



# 1. bfs 함수 만들기
# 주의점: 최소값 cnt하기

from collections import deque

def bfs(i):
    q = deque()
    q.append(i)
    check[i] = True

    while q:
       cur = q.popleft()
       for n in range(2):
          new_cur = cur + moving[n]
          ## 범위 확인
          if 0<= new_cur < f and not check[new_cur]:
             q.append(new_cur)
             floors[new_cur] = floors[cur] + 1 # 1씩 더해나가서 최소값구하기
             check[new_cur] = True 

bfs(s)

# 절대 도달 불가한 경우 (print('use the stairs'))
if floors[g] == -1:
   print('use the stairs')
else:
   print(floors[g])  