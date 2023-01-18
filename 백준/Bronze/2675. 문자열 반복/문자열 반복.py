T = int(input()) # 케이스 수

for t in range(T):
    R, S = input().split()

    # print(R, S)
    print(*[S[n]*int(R) for n in range(len(S))], sep = "")