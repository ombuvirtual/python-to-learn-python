# Invoking Python
# ===============

# Running a script file
# ---------------------

# If your source code is contained in a file you can run it by passing
# its file name as an argument to the ``python`` command. For example,
# suppose you have a script named ``myscript.py``, then to run it you
# enter ``python myscript.py`` in the command line and press enter.

# Let's create a simple script named ``myscript.py`` with a single
# line of Python code that issues a call to the built-in function
# ``print()`` to print a string to ``stdout`` and let's run it by
# passing its file name as an argument to the ``python`` command, ::

#: write a single line of source code to myscript.py file
echo 'print("invoked by passing filename as argument")' > myscript.py

#: run script by passing filename as an argument to python
python myscript.py

# Running script as a shell command
# ---------------------------------

# In GNU/Linux systems it is possible to run a Python script as a *shell
# command*. This means you can run the script by entering its name
# directly on the command line without having to explicitly invoke the
# ``python`` command or specify the path of the script.

# To be able to invoke your script like a shell command you need to do
# three things:

# + You must make the first line of the script begin with the 'magic'
#   characters ``#!``, followed by the path of the Python interpreter
#   you want to invoke to run the script. The rest of the file
#   contains your Python source code.

# + You have to make the script file executable. You can do that using
#   the ``chmod`` shell command.

# + To run the script from anywhere in the filesystem without having
#   to specify its path you have to place it in a directory that is in
#   the shell's command search path. 

# The following example creates a script called ``myscript.sh``. The
# first line of the script starts with the magic characters ``#!``
# followed by the path ``/usr/bin/python``, the path of the
# interpreter that will be invoked by the system to run the source
# code. In this simple example the source code consists of a single
# line of code, a call to the built-in function ``print()`` to print
# the string ``"invoked as a shell command"``, ::

#: the first line in the script indicates which interpreter
#: the system should invoke to run the source code
echo "#! /usr/bin/python" > myscript.sh

#: the source code is just a call to print
echo 'print("invoked as a shell command")' >> myscript.sh

# Now we have a script with the appropriate first line to invoke the
# Python interpreter. However, to run it as a shell command we must
# first make the script file executable. We can do that using the
# shell command ``chmod``, ::

#: make script file executable
chmod u+x myscript.sh

# We can now run ``myscript.sh`` by specifying its path but without
# having to explicitly invoke the Python interpreter in the command
# line. If the script is located in our current working directory then
# its path is ``./myscript.sh`` and we can run it as shown in the
# following snippet, ::

#: run script in current working directory
./myscript.sh

# To be able to run the script without having to specify its path you
# have to place it in a directory that is in the shell's command
# search path. If you want to make the script accessible system wide,
# a good location is ``/usr/local/bin``. In some GNU/Linux systems you
# can create a bin directory just under your home directory,
# ``~/bin``. Placing your script in your ``~/bin`` directory makes it
# accessible only to you. Wherever you place your script, as long as
# it's in the shell's command search path, you'll be able to run it
# from anywhere in the filesystem by simply entering its name in the
# command line.
