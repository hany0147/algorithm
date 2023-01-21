num1 = input()
num2 = input()

A  = int(num1[0])
B = int(num1[1])
C = int(num1[2])
D = int(num2[0])
E = int(num2[1])
F = int(num2[2])

a = A * 100
b = B * 10
c = C * 1
d = D * 100
e = E * 10
f = F * 1
sum_1 = a + b + C
multi_1 = sum_1 * F
multi_2 = sum_1 * E
multi_3 = sum_1 * D
fin_ = multi_1 + (multi_2 * 10) + (multi_3 * 100)

print(multi_1, multi_2, multi_3, fin_, sep = '\n')