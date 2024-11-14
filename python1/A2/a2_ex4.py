# Write a program that prints a diamond over a user-specified size (number of rows/lines - integer). If
# this number is less than 2, then print"Invalid size". Otherwise print a diamond over the entered
# number of lines consisting of the character * (see the example input and output below for how it
# must look like). In order to draw this, the size needs to be an uneven number. If the user enters an
# even number, just increment it by one. This means that for example a size of 10 results in the same
# output than a size 11. Examples for such “diamonds” for sizes 5 and 7:

size = int(input("Diamond size: "))

if size < 2:
    print("Invalid size")
else:
    if size % 2 == 0:
        size += 1

    mid = size // 2

    for i in range(size):
        if i <= mid:
            # Upper half
            spaces_before = mid - i
            if i == 0:
                line = ' ' * spaces_before + '*' + ' ' * spaces_before
            else:
                inner_spaces = 2 * i - 1
                line = ' ' * spaces_before + '*' + ' ' * inner_spaces + '*' + ' ' * spaces_before
        else:
            # Lower half
            j = size - i - 1
            spaces_before = mid - j
            if j == 0:
                line = ' ' * spaces_before + '*' + ' ' * spaces_before
            else:
                inner_spaces = 2 * j - 1
                line = ' ' * spaces_before + '*' + ' ' * inner_spaces + '*' + ' ' * spaces_before
        print(line)