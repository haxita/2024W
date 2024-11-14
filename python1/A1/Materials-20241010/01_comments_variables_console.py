# -*- coding: utf-8 -*-
"""
Author -- Michael Widrich, Andreas Schörgenhumer, Rainer Dangl
Contact -- dangl@ml.jku.at
Date -- 09.10.2024

################################################################################

The following copyright statement applies to all code within this file.

Copyright statement:
This material, no matter whether in printed or electronic form, may be used for
personal and non-commercial educational use only. Any reproduction of this
material, no matter whether as a whole or in parts, no matter whether in printed
or in electronic form, requires explicit prior acceptance of the authors.

################################################################################

In this file, we will learn about syntax, comments and docstrings in Python,
common Python variables, variable operations and data type conversions, and
about printing output to the console as well as reading input from it.

For more details on Python functionality in general, see the official
documentation and tutorial:
https://docs.python.org/3/
https://docs.python.org/3/tutorial/index.html
https://docs.python.org/3/tutorial/introduction.html
"""

################################################################################
# Docstrings
################################################################################

# Python offers the option for a description at the beginning of each file,
# function or class which is called "docstring" and is enclosed in three double
# quotes. What you can see above is such a docstring. Docstrings are for
# documentation purposes of modules, functions, classes or methods. For now, we
# do not really need to know about them, but we will encounter them again when
# we learn about functions.

# The content in docstrings can range from short notes to extensive
# documentation with input/output arguments etc. It will automatically be parsed
# (if possible) and displayed in the help for the specific function or class. In
# PyCharm, you can toggle this help by left-clicking on a function or class and
# pressing Ctrl+q or selecting "Quick Documentation" in the "View" menu bar.

# There are different conventions/styles on how to write docstrings. If you are
# working on an existing project, make sure to use the same style. If you set up
# your own project, choose any style you want and then stay consistent. The
# general conventions for docstrings can be found here:
# https://www.python.org/dev/peps/pep-0257/


################################################################################
# Comments
################################################################################

# Comments are part of a Python file that are not executed, i.e., they don't do
# anything. Comments in Python start with a hashtag (#). You can also place
# comments after non-comment statements using a hashtag. Since this line starts
# with a character, it is a comment.

# There are conventions and advices regarding code style in Python, such as
# https://www.python.org/dev/peps/pep-0008/. It will help you a lot to keep your
# code readable and clean, however, Python does not explicitly force you to
# follow it. We will stick to this style as good as possible in this lecture.
# PyCharm tries to highlight code that goes against PEP standards.


################################################################################
# General
################################################################################

# Python program code is stored in text files. The standard filename suffix
# indicating a Python file is ".py", e.g., "my_file.py".

# A Python code file is executed line by line (from top to bottom of the file).
# Python evaluates expressions from left to right, but when evaluating an
# assignment, the right-hand side is evaluated before the left-hand side.
# https://docs.python.org/3/reference/expressions.html#evaluation-order
# https://docs.python.org/3/reference/expressions.html#operator-precedence


################################################################################
# Variables
################################################################################

#
# General
#

# Variables in Python are just references to objects that are generated, stored
# and managed automatically in the background, i.e., they are essentially only
# names or identifiers that are bound to objects - they themselves do not store
# any information. Variable names must start with characters that are not digits
# and not operators. Python variables are case-sensitive. Use all lowercase
# names with underscores for variables.

# In the next line, a variable "var" is created that is bound to a string object
# with content "hello, world!", which is created and stored somewhere in the
# background. This is done via the assignment operator "=", where the variable
# name is on the left and the content to assign is on the right-hand side of the
# equals sign.
var = "hello, world!"

# We can change the type and content of a variable at any time, since the
# variable is just a reference to some object stored in the background. We can,
# e.g., let it point to the integer object 5 now:
var = 5

#
# Error messages
#

# Variable names must not start with digits. Try to run this line in your Python
# console without the hashtag:
# 1var = 5
# You will see that you receive an error message (SyntaxError). Such error
# messages can help you a lot to find out what went wrong. Try to get familiar
# with reading and using them.


################################################################################
# Immutability
################################################################################

# All the following data types (boolean, integer, float, string) are so-called
# immutable data types. This means that an object of such a data type cannot be
# changed. Any kind of "modification" thus actually produces a new object
# containing the result. For now, we do not have to worry about this, but the
# concept of immutability (and mutability) will become very important when we
# talk about data structures in a later unit.


################################################################################
# Data types (1)
################################################################################

#
# Booleans ("bool")
#

# Booleans can take the values True or False. They are used for binary
# information, like checking whether a condition is fulfilled or not.

# Here, we create a boolean variable with content True
true_variable = True
# Here, we create another boolean variable with content False
false_variable = False

# The "not" keyword can be used to negate a boolean
another_true_variable = not false_variable

# Internally, booleans are stored like integers (see below), where True has the
# value 1 and False has the value 0.

#
# Integer numbers ("int")
#

# Integer numbers can be created using digits.

# Here, we create a variable that points to an integer object 5.
an_integer = 5

# Integers are variable-length objects. This means that you do not have to worry
# about overflow problems when using integers with large values. This does come
# at the cost of being less (memory) efficient, but for now, that is not
# something we need to concern ourselves with (we will cover efficient
# mathematical computations later when talking about NumPy).

#
# Floating point numbers ("float")
#

# Floating point numbers can be created using digits combined with a dot.

# Here, we create a variable that points to a float object with value 3.563
a_float = 3.563

# Alternatively, we can use the character "e" between digits to indicate decimal
# powers for float numbers. Syntax: multiplier e decimal_power
another_float = 2e1  # Corresponds to 2 * 10^1 = 20.0
yet_another_float = 1e-3  # Corresponds to 1 * 10^-3 = 0.001

# Floating point numbers are usually stored as 8 bytes float (=64 bits float).
# Keep in mind that floating point values are stored with a fixed number of bits
# and therefore can lose precision.

#
# Making numbers more readable
#

# One can use underscore characters in numbers for readability:
large_int = 123_456_789
large_float = 123_456_789.123_456_789


################################################################################
# Mathematical operations
################################################################################

# Python supports all sorts of mathematical operations using the operators
# + for addition
# - for subtraction
# * for multiplication
# / for division
# ** for power of (syntax: a ** b corresponds to "a" to the power of "b")
# % modulo operation (get the remainder of a division)
# // get the floor value of a division (integer division)

# Addition of ints produces an int
sum_integer = an_integer + an_integer

# Addition of floats produces a float
sum_float = a_float + a_float

# Combining ints and floats produces a float
combination = an_integer + a_float

# Mathematical operations can be combined arbitrarily (common rules for order of
# mathematical operations, including parentheses, apply)
combination = ((an_integer + a_float * an_integer) / a_float) ** 5

# For ints and floats, you can use the syntax shortcuts +=, -=, etc. if you want
# to modify a variable directly
combination += 4  # Identical to: combination = combination + 4
combination /= 2.5  # Identical to: combination = combination / 2.5
combination **= 2  # Identical to: combination = combination ** 2

# If you combine boolean and other numbers, True will be 1 and False will be 0
combination -= True

# You can break long statements into multiple lines with a backslash "\"
combination += 4 + 6 - \
    3 + 5
# Or you can just put them into parentheses and have linebreaks
combination -= (1 + 2 +
                3)


################################################################################
# Data types (2)
################################################################################

#
# Strings ("str")
#

# A string is an object consisting of characters. Strings can be created using
# double quotes, single quotes, three double quotes, or three single quotes. The
# outer quote is always the relevant one.
a_string = "I am a string"
a_string = 'I am also a string'
a_string = 'You can use the other quotes " inside a string'
a_string = "... and the other way around: ' "
a_string = "Line one.\nLine 2.\nLine 3."  # "\n" is the newline character

# 3 quotes may include linebreaks (adds newline character "\n" automatically)
a_string = """I am a string...
and I include a linebreak
as I span multiple lines."""

# You can escape effects of quotes by using the escape character backslash "\"
a_string = 'I want to use " and \' in a string without ending it.'

# If you want to use backslashes in strings, you have to escape their own escape
# function, i.e., use a double backslash:
windows_path = "C:\\Windows\\System32"

# Alternatively, you can use a "raw" string by putting an "r" in front of the
# first quote to ignore the special meaning of characters:
windows_path = r"C:\Windows\System32"
# Note: If a backslash "\" is used as last character of a raw string, it has an
# additional special meaning and will escape the last quote character that
# would end the string. r"C:\Windows\System32\"" would be equivalent to
# r'C:\Windows\System32"'. If you want to use a "\" as last character, you will
# have to escape the special meaning, even in raw strings: r"C:\Windows\\".

#
# There are multiple convenience operations on strings:
#

# Concatenation
conc_strings = "I am " + "3 concatenated" + ' strings!'
conc_strings += " Plus one more!"
automatic_concatenation = "This will result in a single string as " \
                          "if it were " "manually concatenated"

# Case transformation (here, we actually use an advanced concept called methods,
# which we will learn later)
uppercase_string = conc_strings.upper()
lowercase_string = "SILENCE!".lower()

# Repetition
repeated_string = "bla" * 3

# This will not work but try it and try to understand the error message:
# not_possible = "bla" / 3

# Length (the used concept here is a function, which we will learn later)
string_length = len(conc_strings)

# Getting the i-th character of a string via "some_string[i]", where the index
# "i" must be in the range [0, len(some_string)). We will learn more about
# indexing later.
some_string = "hello"
char = some_string[0]  # Character at index 0 = first character = "h"
# However, since strings are immutable, assignment is not possible:
# some_string[0] = "a"

# Counting substrings
number_of_bla = repeated_string.count("bla")

# Replacing and finding substrings
replacement = "This is a placeholder".replace("placeholder", "string")
check_for_substring = "string" in conc_strings  # True if found, False otherwise
locate_substring = replacement.find("is a")  # Index if found, -1 otherwise

# More common string methods:
# http://docs.python.org/3/library/stdtypes.html#string-methods

# You can include all kinds of objects in strings with f"{variable_name}" using
# format strings. Format strings start with an "f" character
a = 1
b = 2.2
c = a + b
string = f"We calculated c = a + b = {a} + {b} = {c}"

# There are many types of formatting options available, like
long_number = 100 / 3
format_string = f"Format float values as :width.precision {long_number:10.5f}"
# You can even use variables, or expressions in general, in the options:
n_decimals = 3
another_formatted_string = f"{long_number:.{n_decimals}f}"

# For more information on string formatting and the available options, see
# https://docs.python.org/3/library/string.html#formatstrings

#
# None
#

# None is the sole value of the data type "NoneType" in Python. It typically
# represents the absence of a value. This will play a role later, when, e.g., a
# function does not return anything.
a = None


################################################################################
# Data type conversions
################################################################################

# If you want to convert an object to another data type, be careful since you
# might lose information! You can convert to data types like this:
val = 2.9
# Conversion of "val" to float (it actually already was a float here):
as_float = float(val)
# Conversion of "val" to int. Note how we lose the information after the
# floating point (it is not rounded to the nearest integer!):
as_int = int(val)
# Conversion of "val" to bool. For the data types from above, 0, 0.0, the empty
# string "" and None evaluate to False, everything else is True:
as_bool = bool(val)
# Conversion of "val" to str. Python will do its best to convert meaningfully:
as_string = str(val)
# NoneType cannot be converted to int or float, but can be "converted" to str:
# not_possible = int(None)
none_string = str(None)


################################################################################
# Type hints
################################################################################

# Python is a dynamically typed language, which means that you do not have to
# specify the data type of a variable when you create it. As mentioned above, 
# variables are essentially just references that point to objects in memory. 
# However, you can use type hints to specify the expected data type of a 
# variable. This is especially useful when you want to make your code more 
# readable.

# The syntax for type hints is to put a colon ":" after the variable name and
# then the expected data type. For example, if you want to specify that a
# variable "my_variable" should be an integer, you can write "my_variable: int".
# IMPORTANT: Type hints are only hints and do not enforce the data type of the
# variable. If you assign a value of a different data type to a variable with a
# type hint, Python will not raise an error.

# Here is an example of how to use type hints:
some_var: int = 5
some_other_var: str = "hello"

# Still, as mentioned above, the following lines will not raise an error, even
# though the type hint specifies that "some_var" should be an integer or a 
# string, respectively:
some_var = "five"
some_other_var = True

################################################################################
# Details on evaluation order
################################################################################

# Multiple assignments in one line are possible. Assignments are performed from
# right to left. The following line will create "var3" with content 8, then
# "var2" with content of "var3" and then "var1" with content of "var2":
var1 = var2 = var3 = 2 * 4


################################################################################
# Console input and output
################################################################################

# The console is the primary default input and output device. To create an
# output, we make use of the built-in function "print", which will print the
# specified object in its string representation to the console. By default, a
# newline character "\n" is automatically added at the end.
print("Hello, world!")  # This is already a string
print(123.456)  # Converts the float via "str" (see data type conversion above)

# Multiple objects can also be passed to "print", which will then be printed in
# sequential order, separated by a whitespace:
print("this", "will", "be", "separated", "by", 1, "whitespace")

# User input from the console can be retrieved with the function "input", which
# will read the input as string, i.e., appropriate data type conversion must be
# done manually afterward.
my_input = input("Please enter something: ")  # "my_input" will be a string
# Here, we again use a Python built-in called "type" that returns the data type
# of the object we passed (you can ignore the "__name__")
print(f"data type of 'my_input': {type(my_input).__name__}")
