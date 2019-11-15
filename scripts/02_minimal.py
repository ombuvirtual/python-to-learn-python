# Minimal Python
# ==============

# | `Preamble`_
# | `Defining and printing strings`_
# | `Variables and assignment`_
# | `Introduction to numeric types`_
# | `Logical values and operations`_
# | `References`_

# Preamble
# --------

# This script introduces *minimal Python*. Minimal Python is the
# minimum of Python language syntax, data types, operators and
# language statements required to understand the explanations and
# examples presented in the scripts that make up *Python to learn
# Python* (PTLP). It is a very small subset of Python introduced at a
# very basic level and narrow scope, sufficient only to get started
# with a more detailed presentation.

# Minimal Python includes the following language elements:

# + Essential syntax:

#   - Python statements end with a new line character, *not* a
#     semicolon ``;``.

#   - Python statements are grouped using indentation, *not* opening
#     and closing braces ``{}``.

#   - Comments start with the ``#`` character, like Linux shell
#     comments.

# + Four data types and some related operations:

#   - *Strings* and the concatenation of strings using the addition
#     ``+`` operator.

#   - *Integers* and the usual arithmetic operations of addition
#     ``+``, subtraction ``-``, multiplication ``*``, division ``/``
#     and exponentiation ``**``.

#   - *Booleans* and the logical operations of conjunction (``and``),
#     disjunction (``or``) and negation (``not``).

#   - *Lists* and the ``append()`` method to add elements to lists,
#     list membership operators ``in`` and ``not in`` and list
#     concatenation using the addition ``+`` operator.

#   - The comparison operators of equality ``==`` and inequality
#     ``<``, ``<=``, ``>`` and ``>=``.

# + Two built-in functions:

#   - ``print()`` to print strings to standard output.

#   - ``len()`` to determine the length of a string or number of
#     elements in a list.

# + Six language statements:

#   - The assignment ``=`` statement and variable name *binding*.

#   - The ``pass`` statement for *no operation*.

#   - The ``if`` statement for conditional execution of groups of
#     statements.

#   - The ``for`` statement for repeated execution of groups of
#     statements.

#   - The ``try`` statement for error handling. In PTLP the ``try``
#     statement is used to demonstrate causes of run time errors.

#   - The ``assert`` statement for confirming the outcome of
#     computations during debugging. In PTLP the ``assert`` statement
#     is used to confirm the results of examples.

# These topics will, of course, be covered in more detail in later
# scripts.

# Defining and printing strings
# -----------------------------

# One of the first things you want to know when starting to learn a
# new programming language is how to write comments. In fact PTLP
# scripts are mostly comments explaining different features of the
# Python language.

# The benefits of adequately documenting source code with good
# comments are well known.  There are also substantial benefits in
# writing good comments as part of the process of learning a new
# language. Comments allow you to make notes on the code examples you
# are working on and the language features you are exploring. Sample
# code with good comments relevant to your experience, for example
# comparing features of the new language with those of languages you
# already know, can become a valuable resource that saves you time
# when you start writing actual programs.

# In Python comments start with a ``#`` character. Everything on a
# line from the first ``#`` character to the end of the line is
# ignored by the interpreter. There are no multi-line comment
# delimiters like ``/*`` and ``*/`` in C and other languages. Each
# line of a multi-line comment must start with a ``#`` character. The
# following are examples of comments, ::

#: everything after the first # character is a comment

#: any # characters after the first are part of the comment

#: this is line 1 of a multi-line comment
#: this is line 2 of a multi-line comment

# Another feature of a programming language you need to know from the
# outset is how to define strings and how to print them to standard
# output. This allows you to display messages for immediate feedback
# when trying out new language constructs.

# In the Python language data entities are represented as *objects* of
# specific *types*. For instance, a string is represented as an object
# of type ``str``. To tell the interpreter to create a string object
# you enclose the relevant text in double quotes. For example, if you
# want to define a string with the text ``a string defined with double
# quotes`` you enclose the text in double quotes and the Python
# interpreter will recognise it as a *string literal expression* and
# create an object of type ``str``. The following is an example of a
# string literal expression defined with double quotes, ::

#: a string literal defined with double quotes,
"a string defined with double quotes"

# Note carefully the second line of code above. It does not end with
# an explicit statement termination character such as a semicolon. In
# the Python language statements can be terminated by simply entering
# a *new line* character. You can if you want end a statement with a
# semicolon but it is not required and is normally left out.

# However, you do need to use a semicolon to separate statements if
# you want to write them on the same line. For example, you can write
# the string expressions ``"foo"`` and ``"bar"`` in one line of code,

# ::

"foo"; "bar"

# The last expression "bar" does not need to end in a semicolon
# because the interpreter recognises the new line character as the
# end of the expression.

# The statements above don't have any useful side effects such as
# assigning the string to a variable or printing the string to
# standard output. When the interpreter encounters the expression
# "foo", for example, it creates an object of type ``str`` that
# represents the string "foo" and then moves on and the object is
# eventually discarded. We'll introduce variable assignment in the
# next section. In this section we deal with printing strings.

# To print a string to standard output you use Python's built-in
# function ``print()``. The ``print()`` function takes a *variable*
# number of string arguments separated by comas. It automatically
# separates multiple arguments with a space and adds a new line
# character at the end.  The following example shows invocations of
# ``print()`` with different number of arguments. Note again that the
# statements end with a new line character and not a semicolon, ::

#: print a string
print("a string defined with double quotes")

#: print two strings
print("foo", "bar")

#: print three strings,
print("foo", "bar", "gnu")

# You can tell the ``print()`` function to separate printed arguments
# with a string other than a single space. Use the keyword parameter
# ``sep=`` to specify what string to print between arguments. The
# following code prints the strings "foo", "bar" and "gnu" using
# different separators, ::

#: don't separate printed arguments
#: so they are printed contiguously
print("foo", "bar", "gnu", sep="")

#: separate printed arguments with a dash
print("foo", "bar", "gnu", sep="-")

#: separate printed arguments with a coma and space
print("foo", "bar", "gnu", sep=", ")

# You can also tell ``print()`` to end the printed line with a string
# other than a single new line character. Use the keyword parameter
# ``end=`` to specify what string to print at the end of a line. The
# following code shows two examples of ending with a string that
# doesn't contain a new line character, ::

#: don't end printed line with a new line
#: so next call to print() will print
#: on the same line in stdout
print("foo", end="")
print("bar")

#: end printed line with dash
print("foo", end="-")
print("bar")

#: end printed line with coma and new line
print("foo", end=",\n")
print("bar")

# Now that we know how to print strings we can easily test the result
# of concatenating two or more strings using the addition ``+``
# operator. The following code concatenates three strings and prints
# the resulting string object, ::

#: concatenate strings with + operator
print("you can" + " add strings " + "using the + operator")

# All the examples above use double quotes to define strings. However,
# you can also define strings using *single quotes*.  The following
# example defines similar strings as above but using single quotes, ::

#: a string literal defined with single quotes
'a string defined with single quotes'

#: print a string
print('a string defined with single quotes')

#: print two strings
print('foo', 'bar')

#: print three strings,
print('foo', 'bar', 'gnu')

#: concatenate strings with + operator
print('you can' + ' add strings ' + 'using the + operator')

# Whether a string is defined using double or single quotes the
# backslash character ``\`` is always interpreted as the *escape
# character* and can be used to insert non-printable characters such
# as tabs and new lines. For example, you can use the escape sequences
# ``\t`` and ``\n`` to insert tab and new line characters in both
# double *and* single quoted strings, ::

#: new line '\n' character in double quoted string
print("line1\nline2")

#: tab character '\t' in double quoted string
print("\ta tab character")

#: new line character '\n' in single quoted string
print('line1\nline2')

#: tab character '\t' in single quoted string
print('\ta tab character')

# You can also use the backslash character ``\`` to escape double quotes
# within a double quoted string and single quotes within a single
# quoted string, as shown in the following example, ::

#: escape double quotes in double quoted string
print("\"using double quotes in double quoted string\"")

#: escape single quotes in single quoted string
print('\'using single quotes in single quoted string\'')

# This section introduced Python's string data type (at a very basic
# level) and showed how to print string objects using the built-in
# function ``print()``. The next section shows how to *name* objects
# so we can refer to them easily by their names in other parts of the
# code.

# Variables and assignment
# ------------------------

# Suppose you have defined the string ``"foo"`` at some point in your
# program and you want to use the same string in other expressions and
# statements by referring to it using the name ``x``.  You can
# associate the name ``x`` with the string object ``"foo"`` by making
# ``x`` the *target* of an *assignment statement*, as shown in the
# following sample code, ::

#: this assignment statement associates
#: the name 'x' with string object "foo"
x = "foo"

# The statement consists of two operands on either side of the
# assignment symbol ``=``. On the left is the name ``x`` that you want
# to associate with the object ``"foo"`` specified on the right. Note
# also that, like all statements in Python, the assignment statement
# does not require an ending semicolon.

# Once the association between ``x`` and ``"foo"`` has been made, you
# can refer to the string ``"foo"`` by its name. The following calls
# to ``print()`` and concatenation operation refer to ``"foo"`` by its
# name ``x``, ::

#: print string "foo"
print("x =", x)

#: concatenate string "foo" with
#: string "bar" and print result
print(x + "bar")

# The names you associate with objects cannot be formed from just any
# character. A valid name or identifier is formed from characters in
# the following classes,

# + lower case (a-z) or upper case (A-Z) letters
# + the underscore character '_'
# + digits 0-9 (except for the first character)

# The following are examples of valid names: ``bar``, ``BAR``,
# ``bar_1`` and ``_bar``. The name ``1_bar`` is *invalid* because it
# starts with a digit.

# In the Python documentation the process of associating a name with
# an object is referred to as *binding*. In the example above we would
# say that the name ``x`` has been *bound* to string object
# ``"foo"``. The assignment statement is just one of several *binding*
# operations in the Python language.

# It is important to realize that in Python there is no such thing as
# declaring a variable. A variable only comes into existence as the
# result of binding a name to an object. In other words, variables are
# the result of binding operations.

# It is possible to reuse names or more precisely to *rebind* a name
# to a different object. For example, suppose you bind ``x`` to the
# string ``"foo"``. You can at a later point in your code rebind ``x``
# to the string ``"bar"`` as shown in the following code, ::

#: bind x to string "foo"
x = "foo"

#: refer to string "foo" using x
print("x =", x)

#: rebind x to string "bar"
x = "bar"

#: refer to string "bar" using x
print("x =", x)

# We now know how to define strings, print them and bind them to
# suitable identifiers so we can conveniently refer to them in our
# code. We will make use of this knowledge in examples designed to
# introduce other language features.

# Introduction to numeric types
# -----------------------------

# Python has data types to represent integers, floating point numbers
# and even complex numbers. This section provides a very brief
# introduction to Python's integer and floating point data types.

# Integers are represented by objects of type ``int``.  To define a
# base 10 positive integer you just write the digits that make up the
# number. For example, to define the number *thirteen* you simply
# write the digits ``13``. When the interpreter encounters the integer
# literal expression ``13`` it creates an object of type ``int`` that
# represents that number. The following are examples of positive
# integer literal expressions, ::

#: positive integer literal expressions
0; 1; 2; 3; 99

# You define negative integers by applying the unary *minus* ``-``
# operator to the positive integer literal expression. For instance,
# negative thirteen is written as ``-13`` or ``- 13``. The following
# are examples of negative integer literal expressions, ::

#: negative integer literal expressions
-99; -3; - 2; - 1

# Floating point numbers are represented by objects of type
# ``float``. To define a positive floating point number you just write
# the digits that make up the number, including the decimal point. For
# example, to define the floating point number *pi* to two decimal
# places you simply write ``3.14``. When the interpreter encounters
# the floating point literal expression ``3.14`` it creates an object
# of type ``float`` that represents that number. The following code
# snippet shows examples of positive float literal expressions, ::

#: positive float literal expressions
0.0; 0.01; 0.5; 2.718

# You define negative floating point numbers by applying the unary
# *minus* ``-`` operator to the positive float literal expression. For
# instance, negative *pi* is written as ``-3.14`` or ``- 3.14``. The
# following are examples of negative float literal expressions, ::

#: negative float literal expressions
-2.718; -0.5, - 0.01

# To print an integer or floating point number you use the ``print()``
# function. It automatically converts objects of type ``int`` and
# ``float`` to strings and then prints the strings. The following are
# examples of printing integer and float literal expressions, ::

#: print integers
print(0, 1, 2, 3, 99)
print(-99, -3, - 2, - 1)

#: print floating point numbers
print(0.0, 0.01, 0.5, 2.718)
print(-2.718, -0.5, - 0.01)

# You can bind names to numeric values using the assignment statement
# in the same way you bind names to string values. For example, to
# bind the name ``x`` to integer ``1`` you write ``x = 1`` and to
# rebind ``x`` to the floating point number ``3.14`` you write ``x =
# 3.14``. The following sample code shows other examples, ::

#: bind x to 0 and y to 99
x = 0; y = 99
print(x, y)

#: rebind x to 0.0 and y to 99.0
x = 0.0; y = 99.0
print(x, y)

# Python supports the usual arithmetic operations of addition ``+``,
# subtraction ``-``, multiplication ``*``, division ``/`` and
# exponentiation ``**``. It uses the familiar syntax and symbols for
# arithmetic operators used in many other languages.

# All the above arithmetic operations will produce a result of type
# ``float`` if *at least one* operand is of type float. Division
# *always* produces a result of type float even if all operands are
# integers and an integer result is expected.  The following sample
# code shows examples of arithmetic operations and the results they
# produce, ::

#: all operands are integers
#: the result is integer
print(1 + 2)
print(3 - 1)
print(3 * 2)
print(3 ** 2)

#: one operand is float
#: the result is float
print(1 + 2.0)
print(3 - 1.0)
print(3 * 2.0)
print(3 ** 2.0)

#: division always produces
#: a float result
print(2 / 1)
print(2 / 1.0)
print(3 / 2)
print(4 / 2)

# You can use parentheses to group expressions when there are many
# terms involved or to specify clearly the grouping of operands and
# operators so you don't have to rely on knowledge of operator
# precedence rules. Take for instance the following compound
# expression, ::

#: define some initial values
x = 2; y = 3; z = 4

#: interpreting this compound expression
#: relies on knowledge of precedence rules
r = 10 * x ** 2 * y + z / 2 - 1

#: print result
print(r)

# It is equivalent to the following expression which uses parentheses, ::

#: using parentheses makes computational
#: intent more clear
r = 10 * (x ** 2) * y + (z / 2) -1

#: print result
print(r)

# The two expressions above produce the same result but the second
# form shows much more clearly our intent.

# We now know how to create objects of type ``str``, ``int`` and
# ``float`` using literal expressions and we can bind names to these
# objects and perform some elementary operations on them. In the next
# section we show how to define Boolean values, how to print them,
# assign names to them and perform some elementary logical operations
# on them.

# Logical values and operations
# -----------------------------

# Logical values and operations allow us to formulate truth conditions
# and test the results to perform alternative computations.

# The logical truth values of *true* and *false* are represented in
# Python by objects of type ``bool``. To define the logical value
# *true* you write ``True`` and to define the logical value *false*
# you write ``False``. When the interpreter encounters either of these
# Boolean expressions it creates an object of type ``bool`` to
# represent the corresponding logical value. This means that objects
# of type ``bool`` can have only two possible values, ``True`` or
# ``False``. The following Boolean expressions create objects with the
# two possible truth values, ::

#: create an object of type 'bool'
#: with the value True
True

#: create an object of type 'bool'
#: with the value False
False

# You can print the values ``True`` and ``False`` using the
# ``print()`` function. It automatically converts the Boolean values
# to the strings ``"True"`` and ``"False"``, ::

#: print Boolean values
print(True, False)

# You can bind Boolean values to a name using the assignment
# statement. In the following code the names ``x`` and ``y`` are bound
# to the values ``True`` and ``False`` respectively and then rebound
# to ``False`` and ``True``, ::

#: bind x to True and y to False
x = True; y = False
print(x, y)

#: rebind x to False and y to True
x = False; y = True
print(x, y)

# Python supports the usual logical operations of *conjunction*,
# *disjunction* and *negation*. Conjunction or logical *and* is
# implemented using the ``and`` operator. The following sample code
# prints the truth table for the ``and`` operation, ::

#: truth table for 'and' operation
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Disjunction or logical *or* is implemented using the ``or``
# operator. The following sample code prints the truth table for the
# ``or`` operation, ::

#: truth table for 'or' operation
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Negation is implemented using the ``not`` operator. The following
# sample code prints the truth table for the ``not`` operation, ::

#: truth table for 'not' operation
print(not True)
print(not False)

# References
# ----------

# + `Language Reference`_
# + `Standard Library`_
# + `Python Tutorial`_

# .. _Language Reference: https://docs.python.org/3.7/reference/index.html
# .. _Standard Library: https://docs.python.org/3.7/library/index.html
# .. _Python Tutorial: https://docs.python.org/3.7/tutorial/index.html
