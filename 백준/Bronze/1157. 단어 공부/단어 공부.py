def count_number(cnt_lst, word_lst):
    if cnt_lst.count(max(cnt_lst)) > 1:
        return "?"
    else:
        return word_lst[cnt_lst.index(max(cnt_lst))]
        
sentence = input().upper()
word_lst = list(set(sentence)) 
cnt_lst = []

# 각 단어별로 개수가 몇 개인지 저장하기

for word in word_lst:
    cnt_lst.append(sentence.count(word))

print(count_number(cnt_lst, word_lst))