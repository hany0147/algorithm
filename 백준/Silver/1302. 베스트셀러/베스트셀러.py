N = int(input()) # 오늘 팔린 책의 개수
book_dict = {}

for _ in range(N):
    book = input()
    if book in book_dict:
        book_dict[book] += 1
    else:
        book_dict[book] = 1
# print(book_dict)


sort_book = sorted(book_dict.items(), key = lambda x: (-x[1], x[0]))
print(sort_book[0][0])