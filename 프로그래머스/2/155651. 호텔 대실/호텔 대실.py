from heapq import heappop, heappush

# def trimming(time):
#     hour = int(time.split(":")[0])
#     minute = int(time.split(":")[1]) + 10

#     if minute >= 60:
#         hour += minute // 60
#         minute %= 60

#     return str(hour) + ":" + str(minute)

# def solution(book_time):
#     book_time = sorted([i[0], trimming(i[1])] for i in book_time)
#     rooms = []
#     for time in book_time:
#         if len(rooms) != 0 and rooms[0] <= time[0]:
#             heapq.heappop(rooms)
#         heapq.heappush(rooms, time[1])
        
#     return len(rooms)


def solution(book_time):
    rooms = []
    book_time.sort(key = lambda _:_[0])
    for book in book_time :
        check_in = num(book[0])
        check_out = num(book[1]) + 10
        if len(rooms) != 0 and rooms[0] <= check_in :
            heappop(rooms)
        heappush(rooms,check_out)
    return len(rooms)

def num(HHMM) :
    return 60*int(HHMM[:2]) + int(HHMM[3:])