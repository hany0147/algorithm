import sys
import heapq

N = int(sys.stdin.readline())
num_lst = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(num_lst, (abs(x), x))
        
    else:
        if num_lst:
            print(heapq.heappop(num_lst)[1])
        else:
            print(0) 