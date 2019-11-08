# Minimal Python
# ==============

# How to define and print a string
# --------------------------------

# One of the first things you want to know when starting to learn a
# new programming language is how to define strings and how to print
# them to standard output. This allows you to display messages for
# immediate feedback when trying out new language constructs. You also
# want to know how to write comments in order to make notes about the
# code you are working on and language features you are exploring.

# In Python comments start with a ``#`` character. Everything on a
# line from the first ``#`` character to the end of the line is
# ignored by the interpreter. There are no multi-line comment
# delimeters like ``/*`` and ``*/`` in C and other languages. Each
# line of a multi-line comment must start with a ``#`` character. The
# following are examples of comments, ::

#: everything after first # character is a comment

#: any # characters after the first are part of the comment

#: line 1 of multi-line comment
#: line 2 of multi-line comment

# To define a string in the Python language you enclose the relevant
# text in double quotes. For example, if you want to define a string
# with the text ``a string defined with double quotes`` you enclose
# the text in double quotes and the Python interpreter will recognize
# it as a *string literal expression* and evaluate it to a string
# object. The following is an example of a string literal expression
# defined with double quotes, ::

#: a string literal defined with double quotes
"a string defined with double quotes"

# Note that the string expression above does not end with a statement
# termination character such as a semicolon. In the Python language
# statements are terminated by a *new line* character.

# However, the semicolon character ``;`` is used to separate multiple
# statements when they appear on the same line. For example, the two
# string expressions "foo" and "bar" can appear on the same line if
# separated by a semicolon, ::

"foo"; "bar"

# The string definitions above don't produce any ouput. They are
# evaluated by the interpreter and then discarded. To print them to
# standard output you use Python's built-in function ``print()``.

# The ``print()`` function takes a *variable* number of string
# arguments separated by comas. It automatically separates mutliple
# arguments with a space and adds a new line character at the end.
# The following example shows invocations of ``print()`` with
# different number of arguments. Note again that the statements end
# with a new line character, no special statement termination
# character is required. ::

#: print a string
print("a string defined with double quotes")

#: print two strings
print("first", "second")

#: print three strings,
#: you can span multiple lines
print("first",
      "second",
      "third")

# You can easily *concatenate* multiple strings to create a new string
# using the addition ``+`` operator, as shown in the following
# example, ::

#: concatenating strings with + operator
print("you can" + " add strings " + "using the + operator")

# All the examples above show the use of double quotes to define
# strings. However, you can also define strings using *single quotes*.
# The following example defines similar strings as above but using
# single quotes, ::

#: a string literal defined with single quotes
'a string defined with single quotes'

#: print a string
print('a string defined with single quotes')

#: print two strings
print('first', 'second')

#: print three strings,
#: you can span multiple lines
print('first',
      'second',
      'third')

#: concatenating strings with + operator
print('you can' + ' add strings ' + 'using the + operator')

# In *both* double and single quoted strings the backslash character
# ``\`` is interpreted as the *escape character*. For example, the
# escape sequences for the tab and new line characters, ``\t`` and
# ``\n`` respectively, work in the same way in double and single
# quoted strings, ::

#: new line '\n' character in double quoted string
print("line1\nline2")

#: tab character '\t' in double quoted string
print("\ta tab character")

#: new line character '\n' in single quoted string
print('line1\nline2')

#: tab character '\t' in single quoted string
print('\ta tab character')

# You can use the backslash character ``\`` to escape double quotes
# within a double quoted string and single quotes within a single
# quoted string, ::

#: escape double quotes in double quoted string
print("\"using double quotes in double quoted string\"")

#: escape single quotes in single quoted string
print('\'using single quotes in single quoted string\'')


