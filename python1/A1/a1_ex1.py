# Create four variables of data types bool (boolean), int (integer), float (floating point) and str
# (string). You can choose arbitrary variable names and values (to use the unit test, you of course
# need to use the same values as in the example below). Print the variables (to the console) but with
# the following additional rules:

# • The integer must have a minimum print width of 7, must have leading zeros and should display
# its sign at the beginning of the line (irrespective whether it is positive or negative).
# • The float must have a minimum print width of 8, and the number of decimals (precision) must
# be set to 4.
# • The string must be printed two times next to each other, i.e., if the string is A, then AA must
# be printed.

# Example output for boolean = False, integer = -48, float = 1.5 and string = pythonisgreat (the
# ␣ character below represents a space, you do not have to literally print this character):
# False
# -000048
# ␣␣␣␣␣␣1.5000
# pythonisgreatpythonisgreat

B = False

I = -48

F = 1.5

S = "pythonisgreat"

print(B)
print(f"{I:+07d}")
print(f"{F:12.4f}")
print(S*2)



