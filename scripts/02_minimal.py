# Minimal Python
# ==============

# | `Preamble`_
# | `Defining and printing strings`_
# | `Variables and assignment`_
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
# code. We will make use of this knowledge in the following sections
# in examples designed to introduce other language features.

# References
# ----------

# + `Language Reference`_
# + `Standard Library`_
# + `Python Tutorial`_

# .. _Language Reference: https://docs.python.org/3.7/reference/index.html
# .. _Standard Library: https://docs.python.org/3.7/library/index.html
# .. _Python Tutorial: https://docs.python.org/3.7/tutorial/index.html
