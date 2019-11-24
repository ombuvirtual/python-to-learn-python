# Minimal Python
# ==============

# | `Preamble`_
# | `Defining and printing strings`_
# | `Variables and assignment`_
# | `Introduction to numeric types`_
# | `Logical values and operations`_
# | `Introduction to lists`_
# | `Comparison operations`_
# | `The for statement`_
# | `The if statement`_
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

from ptlp import pl # import pl() function to print line numbers

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
# string literal expression defined with double quotes,

# ::

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
# statements end with a new line character and not a semicolon,

# ::

pl()

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
# different separators,

# ::

pl()

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
# doesn't contain a new line character,

# ::

pl()

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
# the resulting string object,

# ::

pl()

#: concatenate strings with + operator
print("you can" + " add strings " + "using the + operator")

# A common requirement when dealing with a string is to determine how
# many characters it contains. The built-in function ``len()`` takes a
# *collection* object as an argument and returns the number of items
# in the collection.  A collection is an object that supports the
# concept of *number of items*, also known as its *length*. In this
# script we introduce two such collections, strings discussed in this
# section and lists discussed in a later section.

# Suppose you have the string object ``"abc"``, then the function call
# ``len("abc")`` returns 3, the number of characters in the
# string. The following are some examples of using the ``len()``
# function,

# ::

pl()

#: length of null string
print(len(""))

#: length of a string
print(len("0123456789"))

# In all the examples above we used double quotes to define strings,
# however, you can also use *single quotes*. For example, the string
# literal expression 'abc' produces the same result as
# "abc". Everything we've said so far about double quoted strings
# applies equally to single quoted strings. In the following examples
# single quotes are used to demonstrate the properties we discussed
# above for double quoted strings,

# ::

pl()

#: define null string
print('')

#: define a string
print('foo')

#: print two strings
print('foo', 'bar')

#: concatenate strings
print('foo' + 'bar' + 'gnu')

#: length of a string
print(len('foobargnu'))

# Whether a string is defined using double or single quotes the
# backslash character ``\`` is always interpreted as the *escape
# character* and can be used to insert non-printable characters such
# as tabs and new lines. For example, you can use the escape sequences
# ``\t`` and ``\n`` to insert tab and new line characters in both
# double *and* single quoted strings,

# ::

pl()

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
# quoted string, as shown in the following example,

# ::

pl()

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
# following sample code,

# ::

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
# name ``x``,

# ::

pl()

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
# to the string ``"bar"`` as shown in the following code,

# ::

pl()

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
# integer literal expressions,

# ::

#: positive integer literal expressions
0; 1; 2; 3; 99

# You define negative integers by applying the unary *minus* ``-``
# operator to the positive integer literal expression. For instance,
# negative thirteen is written as ``-13`` or ``- 13``. The following
# are examples of negative integer literal expressions,

# ::

#: negative integer literal expressions
-99; -3; - 2; - 1

# Floating point numbers are represented by objects of type
# ``float``. To define a positive floating point number you just write
# the digits that make up the number, including the decimal point. For
# example, to define the floating point number *pi* to two decimal
# places you simply write ``3.14``. When the interpreter encounters
# the floating point literal expression ``3.14`` it creates an object
# of type ``float`` that represents that number. The following code
# snippet shows examples of positive float literal expressions,

# ::

#: positive float literal expressions
0.0; 0.01; 0.5; 2.718

# You define negative floating point numbers by applying the unary
# *minus* ``-`` operator to the positive float literal expression. For
# instance, negative *pi* is written as ``-3.14`` or ``- 3.14``. The
# following are examples of negative float literal expressions,

# ::

#: negative float literal expressions
-2.718; -0.5, - 0.01

# To print an integer or floating point number you use the ``print()``
# function. It automatically converts objects of type ``int`` and
# ``float`` to strings and then prints the strings. The following are
# examples of printing integer and float literal expressions,

# ::

pl()

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
# 3.14``. The following sample code shows other examples,

# ::

pl()

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
# produce,

# ::

pl()

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
# expression,

# ::

pl()

#: define some initial values
x = 2; y = 3; z = 4

#: interpreting this compound expression
#: relies on knowledge of precedence rules
r = 10 * x ** 2 * y + z / 2 - 1

#: print result
print(r)

# It is equivalent to the following expression which uses parentheses,

# ::

pl()

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
# two possible truth values,

# ::

#: create an object of type 'bool'
#: with the value True
True

#: create an object of type 'bool'
#: with the value False
False

# You can print the values ``True`` and ``False`` using the
# ``print()`` function. It automatically converts the Boolean values
# to the strings ``"True"`` and ``"False"``,

# ::

pl()

#: print Boolean values
print(True, False)

# You can bind Boolean values to a name using the assignment
# statement. In the following code the names ``x`` and ``y`` are bound
# to the values ``True`` and ``False`` respectively and then rebound
# to ``False`` and ``True``,

# ::

pl()

#: bind x to True and y to False
x = True; y = False
print(x, y)

#: rebind x to False and y to True
x = False; y = True
print(x, y)

# Python supports the usual logical operations of *conjunction*,
# *disjunction* and *negation*. Conjunction or logical *and* is
# implemented using the ``and`` operator. The following sample code
# prints the truth table for the ``and`` operation,

# ::

pl()

#: truth table for 'and' operation
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Disjunction or logical *or* is implemented using the ``or``
# operator. The following sample code prints the truth table for the
# ``or`` operation,

# ::

pl()

#: truth table for 'or' operation
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Negation is implemented using the ``not`` operator. The following
# sample code prints the truth table for the ``not`` operation,

# ::

pl()

#: truth table for 'not' operation
print(not True)
print(not False)

# Introduction to lists
# ---------------------

# The *list* data type allows you to define and dynamically build an
# *ordered* collection of arbitrary elements that can then be
# processed in some way by iterating over the collection.

# In the Python language lists are represented by objects of type
# ``list``. To explicitly define a list you enclose its elements in
# square brackets and separate them by comas. For example, to define a
# list containing the ordered sequence of strings ``"a"``, ``"b"`` and
# ``"c"`` you write ``["a", "b", "c"]``. When the interpreter
# encounters this literal list expression it creates an object of type
# ``list`` that represents the ordered sequence of strings ``"a"``,
# ``"b"`` and ``"c"``.

# The following examples show definitions of *homogeneous* lists, that
# is, lists in which all elements are of the same type,

# ::

#: define an empty list
[]

#: define a list with one string element
["a"]

#: define a list of strings
["a", "b", "c"]

#: define a list of integers
[1, 2, 3]

#: define a list of lists
[[], [1], [1, 2]]

# The following examples show definitions of *heterogeneous* lists,
# that is, lists that contain elements of different types,

# ::

#: a list of integers, floats and strings
[1, "1", 2.0, "2.0", 3, "3"]

#: a list of integers, strings and lists
[0, '', [], 1, '1', [1]]

# To print a list object you use the ``print()`` function. It
# automatically converts a list object to a string, as shown in the
# following example,

# ::

pl()

#: print the empty list
print([])

#: print a list of strings
print(["a", "b", "c"])

#: print a list of integers
print([1, 2, 3])

#: print a list of lists
print([[], [1], [1, 2]])

#: print a heterogeneous list
print([1, 3.14, "foo", ["bar"]])

# You can bind names to list objects using the assignment statement in
# the same way you do for strings, integers, floats and Boolean
# values. For example, to bind the name ``x`` to list ``[1, 2, 3]``
# you write ``x = [1, 2, 3]`` and to rebind ``x`` to list ``["a", "b",
# "c"]`` you write ``x = ["a", "b", "c"]``. The following sample code
# shows other examples,

# ::

pl()

#: bind x to the empty list
x = []
print(x)

#: rebind x to a list of floats
x = [0.01, 0.1, 1.0]
print(x)

#: rebind x to a list of lists
x = [[], [1], [1, 2]]
print(x)

# To determine the number of elements in a list you use the built-in
# function ``len()`` which we introduced in the section on
# strings. Suppose ``x`` is bound to list object ``[1, 2, 3]``, then
# the function call ``len(x)`` returns 3, the number of elements in
# ``x``. The following are some examples of using the ``len()``
# function,

# ::

pl()

#: length of empty list
print(len([]))

#: length of a list of strings
x = ["a", "b", "c"]
print(len(x))

#: length of a list of lists
x = [[], [1], [1, 2]]
print(x)

#: length of first element of a list of lists
x = [["a", "b"], ["c"]]
print(len(x[0]))

# The index of the last element of a non-empty list is given by
# ``len(x) - 1``. You can use this fact to reference the last element
# of a list as in the following example,

# ::

pl()

#: a list x
x = [1, 2, 3]

#: print last element of x
print(x[len(x) - 1])

# Let's now consider three operations you can perform on list objects,
# concatenation, referencing its elements and adding elements to
# it. You can create a new list by concatenating two or more existing
# lists using the addition operator ``+``. For example, if you want to
# create a new list that contains all the elements in list ``[1, 2,
# 3]`` followed by all the elements in list ``[4, 5, 6]``, you write
# ``[1, 2, 3] + [4, 5, 6]``. The following code shows some examples of
# list concatenation,

# ::

pl()

#: concatenate multiple lists
x = [1] + [2, 3] + [4, 5] + [6]
print(x)

#: bind x and y to list objects
x = ["a", "b", "c"]
y = ["d", "e", "f"]

#: concatenate lists x and y
z = x + y
print(z)

#: concatenating a list with the empty list
#: creates a new list with the same elements
x = [1, 2] + []
print(x)

# The elements of a list are indexed by integer values, starting at
# index 0. Consider, for example, the list ["a", "b", "c"], the index
# of element "a" is 0, the index of "b" is 1 and the index of "c" is
# 2. To reference an element in a list you use the *index*
# operator. The index operator applied to a list named ``x`` has the
# form ``x[i]``, where ``i`` is the index of the element you want to
# reference. For example, if the list above was bound to the name
# ``x``, element ``"a"`` would be referenced by ``x[0]``, element
# ``"b"`` by ``x[1]`` and ``"c"`` by ``x[2]``. The following code
# snippet shows some examples of referencing list elements,

# ::

pl()

#: a list x
x = ["foo", "bar", "gnu"]

#: reference first element of x
print(x[0])

#: reference second element of x
print(x[1])

#: reference third element of x
print(x[2])

#: you can apply the index operator to a
#: literal list although it's not very useful,
#: the following references the second
#: element of a literal list
print([1, 2, 3][1])

# To add an element to the end of a list you can use the ``append()``
# method. The ``append()`` method takes as an argument the object you
# want to add to the list. Suppose ``x`` is bound to the empty list
# ``[]``, to add the element ``"foo"`` to it you write
# ``x.append("foo")``. To add another element to the end of list
# ``x``, say the string ``"bar"``, you write ``x.append("bar")``. The
# following code provides more examples,

# ::

pl()

#: start with an empty list x
x = []

#: add strings "a", "b" and "c"
x.append("a")
x.append("b")
x.append("c")

#: add a string bound to y
y = "foo"
x.append(y)

#: print list x
print(x)

# We have now introduced all the data types in minimal Python,
# ``str``, ``int``, ``float``, ``bool`` and ``list``. We have seen how
# to define objects of these types using literal expressions, how to
# bind names to them with the assignment statement and introduced some
# basic operations you can perform on these types of objects.

# Comparison operations
# ---------------------

# This section is an introduction to the comparison operations of
# equality, identity and inequality as they apply to objects of type
# ``int``, ``float``, ``bool``, ``str`` and ``list``.

# These operations are implemented using the following operators:

# + equality ``==`` and non-equality ``!=``
# + identity ``is`` and non-identity ``is not``
# + strict inequality *less than* ``<`` and *greater than* ``>``
# + non-strict inequality *less than or equal* ``<=`` and *greater
#   than or equal* ``>=``

# These are *binary* operators that operate on two operands. The
# expressions that can be constructed using these operators always
# evaluate to a Boolean value of ``True`` or ``False``.

# I describe first the equality and identity operators.  The equality
# operator ``==`` tests whether its two operands *represent* the same
# *value*. The identity ``is`` operator, on the other hand, tests
# whether the two operands *are* the same *object*. It is very
# important to understand this difference from the outset.

# Suppose you have an object of type ``int`` that represents the
# integer value ``1`` and an object of type ``float`` that represents
# the float value ``1.0``.  These are two different objects that
# represent the same mathematical number 1. Therefore, the equality
# expression ``1 == 1.0`` evaluates to ``True``, since the two objects
# represent the same value.  On the other hand, the identity
# expression ``1 is 1.0`` evaluates to ``False``, since the two
# objects involved are different. The following code confirms this
# result,

# ::

pl()

#: equality evaluates to True,
#: 1 and 1.0 represent the same value
print(1 == 1.0)

#: identity evaluates to False,
#: 1 and 1.0 are different objects
print(1 is 1.0)

# An example based on lists may serve to clarify the difference
# between equality and identity. Whenever the Python interpreter
# encounters the expression ``[]`` it creates a new object of type
# ``list`` that represents the value *empty list*. The equality
# expression ``[] == []`` evaluates to ``True`` because the two
# operands are objects representing the same value *empty list*. On
# the other hand, the identity expression ``[] is []`` evaluates to
# ``False`` because the two operands are different objects. This is
# confirmed in the following code,

# ::

pl()

#: equality evaluates to True,
#: both operands represent the 'empty list'
print([] == [])

#: identity evaluates to False,
#: each list expression produces a different object
print([] is [])

# The same argument applies to non-empty lists, as show in the
# following code,

# ::

pl()

#: equality evaluates to True,
#: the values represented are equal
print(["a", "b", "c"] == ["a", "b", "c"])

#: identity evaluates to False,
#: each list expression produces a different object
print(["a", "b", "c"] is ["a", "b", "c"])

# The examples above showed the difference between equality and
# identity. We now turn our attention to equality expressions that
# involve operands of *different* types.

# In this case equality fails when the types of the operands are such
# that they can't represent the same value. For instance, the
# expression ``1 == "1"`` evaluates to ``False`` because the integer 1
# is not equal to the string "1".  All the following expressions
# evaluate to ``False`` because the types involved can't be used to
# represent the same value,

# ::

pl()

#: int and str
print(1 == "1")

#: int and list
print(1 == [1])

#: float and str
print(1.0 == "1.0")

#: float and list
print(1.0 == [1.0])

#: str and list
print("a" == ["a"])

#: bool and str
print(True == "1")
print(False == "0")

# The above argument does not apply to equality expressions in which
# the two operands are combinations of objects of type ``int``,
# ``float`` or ``bool``. Objects of type ``int`` and ``float`` can be
# used to represent the same numeric value and in such cases the
# objects are considered equal, as they should.  For instance, the
# number 1 can be equally represented by the ``int`` object ``1`` or
# the float object ``1.0``. The equality expression ``1 == 1.0``
# evaluates to ``True`` because the two objects represent the same
# value. The following are examples in which ``int`` and ``float``
# objects are equal,

# ::

pl()

#: equality evaluates to True,
#: int and float objects both represent 0
print(0 == 0.0)

#: equality evaluates to True,
#: int and float objects both represent 2
print(2 == 4 / 2)

# The Boolean values ``True`` and ``False`` are considered equal to
# the numeric values 1 and 0 respectively. Therefore, the following
# equality expressions evaluate to True,

# ::

pl()

#: equality evaluates to True,
#: True and 1 are considered the same value
print(True == 1)
print(True == 1.0)

#: equality evaluates to True,
#: False and 0 are considered the same value
print(False == 0)
print(False == 0.0)

# The examples above considered equality of objects of different
# types. Let's now consider equality of objects of the *same* type.

# Equality of ``int`` and ``float`` objects follow the rules of
# equality of arithmetic. The following equality expressions with
# ``int`` and ``float`` operands evaluate to ``True``,

# ::

pl()

#: both operands are int
print(1 == 2 - 1)

#: both operands are float
print(1.5 == 3 / 2)

#: one int and one float operand
print(2 == 4 / 2)

# Equality of objects of type ``bool`` is trivial. Two ``bool``
# objects are equal if they both represent the value ``True`` or
# ``False``.

# Equality of strings is also straightforward. Two objects of type
# ``str`` are equal if the string values they represent have the same
# number of characters and their corresponding characters are
# equal. The following equality expressions with ``str`` operands
# evaluate to ``True``,

# ::

pl()

#: string equality expressions that evaluate to True
print("" == '')
print("foo" == "foo")
print("foo" == "f" + "o" + "o")
print('_*_' == '_' + '*' + '_')

# Finally, let's consider equality of lists. For two objects of type
# ``list`` to compare equal, they must be of equal length and their
# corresponding elements must compare equal. The following are
# examples of list equality expressions,

# ::

pl()

#: expressions that evaluate to True
print([1] == [1])
print([1] == [1] + [])
print([1] == [1.0])
print(["ab"] == ["a" + "b"])

#: expressions that evaluate to False
print([1] == [2])
print([1] == [1] + [2])
print([1] == ["1"])
print(["a"] == ["a", "b"])

# An understanding of non-equality and non-identity operators, ``!=``
# and ``is not``, follows trivially from an understanding of equality
# and identity so there is no need to cover them explicitly here.

# Let's now turn our attention to inequality comparison operations. I
# will restrict the discussion to the strict inequality *less than*
# ``<`` operator.  There is no loss of generality because
# understanding the operation of the other inequality operators
# follows easily from knowledge of equality and *less than*
# inequality.

# The first thing to note is that applying inequality operators to
# operands of different types causes a ``TypeError`` run time error.
# For example, when the interpreter encounters the expression ``1 <
# [1]`` it generates the following error,

# ::

#  Traceback (most recent call last):
#    File "myscript.py", line 10, in <module>
#      1 < [1]
#  TypeError: '<' not supported between instances of 'int' and 'list'

# The fourth line indicates the class of error, ``TypeError``,
# followed by a very precise explanatory message.

# Inequality of numeric types ``int`` and ``float`` follows the
# familiar rules of arithmetic. In this case the two numeric operands
# don't have to be of the same type. For example, the expression ``1 <
# 2.0`` involving an ``int`` and ``float`` evaluates to ``True``, as
# expected from our understanding of numeric ordering in
# arithmetic. The following are some examples of numeric inequalities,

# ::

pl()

#: some numeric inequalities
#: that evaluate to True
print(1 < 3.14)
print(0 < 1.0)
print(-1 < 0.0)
print(-2.0 < -1)

# Inequality of strings is based on lexicographic ordering. The
# following are examples of inequality expressions with string
# operands,

# ::

pl()

#: some string inequalities
#: that evaluate to True
print("" < "a")
print("a" < "b")
print("a" < "aa")
print("0a" < "a")
print("_a" < "a")
print("" < "abc")
print("abc" < "c")

# The comparison of lists is more involved than comparison of strings
# because the elements of a list can be arbitrary objects.

# Consider first the case of comparing two lists that contain elements
# of different types. The process of comparing two lists involves
# comparing their corresponding elements until the comparison
# evaluates to True or False. If the comparison of two lists involves
# comparing elements of different types the interpreter will generate
# a run time error . For example, the expression ``[1] < ["a"]``
# generates the following error,

# ::

#  Traceback (most recent call last):
#    File "myscript.py", line 10, in <module>
#      print([1] < ["a"])
#  TypeError: '<' not supported between instances of 'int' and 'str'

# In some cases the comparison expression is resolved before elements
# of different type are compared and no run time error is generated,
# as shown in the following example,

# ::

pl()

#: evaluates to True
print([1] < [2, "a"])

# For the rest of the discussion let's assume the lists involved have
# elements that are comparable. Furthermore, let's consider first the
# case of lists that contain the same number of elements.

# Suppose you have two lists x and y and the inequality expression x <
# y.  To evaluate the expression the inequality operator ``<`` is
# applied to each pair of corresponding elements of x and y, one pair
# at a time from left to right.  If inequality of a given pair is
# ``True``, then list inequality is ``True`` and comparison stops; if
# inequality of the given pair is ``False``, then list inequality is
# ``False`` and comparison stops; if the pair of elements are equal
# then the inequality operator is applied to the next pair of
# corresponding elements; and if all elements compare equal list
# inequality is ``False``. The following examples illustrate each
# case,

# ::

pl()

#: evaluates to True
#: because 2 < 3 is True
print([1, 2] < [1, 3])

#: evaluates to False
#: because 1 < 0 is False
print([1, 2] < [0, 3])

#: evaluates to False
#: because lists are equal
print([1, 2] < [1, 2])

# Comparison of lists that contain different number of elements
# operates in the same way as with lists of the same size, with one
# extension. If the elements of the shorter list are equal to the
# corresponding elements of the longer list then the shorter list is
# considered less than the longer list. The following examples
# illustrate these cases,

# ::

pl()

#: evaluates to True
#: empty list less than non-empty list
print([] < [1])

#: evaluates to True
#: shorter list is less than longer list
print([1, 2] < [1, 2, 3])

#: evaluates to True
#: because 1 < 2 is True
print([1, 2] < [2, 1, 0])

#: evaluates to False
#: because 2 < 1 is False
print([1,2] < [1, 1, 0])

# The for statement
# -----------------

# The ``for`` statement is designed to repeatedly execute a group of
# program statements, a common programming requirement often described
# as *executing a loop*.

# Suppose you have a list x containing strings and you want to print
# each string in a separate line. The following ``for`` statement
# would accomplish that task,

# ::

pl()

#: a list of strings
x = ["foo", "bar", "gnu"]

#: iterates over the elements of list x,
#: at each iteration binds 'item' to next element,
#: then calls print() with 'item' as an argument,
#: repeats until there is no next element
for item in x:
    print(item)

# The ``for`` statement above iterates over the elements of list
# ``x``. At the start of each iteration it gets the *next* element in
# the list and binds it to the identifier ``item``, it then executes
# the call to ``print(item)``.  This process of iteration stops when
# the attempt to get the *next* element returns no element, signalling
# the end of the list. Once the string ``"gnu"``, the last string in
# the list, is printed, the attempt to get the next element signals
# end of list and the ``for`` loop ends.

# Let's focus now on the syntax of the ``for`` statement. The
# statement consists of two parts: The *statement header* and the
# *statement group* that follows the header and is meant to be executed
# repeatedly.

# The statement header begins with the keyword ``for`` and is followed
# by the *loop variable* which can be any valid name, in this example
# the name ``item``. The loop variable is followed by the keyword
# ``in`` which itself must be followed by an *iterable* object, in
# this example the list ``x``. The header ends with a mandatory colon
# ``:`` character.

# In many programming languages a statement group is defined by
# explicitly enclosing the statements in braces ``{}``. In Python a
# statement group is defined by *indenting* each statement in the
# group a consistent amount relative to the statement header. In the
# example above the call to the ``print()`` function is indented four
# spaces relative to the statement header. This indentation is not
# optional, it is syntactically required. Suppose we rewrite the
# example above without indentation as in the following code,

# ::

#  for item in x:
#  print(item)

# When the Python interpreter encounters this statement it generates
# an ``IndentationError`` and displays the following information,

# ::

#    File "myscript.py", line 10
#      print(item)
#          ^
#  IndentationError: expected an indented block

# The size of indentation does not matter but it must be consistent
# throughtout the same program.

# In the example above the statement group associated with the ``for``
# loop contains only one statement, the call to ``print()``.

# Let's see another ``for`` loop example.  Suppose as before you have
# a list of strings and you want to print each string in a separate
# line but this time also print in its own line the concatenation of
# all elements printed up to the current iteration. The following
# ``for`` statement would accomplish the task,

# ::

pl()

#: a list of strings
x = ["foo", "bar", "gnu"]

#: initial concatenation
s = ""

#: prints 'item' and the concatenation
#: of elements printed up to current
#: iteration
for item in x:
    print(item)
    print(s + item)

# The following example uses a string as the iterable object in the
# ``for`` statement.

# ::

pl()

#: a string
s = "abcdef"

#: 'for' loop with a string as
#: the iterable object
for char in s:
    print(char)
    print(char.upper())

# You can also use a literal expression for the iterable object in a
# for loop, as show in the following example,

# ::

pl()

#: you can use a literal expression
#: for the iterable object in 'for' loop
sum = 0
for n in [1, 2, 3]:
    sum = sum + n
    print(n, sum)

# It is possible to nest ``for`` statements. In other words, a ``for``
# loop can be part of the statement group of another ``for`` loop, as
# long as indentation is observed. The following example uses two
# nested for loops.

# ::

pl()

#: two lists of strings
x = ["a", "b"]
y = ["c", "d"]

#: you can nest for loops
for m in x:
    for n in y:
        print(m + n)

# The if statement
# ----------------

# The ``if`` statement is designed to allow the execution of
# alternative groups of program statements based on the result of
# testing the truth value of an expression.

# Suppose you have a list of lower case and upper case letters and you
# want to print only those that are upper case. To accomplish this
# task you can use a ``for`` loop to iterate over the letters in the
# list and use an ``if`` statement to test whether a letter is upper
# case and only execute a statement to print it if the result of the
# test is ``True``. The following code implements this example,

# ::

pl()

#: a list of letters
letters = ["a", "B", "c", "D"]

#: prints upper case letters in list
for letter in letters:
    if letter.isupper():
        # this statement is only executed
        # if letter.isupper() returns True
        print(letter)

# For each iteration of the ``for`` loop the ``if`` statement tests
# whether the expression ``letter.isupper()`` evaluates to ``True`` or
# ``False``. If the expression evaluates to ``True`` the function call
# ``print(letter)`` is executed. If it evaluates to ``False`` the
# ``if`` statement ends and executation continues with the next
# iteration of the ``for`` loop.

# The ``if`` statement consists of two parts, the statement header and
# the group of statements to be *conditionally* executed. The
# statement header begins with the keyword ``if`` and is followed by
# the *conditional expression* used to decide whether to execute the
# group of statements following the statement header.  The end of the
# statement header is indicated by a colon ``:`` character followed by
# a new line character.  In the example above the conditional
# expression is ``letter.isupper()``.

# The header line is followed by the group of statements to be
# executed if the condional expression evaluates to True. In the
# simple example above there is one statement in the group,
# ``print(letter)``, usually there would be more than one. It is very
# important to understand that the group of statements to be
# conditionally executed is defined by their *indentation* relative to
# the ``if`` statement header.

# In the example above the condition for executing the
# ``print(letter)`` statement is provided by the Boolean expression
# ``letter.ispupper()``, a function call that returns either ``True``
# of ``False``. However, you can use any valid expression as the
# condition of an ``if`` statement, not just Boolean expressions . The
# ``if`` statement provides a *Boolean context* in which the result of
# any expression is *interpreted* as either ``True`` or ``False``. If
# an expression evaluates to any of the following values it is
# interpreted as ``False``,

# + the number zero
# + the value ``None``
# + an *empty* collection such as a null string or empty list

# *Any* other value is interpreted as ``True``. Of course if the
# conditional expression is a Boolean expression there is no need for
# any intepretation because the result *is* a Boolean value. Let's
# illustrate this point with an example. Suppose you have the
# following list,

# ::

x = ['', "", 0, 0.0, [], None, "foo"]

# According to the above rule all the values in ``x`` would be
# interpreted as ``False`` by an ``if`` statement, except for the
# string "foo" which would be interpreted as ``True``. In the
# following code sample a ``for`` loop iterates over the elements in
# ``x`` and an ``if`` statement tests each the value of each element
# and only prints it when the value is intepreted as ``True``, so only
# the string "foo" is printed,

# ::

pl()

#: iterates over list x defined above,
#: it only prints "foo" because all other
#: elements in x are interpreted as False
for item in x:
    if item:
        print(item)

# So far we have used the simplest form of the if statement. In this
# form a group of statements is executed only if the conditional
# expression evaluates to ``True``.  Sometimes you also need to
# execute a particular group of statements when the conditional
# expression evaluates to ``False``. In these cases you can use the
# ``if else`` form of the ``if`` statement.

# Let's illustrate with an example. Suppose you have a list of
# integers and you want to count how many are even and how many are
# odd. You can determine whether an element in the list is even or odd
# by testing whether the remainder after division by 2 is either 0 or
# 1 respectively. Therefore, if ``n`` denotes an element in the list,
# you can test that ``n`` is even using the conditional expression ``n
# % 2 == 0`` and you can test that it is odd using the expression ``n
# % 2 == 1``.

# The following code implements the example above using a conditional
# expression that tests whether ``n`` is even. If the condition is
# ``True`` the statement to count the number of even elements in the
# list is excecuted.  If the condition is ``False`` the statement
# after the ``else`` clause is executed to count the number of odd
# elements,

# ::

pl()

#: a list of integers
x = [2, 5, 4, -1, 3]

#: initialize even and odd counts
even = 0; odd = 0

for n in x:
    # test if n is even
    if n % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

#: print counts
print("even =", even, "odd =", odd)

# You can see from this example that the ``else`` clause is very
# simple, it consists of the keyword ``else`` followed by a colon
# ``:`` and a new line character marking the end of the clause. There
# is no conditional expression in an ``else`` clause because its group
# of statements is meant to be always executed whenever the
# conditional expression of the ``if`` statement is ``False``.

# The above example can be rewritten to take advantage of the fact
# that an ``if`` statement interprets a non-zero number as the Boolean
# value ``True``. Rather than using the conditional expression ``n % 2
# == 0`` we can use the more succinct expression ``n % 2``. This
# expression evaluates to 1 when ``n`` is odd which is interpreted as
# True by the ``if`` statement. The following code implements this
# alternative solution,

# ::

pl()

#: a list of integers
x = [2, 5, 4, -1, 3]

#: initialize even and odd counts
even = 0; odd = 0

for n in x:
    # test if n is odd
    if n % 2:
        odd = odd + 1
    else:
        even = even + 1

#: print counts
print("even =", even, "odd =", odd)

# Sometimes you need to be able to execute different groups of
# statements, where *each* group is associated with a different
# conditional expression. In these cases using the ``if else`` form is
# not the best solution. For example, suppose you have a list of
# strings and you want to know the frequency of strings that are 0, 1
# and 2 characters long as well as the frequency of those with lengths
# greater than 2 characters. This problem requires multiple
# conditional expressions to test for strings of different lengths and
# requires multiple groups of statements to count the number of
# strings in each category.

# One solution to the above problem is to use nested ``if else``
# statements, as shown in the following sample code,

# ::

pl()

#: a list of strings
x = ["", "", "b", "ab", "cd", "ef", "foo"]

#: initialize frequency counts
freq0 = 0; freq1 = 0; freq2 = 0; freq = 0

#: calculate frequency of strings
#: of different sizes
for s in x:

    # nesting of groups of statements
    # and the conditional expressions
    # to execute them
    if len(s) == 0:
        freq0 = freq0 + 1
    else:
        if len(s) == 1:
            freq1 = freq1 + 1
        else:
            if len(s) == 2:
                freq2 = freq2 + 1
            else:
                freq = freq + 1

#: print frequencies
print("freq0 =", freq0, "freq1 =", freq1)
print("freq2 =", freq2, "freq =", freq)

# One problem with this solution is that the code becomes less
# readable as the level of nesting increases. Another problem is that
# it requires three *separate* ``if`` statements. A more satisfactory
# approach is to use the ``if elif`` form of the ``if`` statement.

# You can visualize the motivation for implementing the ``elif``
# clause if you look carefully at the sample code above.  If it were
# possible to extend the ``else`` clause to include a conditional
# expression, as in the ``if`` statement header, you could avoid all
# that nesting.

# That is precisely what the ``elif`` clause does. It requires a
# conditional expression and a group of statements to be executed when
# the expression is ``True``. The following code re-implements the
# example above using ``elif`` clauses,

# ::

pl()

#: a list of strings
x = ["", "", "b", "ab", "cd", "ef", "foo"]

#: initialize frequency counts
freq0 = 0; freq1 = 0; freq2 = 0; freq = 0

#: calculate frequency of strings
#: of different sizes
for s in x:

    # one 'if' statement to conditionally
    # execute multiple groups of statements
    if len(s) == 0:
        freq0 = freq0 + 1
    elif len(s) == 1:
        freq1 = freq1 + 1
    elif len(s) == 2:
        freq2 = freq2 + 1
    else:
        freq = freq + 1

#: print frequencies
print("freq0 =", freq0, "freq1 =", freq1)
print("freq2 =", freq2, "freq =", freq)

# You can see from this example that an ``if`` statement can have as
# many ``elif`` clauses as are required by the problem you are trying
# to solve. In this case we needed to test two expressions in addition
# to the one in the ``if`` statement header. The ``if elif`` form
# allows you to define in a single ``if`` statement, a chain of
# conditions and their associated groups of statements. Furthermore,
# you can end the whole chain with an optional ``else`` clause if you
# need to execute a *default* group of statements for the case in
# which all conditions are ``False``.

# References
# ----------

# + `Language Reference`_
# + `Standard Library`_
# + `Python Tutorial`_

# .. _Language Reference: https://docs.python.org/3.7/reference/index.html
# .. _Standard Library: https://docs.python.org/3.7/library/index.html
# .. _Python Tutorial: https://docs.python.org/3.7/tutorial/index.html
