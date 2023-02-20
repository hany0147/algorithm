N = int(input())
min_ = 99999999
for M in range(1, 1000001):
    m_str = str(M)
    sum_ = 0
    for m in m_str:
        sum_ += int(m)
    fin_ = sum_ + M
    if fin_ == N:
        if M < min_:
            min_ = M

if min_ == 99999999:
    print(0)
else:
    print(min_)