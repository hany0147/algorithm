ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]

song = list(map(int, input().split()))

if song == ascending:
    print('ascending')
elif song == descending:
    print('descending')
else:
    print('mixed')