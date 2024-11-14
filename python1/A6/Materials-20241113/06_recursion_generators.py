# -*- coding: utf-8 -*-
"""
Author -- Michael Widrich, Andreas Schörgenhumer, Rainer Dangl
Contact -- dangl@ml.jku.at
Date -- 11.11.2024

################################################################################

The following copyright statement applies to all code within this file.

Copyright statement:
This material, no matter whether in printed or electronic form, may be used for
personal and non-commercial educational use only. Any reproduction of this
material, no matter whether as a whole or in parts, no matter whether in printed
or in electronic form, requires explicit prior acceptance of the authors.

################################################################################

In this file, we will learn about recursive functions, generator functions and
how to import Python modules.
https://docs.python.org/3/tutorial/classes.html#generators
https://docs.python.org/3/tutorial/modules.html
"""

################################################################################
# Recursion
################################################################################

# Functions are allowed to call themselves recursively. Typically, you split the
# entire task into a smaller subtask that you can solve immediately and the
# rest. The (now smaller) rest is processed by the same function until the rest
# is simple enough to also solve it immediately, which serves as the recursion
# end (base case or recursion anchor). Remember that there must be an end of the
# recursion somewhere and that there must be progress within the recursion
# (e.g., when splitting something, the rest should be smaller than before
# splitting), or otherwise, you will have an endless recursion.


# Example: Power function that calculates x^y. Assumptions: y: int >= 1
def power(x, y):
    # Base case: x^1 = x
    if y == 1:
        return x
    # Split into subtask of a multiplication of one "x" with the rest x^(y - 1),
    # i.e., x^y = x * x^(y - 1)
    return x * power(x, y - 1)


# There can be multiple ends of a recursion, i.e., multiple base cases, and
# multiple recursive calls (either in different branches or even subsequent
# calls). Example: Power function that calculates x^y. Assumptions: y: int
def power(x, y):
    # Base case 1: x^0 = 1
    if y == 0:
        return 1
    # Base case 2: x^1 = x
    if y == 1:
        return x
    # Recursion case 1: y > 0, which means x^y
    # Split into subtask of a multiplication of one "x" with the rest x^(y - 1),
    # i.e., x^y = x * x^(y - 1)
    if y > 0:
        return x * power(x, y - 1)
    # Recursion case 2: y < 0, which means x^-y = 1 / (x^+y)
    # Same idea of splitting into subtask and rest as above, just with
    # appropriate changes for the negative case. Here, we already know x^+y, so
    # our subtask is simply the division (and the negation of "y"). While we do
    # not split something off here, we still achieve recursion progress: We
    # negate "y", which leads to case 1 of the recursion and ultimately its end.
    return 1 / power(x, -y)


# Example: Summation of arbitrary many arguments
def add(*args):
    # Base case 1: no args -> return 0
    if len(args) == 0:  # Equal to: if not args:
        return 0
    # Base case 2: one arg -> return this arg
    if len(args) == 1:
        return args[0]
    # Otherwise, split into subtask of sum of first arg and the rest (args[1:])
    return args[0] + add(*args[1:])


# Simpler solution (make use of the fact that slicing with a too large start
# index, i.e., seq[start:] with start >= len(seq), yields an empty sequence)
def add(*args):
    # Base case: no args -> return 0
    if not args:
        return 0
    # Split into subtask of sum of first arg and the rest (args[1:]). Here, the
    # rest might be empty, which is OK, as we have a matching base case.
    return args[0] + add(*args[1:])


################################################################################
# Generators: Using a function as an iterable with "yield"
################################################################################

# Instead of writing "return", we can also write "yield" within a function. This
# will make the function a so-called generator function that returns a generator
# iterator object which can be used to iterate through elements yielded by this
# function. This generator object stores the state of the function. Everytime an
# element is requested (e.g, using a for loop), the code is executed until the
# yield statement is reached and the specified value is returned. The execution
# is then suspended at this point until the next element is requested, and the
# execution is then resumed again until the next yield is encountered or there
# are no more elements to yield. This means the code is executed when needed
# rather than processing all elements immediately and returning them as, e.g., a
# list. https://docs.python.org/3/glossary.html#term-generator

# Example with a fixed number of iterations:
def iterable_function(n_elems):
    # Code we write here will be executed only once
    print("executed once when the first element is requested")
    for x in range(n_elems):
        # Code we write here will be executed at every iteration
        print("In function:", x)
        # Variable "x" will be returned at every iteration and the current state
        # of the function is saved (e.g., local variables). When another value
        # is requested, the function is resumed after the yield statement,
        # thereby restoring its entire state exactly as it was before.
        yield x
    # No more elements to yield, function terminates
    print("code completed")


for i in iterable_function(5):
    print(f"Function yielded: {i}")


# Another example with infinitely many elements:
def infinite_random_numbers():
    import random  # See further below for more information on module imports
    while True:
        yield random.random()  # float in the range [0.0, 1.0)


# Would result in an endless loop:
# for r in infinite_random_numbers():
#     print(r)

# Solution: We can also use the built-in function "next" to access the next
# element of a so-called iterator object, and a generator function returns such
# an iterator (a generator iterator).
# https://docs.python.org/3/glossary.html#term-generator-iterator
# https://docs.python.org/3/library/functions.html#next
inf = infinite_random_numbers()
for _ in range(5):  # Use an underscore to ignore the result of "range"
    print(next(inf))


# You can still use "return" in conjunction with "yield". If encountered during
# the execution, this will simply end the generator function, i.e., no more
# values will be produced after a "return". Manually calling "next" on an
# iterator that has no more elements will lead to a "StopIteration" exception.
def yield_with_return():
    for j in range(10):
        if j == 3:
            return
        yield j


gen = yield_with_return()
for i in gen:
    print(i)
# This would lead to an exception since there are no more elements:
# next(gen)

#
# Generator expressions
#

# In the data structures unit, we introduced list comprehensions. When replacing
# the brackets [] with parentheses (), this creates a new construct that is
# called a generator expression, which will be evaluated dynamically rather than
# creating a full list. The explanation behind this is that a generator iterator
# will be created. From the official tutorial
# https://docs.python.org/3/tutorial/classes.html#generator-expressions:
# "These expressions are designed for situations where the generator is used
# right away by an enclosing function. Generator expressions are more compact
# but less versatile than full generator definitions and tend to be more memory
# friendly than equivalent list comprehensions."
gen = (i**2 for i in range(10))  # If written like this, can only use it once!
print(sum(gen))  # Prints 285
print(sum(gen))  # Prints 0 ("gen" was already used and does not yield any more elements)
print(sum(i**2 for i in range(10)))  # Better: Enclose directly (parentheses now optional)


################################################################################
# Recursive functions vs iterative functions
################################################################################

# Recursive functions can be more elegant and easier to understand than iterative
# functions, but they can also be less efficient. This is because every recursive
# call requires a new stack frame to be created, which consumes memory. If the
# recursion depth is too high, this can lead to a "RecursionError" exception. In
# contrast, iterative functions do not require additional stack frames and can be
# more memory-efficient. However, they can be more complex and harder to
# understand than recursive functions. In general, you should use the right tool
# for the job: If the problem can be solved elegantly with recursion and the
# recursion depth is not too high, you should use a recursive function. If the
# problem is better solved with an iterative function, you should use an
# iterative function. In some cases, you can also combine both approaches to
# create a hybrid solution. For example, you can use a recursive function to
# solve a problem and then use an iterative function to optimize the solution.
# In general, you should always strive for simplicity and readability in your
# code. If you find that a recursive function is too complex or hard to
# understand, you should consider refactoring it into an iterative function or
# breaking it down into smaller, more manageable functions.

# Example: Fibonacci function using recursion
def fibonacci_rec(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

# Example: Fibonacci function using iteration
def fibonacci_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Let's measure the time it takes to calculate the 30th Fibonacci number using
# both the recursive and iterative functions. We will use the "time" module to
# measure the time it takes to execute the functions. The "time" module provides
# various functions for working with time, including functions for measuring the
# time it takes to execute code. https://docs.python.org/3/library/time.html
import time

start = time.time()
fibonacci_rec(40)
end = time.time()
print(f"Time taken by recursive function: {end - start:.6f} seconds")


start = time.time()
fibonacci_iter(40)
end = time.time()
print(f"Time taken by iterative function: {end - start:.6f} seconds")