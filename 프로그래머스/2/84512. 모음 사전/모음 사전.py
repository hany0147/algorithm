def solution(word):
    global dic, dic_lst
    dic = ['A', 'E', 'I', 'O', 'U']
    dic_lst = []

    dfs(0, "")
    dic_lst.sort()
    
    return dic_lst.index(word);


def dfs(cnt, string):
    if cnt <= 5:
        dic_lst.append(string)
    else:
        return

    for i in range(5):
        dfs(cnt + 1, string + dic[i])