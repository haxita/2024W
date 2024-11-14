# Exercise 2 – Submission: a2_ex2.py 25 Points
# Write a program that repeatedly reads positive integer numbers from the console using a while loop
# (see the example input and output below for how it must look like) and multiplies them. You do not
# need to store all values, only the current input is relevant. The loop should exit in two situations:
# • When the user inputs an"x" instead of a positive integer number. In this case, the program
# should output the product of all numbers entered.
# • Should the product become greater than the value 1000, the program should exit the loop
# immediately (without the user needing to type"x"). Then a message along with the result
# should be printed:"Result has exceeded the value 1000: XXXX" Where "XXXX" is the
# computed product.
# Ensure that your program works for an empty sequence of numbers (i.e., the user immediately
# entered "x"), in which case you must print"Empty sequence". You do not need to check the input,
# you can assume that they are positive integers.
# Example input and output:
# Enter a value (or'x' to stop): x
# Empty sequence
# Example input and output:
# Enter a value (or'x' to stop): 4
# Enter a value (or'x' to stop): x
# Result: 4
# Example input and output:
# Enter a value (or'x' to stop): 4
# Enter a value (or'x' to stop): 5
# Enter a value (or'x' to stop): 3
# Enter a value (or'x' to stop): 2
# Enter a value (or'x' to stop): x
# Result: 120
# Example input and output:
# Enter a value (or'x' to stop): 9
# Enter a value (or'x' to stop): 7
# Enter a value (or'x' to stop): 7
# Enter a value (or'x' to stop): 4
# Result has exceeded the value 1000: 1764


has_input = False
prod = 1

while True:
    num = input(f"Enter a value (or 'x' to stop): ")

    if num == "x":
        if not has_input:
            print("Empty sequence")
        else :
            print(f"Result: {prod}")
        break

    num = int(num)
    prod *= num
    has_input = True

    if prod > 1000:
        print(f"Result has exceeded the value 1000: {prod}")
        break
