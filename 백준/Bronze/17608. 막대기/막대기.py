from collections import deque
import sys
stick_num = int(input()) # 막대기 개수
sticks = deque() # 막대기 리스트

for _ in range(stick_num): # 막대기 저장
    stick = int(sys.stdin.readline().rstrip()) # 막대기 입력
    sticks.append(stick) # 리스트화
# print(list(sticks))

# 막대기 순회(거꾸로)

compare_stick = sticks.pop() # 막대기 순회 기준
fin_sticks = deque() # 최종 막대기 리스트
fin_sticks.append(compare_stick) # 첫번째 기준 막대기까지 삽입한다.

for stick in list(sticks)[::-1]:

    # 기준 막대기보다 크면 최종 리스트에 삽입한다.
    if compare_stick < stick:
        fin_sticks.append(stick)
        compare_stick = stick

# print(fin_sticks)
print(len(fin_sticks))