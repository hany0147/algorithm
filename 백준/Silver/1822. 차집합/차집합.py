A, B = list(map(int, input().split()))

A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))

fin = sorted(list(A_set - B_set))

print(len(fin))
print(*fin)