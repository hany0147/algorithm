def sum_num(n):
    return sum(int(int_n) for int_n in str(n))

def find_self_number(standard):
    non_self_numbers = set()
    for i in range(1, standard):
        tmp = i + sum_num(i)
        non_self_numbers.add(tmp)
    
    for i in range(1, standard):
        if i not in non_self_numbers:
            print(i)

find_self_number(10_001)