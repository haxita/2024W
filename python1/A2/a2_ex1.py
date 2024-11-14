# Exercise 1 – Submission: a2_ex1.py 25 Points
# Write a program that calculates and outputs the bonus payment of an employee in your company
# PyComp. To do this, read the duration of the employment and the department the employee works
# in. The employment years must be greater than 0 and the departments are numbered from 10 to
# 99.
# • For a negative number or 0 (employment), or an invalid department number < 10 or > 99,
# print an error message ("Invalid input") and terminate the program by calling exit(0) You
# can assume that the user will only enter digits.
# • For an employment less than 2 years, the bonus is 200 €.
# • For an employment between (and including) 2 and 3 years the bonus is 300 €.
# • For an employment of more than three years there is a base bonus of 400 €. Furthermore,
# there is an additional bonus depending on the department.
# – If the last digit of the department is between (and including) 1 and 5, the base bonus is
# increased by 10%.
# – If the last digit of the department is between (and including) 6 and 9, the base bonus is
# increased by 20%.
#
# In case of valid inputs (i.e., no errors as described above), print both the bonus (float with 2 decimal
# places; see the example input and output below for how it must look like). Do not perform unnec-
# essary checks, i.e., do not check for values that have already been excluded by previous conditions.
# Example input and output:1
# Enter employment years (> 0): 2
# Enter department (10-99): 8
# Invalid input
# Example input and output:
# Enter employment years (> 0): 0
# Enter department (10-99): 10
# Invalid input
# Example input and output:
# Enter employment years (> 0): 7
# Enter department (10-99): 53
# Bonus for 7 years of employment in department 53: 440.00
# Example input and output:
# Enter employment years (> 0): 3
# Enter department (10-99): 77
# Bonus for 3 years of employment in department 77: 300.00

years = int(input("Enter employment years (> 0): "))
department = int(input("Enter department (10-99): "))

if years <= 0 or department > 99 or department < 10:
    print(f"Invalid input")
elif years < 2:
    bonus = 200
    print(f"Bonus for {years} years of employment in department {department}: {bonus:.2f}")
elif 2 <= years <= 3:
    bonus = 300
    print(f"Bonus for {years} years of employment in department {department}: {bonus:.2f}")
elif 3 < years:
    if 1 <= department % 10 <= 5:
        bonus = 400 * 1.1
        print(f"Bonus for {years} years of employment in department {department}: {bonus:.2f}")
    elif 6 <= department % 10 <= 9:
        bonus = 400 * 1.2
        print(f"Bonus for {years} years of employment in department {department}: {bonus:.2f}")
    else:
        bonus = 400
        print(f"Bonus for {years} years of employment in department {department}: {bonus:.2f}")

