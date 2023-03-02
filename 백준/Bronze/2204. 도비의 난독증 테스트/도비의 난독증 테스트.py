import sys
input = sys.stdin.readline

while True:
    word_lst = []
    original_lst = []
    n = int(input())
    if n == 0:
        break
    for _ in range(n):
        word = input().rstrip()
        original_lst.append(word)
        new_word = word.upper()
        word_lst.append(new_word)

    # print(original_lst)
    # print(word_lst)

    word_lst.sort()
    # print(word_lst)

    for word in original_lst:
        new_word = word.upper()
        # print(new_word, word)
        if new_word == word_lst[0]:
            print(word)