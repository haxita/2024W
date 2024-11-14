# -*- coding: utf-8 -*-
"""
Author -- Rainer Dangl
Contact -- dangl@ml.jku.at
Date -- 05.11.2024

################################################################################

The following copyright statement applies to all code within this file.

Copyright statement:
This material, no matter whether in printed or electronic form, may be used for
personal and non-commercial educational use only. Any reproduction of this
material, no matter whether as a whole or in parts, no matter whether in printed
or in electronic form, requires explicit prior acceptance of the authors.

################################################################################
"""

################################################################################
# Debugging
################################################################################

# Debugging is the process of identifying and fixing errors in the code.
# Python provides a built-in debugger called "pdb". However, this does not 
# offer the best experience. Rather, we recommend using an IDE with a built-in
# debugger. In Visual Studio Code, you can set breakpoints by clicking on the
# left side of the line number. Then, you can run the debugger by clicking on
# the "Run and Debug" button on the left side of the screen. This will start the
# debugger and stop at the first breakpoint. You can then step through the code
# line by line and inspect variables. You can also set conditional breakpoints
# and watch expressions.


def greet_user():
    name = input("Please enter your name: ")
    print("Name entered. Thank you!")
    print(f"Let's do some calculations, {name}!")

def calculate_sum(a: int, b: int) -> int:
    return a + b

def calculate_difference(a: int, b: int) -> int:
    return a - b

def calculate_product(a: int, b: int) -> int:
    return a * b

def create_values(a: int, b: int):
    values = []
    for i in range(min(a, b), max(a, b)):
        values.append(i)
    return values

def calculate_average(vals: list[int]) -> int:
    sum_vals = 0
    for i in vals:
        sum_vals+=i
    return sum_vals/len(vals)

def calculate_quotient(a: int, b: int) -> int:
    try:
        return a / b
    except ZeroDivisionError as ex:
        print(f"Exception was raised: {ex}")

def main():
    greet_user()
    nums = []
    for i in range(1, 3):
        nums.append(int(input(f"Enter the number {i}: ")))
    a, b = nums

    
    sum_result = calculate_sum(a, b)
    diff_result = calculate_difference(a, b)
    prod_result = calculate_product(a, b)
    quot_result = calculate_quotient(a, b)
    values = create_values(a, b)
    avg_result = calculate_average(values)

    print(f"Sum of {a} and {b}: {sum_result}")
    print(f"Difference of {a} and {b}: {diff_result}")
    print(f"Product of {a} and {b}: {prod_result}")
    if quot_result is not None:
        print(f"Quotient of {a} and {b}: {quot_result}")
    print(f"Average of values between and including {a} and {b}: {avg_result}")

if __name__ == "__main__":
    main()