import sys
import heapq
input = sys.stdin.readline

n = int(input())
classtime = [] # 튜플로 저장
classroom = [] # 강의실 배열
for _ in range(n):
    s, t = map(int, input().split())
    classtime.append((s, t))

# 시작 시간이 빠른 순으로 정렬한다.
# 만약 시작 시간이 같으면, 종료가 빠른 순으로 정렬
classtime.sort(key=lambda x: (x[0], x[1]))
# print(classtime)
for i in classtime:
    (s, t) = i
    # 강의실이 비어 있지 않고, 현 강의의 시작 시간이 강의실의 최소값보다 작거나 같으면,
    # 강의실의 최소값을 빼고나서, 현 강의의 종료 시간을 푸쉬한다.
    # 힙이 비어있으면 인덱스 에러가 나므로, 강의실이 비어있으면 안됨
    if classroom and classroom[0] <= s:
        heapq.heappop(classroom) # classroom의 최소값 빼기
    heapq.heappush(classroom, t) # 강의실의 현재 강의의 종료 시간 넣기

# print(classroom)
print(len(classroom))