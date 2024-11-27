# -*- coding: utf-8 -*-
"""
Author -- Michael Widrich, Andreas Schörgenhumer, Rainer Dangl
Contact -- dangl@ml.jku.at
Date -- 25.11.2024

###############################################################################

The following copyright statement applies to all code within this file.

Copyright statement:
This material, no matter whether in printed or electronic form, may be used for
personal and non-commercial educational use only. Any reproduction of this
material, no matter whether as a whole or in parts, no matter whether in 
printed or in electronic form, requires explicit prior acceptance of the 
authors.

###############################################################################

Example solutions for tasks in the provided tasks file.
"""

#
# Task 1
#

# Create a class "Face" with an attribute "orientation" and two methods
# "look(new_orientation)" and "show()". "new_orientation" is a string argument.
# If "new_orientation" is the string "left", let the attribute "orientation"
# point to string "left". If "new_orientation" is the string "right", let the
# attribute "orientation" point to string "right". "show" should print a face in
# "right" or "left" orientation, based on the current value of "orientation".
# The default initialization is "left". Example:
# face = Face()
# face.look("left")
# face.show()  # Prints "<.<"
# face.look("right")
# face.show()  # Prints ">.>"
# Also implement a method "get_info()" that returns a string of the form:
# "Face is looking <orientation>", where <orientation> is the value of the
# attribute "orientation".

# Your code here #


class Face:
    
    def __init__(self):
        self.orientation = "left"
    
    def look(self, new_orientation):
        if new_orientation == "left" or new_orientation == "right":
            self.orientation = new_orientation
    
    def show(self):
        if self.orientation == "left":
            print("<.<")
        elif self.orientation == "right":
            print(">.>")
    
    def get_info(self):
        return f"{type(self).__name__} is looking {self.orientation}"


face = Face()
face.look("right")
face.show()
face.look("left")
face.show()
print(face.get_info())


# Alternative solution with a helper method "_get_name":
class Face:
    
    def __init__(self):
        self.orientation = "left"
    
    def _get_name(self):
        return "Face"
    
    def look(self, new_orientation):
        if new_orientation == "left" or new_orientation == "right":
            self.orientation = new_orientation
    
    def show(self):
        if self.orientation == "left":
            print("<.<")
        elif self.orientation == "right":
            print(">.>")
    
    def get_info(self):
        return f"{self._get_name()} is looking {self.orientation}"


#
# Task 2
#

# Create a class "OwlFace" that is derived from class "Face" from task 1.
# Override the method "look" as follows: If "new_orientation" is the string
# "left", let the attribute "orientation" point to string "left". If
# "new_orientation" is the string "right", let the attribute "orientation" point
# to string "right". If "new_orientation" is the string "ahead", let the
# attribute "orientation" point to string "ahead". Make sure to reuse code from
# the base class "Face". "show" should print a face in "right", "left" or
# "ahead" orientation, based on the current value of "orientation". Example:
# face = OwlFace()
# face.look("left")
# face.show()  # Prints "(O<O)"
# face.look("right")
# face.show()  # Prints "(O>O)"
# face.look("ahead")
# face.show()  # Prints "(OvO)"
# Also implement a method "get_info()" that returns a string of the form:
# "OwlFace is looking <orientation>", where <orientation> is the value of the
# attribute "orientation". Try to reuse as much code as possible from the base
# class "Face". Ideally, you do not need to override this method at all!

# Your code here #


class OwlFace(Face):
    
    def look(self, new_orientation):
        if new_orientation == "ahead":
            self.orientation = new_orientation
        else:
            super().look(new_orientation)
    
    def show(self):
        if self.orientation == "left":
            print("(O<O)")
        elif self.orientation == "right":
            print("(O>O)")
        elif self.orientation == "ahead":
            print("(OvO)")


face = OwlFace()
face.look("left")
face.show()
face.look("right")
face.show()
face.look("ahead")
face.show()
print(face.get_info())


# Alternative solution with overriding only the helper method "_get_name":
class OwlFace(Face):
    
    def _get_name(self):
        return "OwlFace"
    
    def look(self, new_orientation):
        if new_orientation == "ahead":
            self.orientation = new_orientation
        else:
            super().look(new_orientation)
    
    def show(self):
        if self.orientation == "left":
            print("(O<O)")
        elif self.orientation == "right":
            print("(O>O)")
        elif self.orientation == "ahead":
            print("(OvO)")


#
# Task 3
#

# Create a class "Transformer" with two methods that operate on numerical lists:
#   > _transform(self, list_): A "private" method that takes a list as input,
#     processes/transforms this list and returns the processed/transformed list.
#     Since "Transformer" does not convey which transform operation should be
#     performed, the method should be considered "abstract", i.e., without any
#     actual implementation: Use "raise NotImplementedError" to indicate that
#     subclasses must overwrite this method. For more details, see
#     https://docs.python.org/3/library/exceptions.html#NotImplementedError
#   > transform(self, lists): This method takes a list of lists as input and
#     calls the "_transform" method for each list, collecting the returned lists
#     into a new list which is then returned.
# Afterwards, create these concrete transformer classes (concrete meaning that
# you have to implement the abstract method "_transform"):
#   > "AbsTransformer": Extends "Transformer". Returns the absolute values in
#     the list.
#   > "ScaleTransformer": Extends "Transformer". Has an "__init__" method with
#     two arguments "min_" and "max_" that will be used to scale the values in
#     the list to the interval [min_, max_].
#   > "NormalizeTransformer": Extends "ScaleTransformer" by setting "min_" and
#     "max_" to 0 and 1, respectively (i.e., a "NormalizeTransformer" is simply
#     a "ScaleTransformer" with 0 and 1 as fixed values).
# Finally, create a transformer object of each of the three classes and apply
# their transformation on the given input "example_lists:
#
# example_lists = [[0, 2, 7], [-1, -2, 10, 13, -1, 5]]
# example_lists -> AbsTransformer -> ScaleTransformer (with min_=1 anx max_=10)
# -> NormalizeTransformer
#
# The final result after the normalization transformation should be the
# following list (minor precision differences due to floating point numbers
# might occur):
# [[0.0, 0.2857142857142857, 1.0],
#  [0.0, 0.09999999999999999, 0.8999999999999999, 1.0, 0.0, 0.39999999999999997]]
example_lists = [[0, 2, 7], [-1, -2, 10, 11, -1, 5]]

# Your code here #


class Transformer:
    
    # The parameterized return type hint means "a list of lists"
    def transform(self, lists) -> list[list]:
        return [self._transform(list_) for list_ in lists]
    
    def _transform(self, list_: list) -> list:
        # Must be implemented by subclasses
        raise NotImplementedError


class AbsTransformer(Transformer):
    
    def _transform(self, list_: list) -> list:
        return [abs(i) for i in list_]


class ScaleTransformer(Transformer):
    
    def __init__(self, min_, max_):
        # Calling "super.__init__" is actually not required here, since the base
        # class "Transformer" does not have an "__init__" method
        super().__init__()
        self.min = min_
        self.range = max_ - min_

    def _transform(self, list_: list) -> list:
        list_min = min(list_)
        list_range = max(list_) - list_min
        return [((i - list_min) / list_range) * self.range + self.min for i in list_]


class NormalizeTransformer(ScaleTransformer):
    
    def __init__(self):
        super().__init__(min_=0, max_=1)


at = AbsTransformer()
at_lists = at.transform(example_lists)
st = ScaleTransformer(1, 10)
st_lists = st.transform(at_lists)
nt = NormalizeTransformer()
nt_lists = nt.transform(st_lists)


#
# Task 4
#

# Create a class "Product" with the following attributes and methods:
#   > "price": A float attribute that stores the price of the product.
#   > "stock": A class attribute that stores the total stock of products.
#   > "__init__(self, price: float)": Initializes the product with a price.
#   > "price": A property that returns the price of the product.
#   > "price": A setter that sets the price of the product.
# Create a class "Book" that is derived from class "Product" with the following
# attributes and methods:
#   > "author": A string attribute that stores the author of the book.
#   > "title": A string attribute that stores the title of the book.
#   > "__init__(self, price: float, author: str, title: str)": Initializes the
#     book with a price, author, and title. The stock of books should be
#     increased by 1 when a new book is created.
# Create a class "AudioBook" that is derived from class "Product" with the
# following attributes and methods:
#   > "author": A string attribute that stores the author of the audiobook.
#   > "title": A string attribute that stores the title of the audiobook.
#   > "duration": A float attribute that stores the duration of the audiobook
#     (in hours).
#   > "__init__(self, price: float, author: str, title: str, duration: float)":
#     Initializes the audiobook with a price, author, title, and duration. The
#     stock of audiobooks should be increased by 1 when a new audiobook is
#     created.
# Create the following objects and print their information:
#   > book1 = Book(10.99, "Stephen King", "Black House")
#   > book2 = Book(18.99, "Stephen King", "It")
#   > audiobook1 = AudioBook(9.99, "Sally Rooney", "Normal People", 10.5)
# Print the information of the objects and the total stock of books and
# audiobooks. Change the price of "book1" to 12.99 and print the new price of
# "book1".

# Your code here #



from abc import ABC, abstractmethod

class Product(ABC):

    stock = 0
    
    def __init__(self, price: float):
        self._price = price

    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, price: float):
        self._price = price
    
    def sell(self):
        Product.stock -= 1



class Book(Product):
    
    def __init__(self, price: float, author: str, title: str):
        super().__init__(price)
        self._author = author
        self._title = title
        Book.stock += 1
    
    @property
    def author(self) -> str:
        return self._author
    
    @property
    def title(self) -> str:
        return self._title


class AudioBook(Product):
    
    def __init__(self, price: float, author: str, title: str, duration: float):
        super().__init__(price)
        self._author = author
        self._title = title
        self._duration = duration
        AudioBook.stock += 1
    
    @property
    def author(self) -> str:
        return self._author
    
    @property
    def duration(self) -> float:
        return self._duration
    
    @property
    def title(self) -> str:
        return self._title

    
book1 = Book(10.99, "Stephen King", "Black House")
book2 = Book(18.99, "Stephen King", "It")
audiobook1 = AudioBook(9.99, "Sally Rooney", "Normal People", 10.5)

print(f"Book 1: {book1.title} by {book1.author}, price: {book1.price}")
print(f"Book 2: {book2.title} by {book2.author}, price: {book2.price}")
print(f"AudioBook 1: {audiobook1.title} by {audiobook1.author}, \
      price: {audiobook1.price}, duration: {audiobook1.duration}")
print(f"Total stock of books: {Book.stock} items")
print(f"Total stock of audiobooks: {AudioBook.stock} items")

book1.price = 12.99
print(f"Book 1: {book1.title} by {book1.author}, price: {book1.price}")
