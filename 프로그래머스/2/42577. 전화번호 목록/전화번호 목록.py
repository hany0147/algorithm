def solution(phone_book):
    # 배열의 길이가 100만이기 때문에, 이중 for문을 불가능
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    return True
    
    
    # 효율성 통과 못하는 코드
    # phone_book.sort()
    # for phone in phone_book:
    #     n = len(phone)
    #     for phone2 in phone_book:
    #         if phone == phone2:
    #             continue
    #         if phone == phone2[:n]:
    #             return False
    # return True