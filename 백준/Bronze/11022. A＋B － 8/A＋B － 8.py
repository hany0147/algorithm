T = int(input())

for t in range(1, T + 1):
    A, B = list(map(int, input().split()))
    C = A + B
    print(f'Case #{t}: {A} + {B} = {C}')