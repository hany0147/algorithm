T = int(input())

for t in range(T):

    # 거스름 돈의 액수는 센트로 입력됨
    C = int(input())
    # print(C) # 1달러 = 100센트 124센트면 1.24달러

    remain_c= 0
    remain_dic = {} # dict 이용
    
    # 손님이 받는 동전의 개수를 최소로 하려면, 가장 많은 돈부터 나눠야 한다.
    remain_dic['Quarter'] = C // 25
    remain_c = C % 25

    remain_dic['Dime'] = remain_c // 10
    remain_c = remain_c % 10

    remain_dic['Nickel'] = remain_c // 5
    remain_c = remain_c % 5

    remain_dic['Penny'] = remain_c // 1
   
    lst = []
    for key, value in remain_dic.items():
       lst.append(value)

    print(*lst)    