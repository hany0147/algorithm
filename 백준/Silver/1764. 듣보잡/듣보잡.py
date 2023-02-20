N, M = list(map(int, input().split())) # n 듣도 못한 사람의 수, m 보도 못한 사람의 수
no_listen = set()
no_see = set()
for n in range(N):
    no_listen.add(input())

for m in range(M):
    no_see.add(input())
no_listen_see = sorted(list(no_see & no_listen))

print(len(no_listen_see))

for _ in no_listen_see:
    print(_)