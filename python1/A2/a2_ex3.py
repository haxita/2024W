# Exercise 3 – Submission: a2_ex3.py 25 Points
# Using the built-in range(start, stop, step), write a program that reads these three integer num-
# bers and iterates through the value range. Your program must do the following (see the example
# input and output below for how it must look like):
# • Compute the sum of all even values.
# • Compute the sum of all uneven values multiplied with the respective index (value × index for
# every iteration and the sum of that).
# • For the first and last 5 values, print them to the console in the format that you see below. If
# the user-specified range results in less than 5 values, just print those. If the range is more than
# 5 but less than 10 (so that you cannot print 5 first and 5 last values), just print all steps.
# • After the iteration, print both the even-value sum as well as the sum of odd values times their
# indices. If the range does not contain any values (an empty range) or if there are no even/odd
# values, the respective sum must be set to 0. Important: the upper boundary (stop) should be
# included in the iteration.
# Example input and output:
# Start: 1
# Stop: 10
# Step: 3
# Index: 0, Value: 1
# Index: 1, Value: 4
# Index: 2, Value: 7
# Index: 3, Value: 10
# Sum of even values: 14
# Sum of odd multiplied values: 14
#
# Example input and output:
# Start: 0
# Stop: 100
# Step: 1
# Index: 0, Value: 0
# Index: 1, Value: 1
# Index: 2, Value: 2
# Index: 3, Value: 3
# Index: 4, Value: 4
# Index: 96, Value: 96
# Index: 97, Value: 97
# Index: 98, Value: 98
# Index: 99, Value: 99
# Index: 100, Value: 100
# Sum of even values: 2550
# Sum of odd multiplied values: 166650
# Example input and output:
# Start: 59
# Stop: 20
# Step: 1
# Sum of even values: 0
# Sum of odd multiplied values: 0
# Example input and output:
# Start: 9
# Stop: 40
# Step: 5
# Index: 0, Value: 9
# Index: 1, Value: 14
# Index: 2, Value: 19
# Index: 3, Value: 24
# Index: 4, Value: 29
# Index: 5, Value: 34
# Index: 6, Value: 39
# Sum of even values: 72
# Sum of odd multiplied values: 388

start = int(input("Start: "))
stop = int(input("Stop: "))
step = int(input("Step: "))

if step == 0:
    values = []
elif (step > 0 and start > stop) or (step < 0 and start < stop):
    values = []
else:
    values = list(range(start, stop + 1, step)) if step > 0 else list(range(start, stop - 1, step))

sum_even = 0
sum_odd_times_index = 0

for idx, val in enumerate(values):
    if val % 2 == 0:
        sum_even += val
    else:
        sum_odd_times_index += val * idx

num_values = len(values)
if num_values == 0:
    pass
elif num_values < 5:
    for idx, val in enumerate(values):
        print(f"Index: {idx}, Value: {val}")
elif 5 <= num_values < 10:
    for idx, val in enumerate(values):
        print(f"Index: {idx}, Value: {val}")
else:
    for idx, val in enumerate(values[:5]):
        print(f"Index: {idx}, Value: {val}")
    for idx, val in enumerate(values[-5:], start=num_values - 5):
        print(f"Index: {idx}, Value: {val}")

print(f"Sum of even values: {sum_even}")
print(f"Sum of odd multiplied values: {sum_odd_times_index}")
