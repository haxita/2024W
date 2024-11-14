# Read four numbers a, b, c and d from the console and convert them to integers. Afterwards, perform
# the following calculations and print the results (no string formatting required; see the example input
# and output below for how it must look like):
# • The sum of a, b and d
# • The product of all four numbers
# • The sum of a and c times the sum of b and d
# • The result of an integer division when dividing a by c
# • The result of a regular division when dividing a by b
# • The remainder of a division (modulo) when dividing a by d
# • a-c
# • √d= d
# 2
# • c
# 3· ab+ c
# 2−1 + d
# Example input and output:1
# a: 20
# b: 19
# c: 18
# d: 17
# Sum of a, b and d: 56
# Product of all numbers: 116280
# The sum of a and c times the sum of b and d: 1368
# a divided by c (int): 1
# a divided by d (float): 1.0526315789473684
# Remainder of a divided by d: 3
# a to the power of -c: 3.814697265625e-24
# d to the power of 1/2 (square root): 4.123105625617661
# Complex equation: 1.610612736e+37

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

Sum = a + b + d
print("Sum of a, b and d:", Sum)

Product = a * b * c * d
print("Product of all numbers:", Product)

SumACBD = (a + c) * (b + d)
print("The sum of a and c times the sum of b and d:", SumACBD)

DividAC = int (a / c)
print("a divided by c (int):", DividAC)

DividAD = float (a / b)
print("a divided by b (float):", DividAD)

Remainder = a % d
print("Remainder of a divided by d:", Remainder)

PowerA = a ** -c
print("a to the power of -c:", PowerA)

PowerD = d ** 0.5
print("d to the power of 1/2 (square root):", PowerD)

ComplexE = c/3 * ( a ** ( b + c/2 ) -1) + d
print("Complex equation:", ComplexE)


