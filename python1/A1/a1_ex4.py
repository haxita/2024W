# Write a program that can print a small order form for a furniture store (see the example input and
# output below for how it must look like). You have to read in three integer numbers, which will then
# be part of such an order:
# • The number of ordered chairs. Each chair costs 49.99euros.
# • The number of ordered tables. Each table costs 199.99euros.
# • The number of ordered lamps. Each lamp costs 29.99euros.
# Calculate the total cost for these three positions, and finally, compute the total cost of the entire
# order. The number of ordered items must have a minimum print width of 3 (4 for the line with the
# lamps, because it is a letter shorter), for the single price 6 and 9 for the item sum. The total sum
# should have a print width of 26, so that even for large sums (see example below) the formatting still
# works. You have to format only the output, not the user input. All float results must be printed
# with 2 decimal places.
# Example input and output:
# Input the number of ordered chairs: 123
# Input the number of ordered tables: 654
# Input the number of ordered lamps: 123
# Order Form:
# ---------------------------------
# Chairs: 123 x 49.99 = 6148.77
# Tables: 654 x 199.99 = 130793.46
# Lamps: 123 x 29.99 = 3688.77
# ---------------------------------
# Total: 140631.00
# =================================

Chairs_num = int (input ("Input the number of ordered chairs: "))
Tables_num = int (input ("Input the number of ordered tables: "))
Lamps_num = int (input ("Input the number of ordered lamps: "))

Cost_Chairs = 49.99
Cost_Tables = 199.99
Cost_Lamps = 29.99

Total_Chairs = Chairs_num * Cost_Chairs
Total_Tables = Tables_num * Cost_Tables
Total_Lamps = Lamps_num * Cost_Lamps

Total_Cost = Total_Chairs + Total_Tables + Total_Lamps

print ("\nOrder Form:")
print ("---------------------------------")
print (f"Chairs: {Chairs_num:3d} x {Cost_Chairs:6.2f} = {Total_Chairs:10.2f}")
print (f"Tables: {Tables_num:3d} x {Cost_Tables:6.2f} = {Total_Tables:10.2f}")
print (f"Lamps: {Lamps_num:4d} x {Cost_Lamps:6.2f} = {Total_Lamps:10.2f}")
print("---------------------------------")
print (f"Total: {Total_Cost:26.2f}")
print ("=================================")