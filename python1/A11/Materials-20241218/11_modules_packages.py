# -*- coding: utf-8 -*-
"""
Author -- Michael Widrich, Andreas Schörgenhumer, Rainer Dangl
Contact -- dangl@ml.jku.at
Date -- 15.12.2024

###############################################################################

The following copyright statement applies to all code within this file.

Copyright statement:
This material, no matter whether in printed or electronic form, may be used for
personal and non-commercial educational use only. Any reproduction of this
material, no matter whether as a whole or in parts, no matter whether in 
printed or in electronic form, requires explicit prior acceptance of the 
authors.

###############################################################################

In this file, we will learn about recursive functions, generator functions and
how to import Python modules.
https://docs.python.org/3/tutorial/classes.html#generators
https://docs.python.org/3/tutorial/modules.html
"""

###############################################################################
# Modules
###############################################################################

#
# Importing modules
#

# You can import existing modules (=Python files) via the "import ..." or
# "import ... as ..." statement. Afterward, you can use its contents. Here, the
# full module will be imported:
import sys
python_executable = sys.executable
# This imports the module "sys" and binds it to the name "sys". You can now
# access the content of the module using the "." operator.

# You can check the content of the module using the "dir" function:
dir(sys)

# Many Python modules have suggested nicknames. You can choose a different name
# of the imported module using the "as" keyword:
import sys as system
encoding_in_this_python = system.getdefaultencoding()

# Use "from ... import ..." to only import a specific part of a module (can be
# a submodule, function, global variable, class, etc.):
from os import path
correct_path = path.join("some", "directory")
# To be precise, this imports names from the module into our global/module
# namespace without importing the import module name (e.g., "os" is undefined).

# You can import multiple modules with one statement using commas
import os, sys
from os import path, makedirs
print(os, sys, path, makedirs)

# If you import a module multiple times, Python will, by default, perform the
# import only once.

# You can also import all names from a module using the "*" operator. This is
# generally discouraged because it can overwrite existing names in your
# namespace and make it unclear where a name comes from:
from os import *
print(makedirs)


#
# Creating and using custom modules
#

# If you want to reuse content from your own files, you can simply import it
# from there. Always make sure that the PYTHONPATH environment variable is set
# correctly or the module is within your working directory. Python will search
# within the PYTHONPATH and the working directory (and an installation-
# dependent default) for the module.

# On a linux system, you can set the PYTHONPATH environment variable using:
# export PYTHONPATH=/path/to/your/module:$PYTHONPATH
# To add a directory permanently, add the line to your ~/.bashrc file.

# The following line imports function "add" from file "my_module.py" and binds
# it to the name "my_add":
from my_module import add as my_add

argument_list = list(range(10))
print(my_add(*argument_list))

# When importing from a file, the content of the file will be executed. Often,
# we want to include code that should only be executed when using the file as
# main file (= execute only when calling the file but not when importing from
# it). This can be done using the following syntax:

print("This code will be executed when this file is imported")

if __name__ == "__main__":
    print("This code will not be executed when this file is imported")

# You can check the example in "my_module.py" by executing "my_module.py"
# directly, i.e., executing it as a script with "python my_module.py".

#
# Packages
#

# To better structure your code files, you can put them into directories. To
# make Python recognize files within directories, place an empty "__init__.py"
# file inside, which makes the directory a Python package. The following
# examples are directly taken from the official Python tutorial:
# https://docs.python.org/3/tutorial/modules.html#packages

# Suppose you have the following project structure:
# sound/                          Top-level package
#       __init__.py               Initialize the sound package
#       formats/                  Subpackage for file format conversions
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  Subpackage for sound effects
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  Subpackage for filters
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py
#               ...

# You can then import from your main "sound" package as follows (examples):
# import sound  # Import the main package
from sound.effects import echo  # Import the submodule "echo"
# from sound.effects.echo import echofilter  # Import the function "echofilter"
# from sound.formats import wavread  # Import the submodule "wavread"
# from sound.formats.wavread import readwav  # Import the function "readwav"