H, M = list(map(int, input().split()))

if M - 45 < 0:
    new_M = M + 15
    if H == 0:
        new_H = 23
    else:
        new_H = H - 1
else:
    new_M = M - 45
    new_H = H

print(new_H, new_M)