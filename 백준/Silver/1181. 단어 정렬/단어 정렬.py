N = int(input())
lst = []
for _ in range(N):
    word = input()
    if word not in lst:
        lst.append(word)
    # heapq.heappush(heap_lst, word)

lst.sort(key= lambda x : (len(x), x))

print(*lst, sep = '\n') 