# The ``list`` data type
# ----------------------

# | `Overview`_
# | `Imports`_
# | `Creating lists`_
# | `Querying lists`_
# | `Modifying lists`_
# | `Comparing lists`_
# | `Iterating lists`_
# | `References`_

# Overview
# ~~~~~~~~

# The ``list`` type is one of Python's *mutable sequence*
# types. Specifically, a ``list`` object is a mutable, ordered
# sequence of elements which can be Python objects of any
# type. Although lists can contain elements of different, arbitrary
# types, they are most commonly used when a mutable, ordered
# collection of objects of the same type is required.

# There are several ways of creating new list objects:

# + You can use a special syntax, called *list displays*, to
#   explicitly define the elements of a list when you know the
#   expressions for each element before run-time.
# + You can use the ``list(iterable)`` constructor to create a list
#   from the elements of an existing *iterable* object.
# + You can use *list comprehensions* to create a list when its
#   elements are the result of operations on the elements of one or
#   more existing iterable objects.
# + You can create a new list by *concatenating* two or more existing
#   lists.
# + You can create a new list from a *slice* of an existing list.

# The ``list`` type supports the following operations common to all
# sequence types (immutable and mutable):

# + You can test list *membership* of a given object.
# + You can *index* an element of a list to reference it.
# + You can use the built-in function ``len()`` to get the number of
#   elements in a list.
# + You can use the built-in functions ``max()`` and ``min()`` to get the
#   largest or smallest elements in a list.
# + You can use the method ``count()`` to count the occurrences of an
#   element in a list.
# + You can use the method ``index()`` to determine the index of the first
#   occurrence of an element in a list.

# Since lists are *mutable sequences* they can be modified after being
# created. Therefore, in addition to the above operations, lists support the
# following operations which modify a list in some way:

# + You can add elements to a list using the methods ``append()``,
#   ``extend()`` and ``insert()``, as well as the repetition operator
#   ``*=``.
# + You can remove elements from a list using the methods ``clear()``,
#   ``pop()`` and ``remove()``, as well as the ``del`` statement applied to
#   a slice of the list.
# + You can replace list elements at specified locations using the
#   *index* and *slice* operations as targets of an assignment statement.
# + You can reverse the order of elements with the ``reverse()`` method.
# + You can sort the elements of a list with the ``sort()`` method.

# The following sections cover these features with examples.

# Imports
# ~~~~~~~

# ::

#: import line number function
from ptlp import ln

#: import maths module, used in some examples
import math

# Creating lists
# ~~~~~~~~~~~~~~

# Creating lists using list displays
# ``````````````````````````````````

# If you want to create a list from elements you know before run-time
# you just write down the elements using a special syntax called a
# *list display*. A *list display* is simply a list of coma separated
# expressions enclosed in square brackets. For example, suppose you
# want to create a list containing the three integers 1, 2, 3 in that
# order. You define the list using the following list display, ::

x = [1, 2, 3]

# At run-time the interpreter evaluates the *list display* expression
# to a new object of type ``list``. A list display expression is
# essentially a literal for defining lists. Just like a string literal
# is special notation for telling the interpreter you want a string
# object, a list display is special notation for telling the
# interpreter you want a list object.

# To create an empty list you write a display list without any
# enclosed expressions, ::

x = []

# A list display to create a list containing a single element does not
# require a trailing comma (as is the case for tuples), you can simply
# write, ::

x = [1]

# The following list display expression defines a list of strings, ::

x = ["a", "b", "c"]

# The expressions corresponding to the elements in a list display can
# be as simple or as complex as your problem requires. In the
# following list display the elements are arithmetic expressions
# involving identifiers, function calls and arithmetic operators, ::

x = [math.sqrt(3 ** 2 + 5 ** 2), math.pi * 7 ** 2]

# The elements in a list display can be of any type, including other
# lists, ::

x = [[1], [2, 3], []]

# Lists are most commonly used in cases in which all elements are of
# the same type. However, the ``list`` type is not limited to that
# case. Lists can include a mixture of any types. The following
# example shows a list display with elements of type ``int``,
# ``float``, ``str``, ``list`` and ``tuple``, ::

x = [1, math.pi, "a", ["b", "c"], ("d",)]

# List displays can span multiple lines. This is a convenient feature
# when writing long list definitions, ::

x = ["a", "b", "c", "d", "e", "f",
     "g", "h", "i", "j", "k", "l"]


# The following examples summarise the above points on list
# displays. You can view the output in ``type_list.output``.

# ::

#: list display examples

#: an empty list
print(ln(), [])

#: a list with one element
print(ln(), [1])

#: a list of integers
print(ln(), [1, 2, 3])

#: a list of strings
print(ln(), ["a", "b", "c"])

#: a list of lists
print(ln(), [["a", "b"], ["d"], []])

#: a list with mixed types
print(ln(), [1, math.pi, "a", ["b"], ("c",)])

#: a list spanning multiple lines"
print(ln(), ["a", "b", "c",
             "d", "e", "f",
             "g", "h", "i"])

# Creating lists using ``list()`` constructor
# ```````````````````````````````````````````

# Using *list displays* you can create a list by explicitly writing
# down its elements. However, there are situations in which you don't
# know what the elements are *before* running the program.  If the
# elements you require are contained, in the right order, in an
# existing *iterable* object then you can use the ``list()``
# constructor to create the new list. The ``list()`` constructor takes
# an iterable object as an argument and returns a new list object with
# the same elements and ordering as the iterable object.

# Since sequences are iterable you can use sequence objects to create
# new lists. For example, if you have the string "abcdef" and want to
# create a list containing each letter, you simply call the
# constructor with the string as an argument, ::

#: create a list from a string
x = list("abcdef")
assert x == ["a", "b", "c", "d", "e", "f"]

# The following example creates a list from a range object, ::

#: create a list from a range
x = list(range(0,10))
assert x == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# The next example creates a list from a tuple object, ::

#: create a list from a tuple
x = list(("a", "b", "c"))
assert x == ["a", "b", "c"]

# You can, of course, create a list from an existing list, ::

#: create list 'y' from list 'x'
x = ["a", "b", "c"]
y = list(x)

#: the two lists have the same elements
assert x == y

#: but they are different list objects
assert id(x) != id(y)

# To create an empty list you call the constructor without arguments, ::

#: create an empty list
x = list()
assert x == []

# Creating lists using list comprehensions
# ````````````````````````````````````````

# Sometimes you need to create a list in which each element is the
# result of performing some calculation on the corresponding element
# of an existing iterable object. Suppose you have a string "abc" and
# you need to create a list in which an element is the result of
# prefixing each letter of the string with the underscore character
# "_" to produce the list ["_a", "_b", "_c"].

# You can construct such a list using a ``for`` statement to iterate
# over the string.  In each iteration the ``for`` loop variable is
# bound to the next letter in the string and can be used to produce a
# new element using a concatenation expression. The new element can
# then be added to the list using the ``append()`` method, ::

x = []
for i in "abc":
    x.append("_" + i)
assert x == ["_a", "_b", "_c"]

# In this and similar situations you can use special syntax called a
# *list comprehension* that allows you to write a single expression
# that evaluates to the desired list. A list comprehension expression
# starts with an opening square bracket and ends with a closing square
# bracket. In its simplest form the components enclosed in square
# brackets consist of an expression that produces each element of the
# new list, followed by a ``for`` statement that loops over the
# elements of the iterable object.

# You can use the following list comprehension to create the list
# above in a more succinct and convenient way in a single expression, ::

x = ["_" + i for i in "abc"]
assert x == ["_a", "_b", "_c"]

# The expression in terms of the ``for`` loop variable can be any
# valid expression.  The following example uses the string method
# ``upper()`` to create a list of upper case letters, ::

x = [i.upper() for i in "abc"]
assert x == ["A", "B", "C"]

# There are situations in which you want the new list to only include
# elements satisfying some condition. The list comprehension syntax
# allows the use of an ``if`` statement for that purpose. The
# following example creates a list by squaring the elements of the
# range object but only if the element is even, ::

x = [i ** 2 for i in range(0, 10) if i % 2 == 0]
assert x == [0, 4, 16, 36, 64]

# If you need to iterate over more than one iterable object you can
# use multiple ``for`` statements. Suppose you want to create a list
# in which the elements are the products of the elements in two tuples
# of integers but only including products less than 10. You can do
# that with a list comprehension with two ``for`` loops and an ``if``
# statement, ::

x = [i * j for i in (2, 2, 2) for j in (3, 4, 5) if i * j < 10]
assert x == [6, 8, 6, 8, 6, 8]

# You can write long list comprehension expressions over multiple
# lines for convenience, ::

x = [i + j + k
     for i in ("a", "b")
     for j in ("c", "d")
     for k in ("e", "f")]

assert x == ["ace", "acf",
             "ade", "adf",
             "bce", "bcf",
             "bde", "bdf"]

# Creating a list by concatenating existing lists
# ```````````````````````````````````````````````

# You can use the addition operator ``+`` to concatenate two or more
# lists to produce a new list object. The following example adds
# multiple lists, ::

x = ["a"] + ["b", "c"] + ["d", "e", "f"]
assert x == ["a", "b", "c", "d", "e", "f"]

# The operands can be names bound to list objects, ::

y = [1, 2, 3]
z = [4, 5, 6]
x = y + z
assert x == [1, 2, 3, 4, 5, 6]

# Adding the empty list produces a new list object with the same
# elements, ::

y = [1, 2]
x = [ ] + y
assert id(x) != id(y)
assert x == y

# You can use the augmented assignment operator ``+=``, ::

x = ["a", "b"]
x += ["c", "d"]
assert x == ["a", "b", "c", "d"]

# It is possible to create a new list by *repeating* an existing list
# a specified number of times using the operator ``*=``. It is shorter
# and more elegant than explicitly adding a list to itself a number of
# times. The following example creates a new list by adding list ``x``
# to itself three times, ::

x = ["a", "b"]
x *= 3
assert x == ["a", "b", "a", "b", "a", "b"]

# Creating a list by slicing an existing list
# ```````````````````````````````````````````

# Slicing returns a new list ::

#: a list of strings
x = ["a", "b", "c"]

#: creates new list ['a', 'b']
print(ln(), x[0:2])

#: creates new list ['c', 'b', 'a']
print(ln(), x[-2:])

# Use slicing to make a shallow copy of a list, ::

x = x[:]
print(ln(), x)

# Querying lists
# ~~~~~~~~~~~~~~

# Lists are sequences so you can use the standard sequence operations
# to query them. The following sections show how to use those common
# sequence operations on list objects.

# Referencing elements of a list
# ``````````````````````````````

# Since a list is a sequence you can use the indexing operator
# ``x[index]`` to reference an element of list ``x`` at a specific
# location ``index``. The first element has index 0 the second index 1
# and so on, ::

#: a list of strings
x = ["a", "b", "c"]

#: indexing operator applied to x at o
#: evaluates to first element of x
assert x[0] == "a"

#: evaluates to second element
assert x[1] == "b"

# To reference the last element in the list using the fact that the
# index of the last element is the size of the list minus 1. You can
# use the built-in function ``len()`` to get the size of a list.
# The following example shows how this done for the list ``x``, ::

#: reference last element
assert x[len(x) - 1] == "c"

# You can use a *negative* index to reference elements from the end of
# the list. You start at -1 to reference the last element, -2 the
# second last element and so on. Therefore you can reference the
# element at -1 to get the last element rather than having to
# calculate its positive index from size of the list. The next example
# makes use of negative indeces, ::

assert x[-1] == "c"
assert x[-2] == "b"

# Testing list membership
# ```````````````````````

# Given an object ``e`` and a list ``x`` it is common to ask whether x
# contains e. The operators ``in`` and ``not in`` are used to test
# whether an object is an element of a collection.

# The Boolean expression ``e in x`` returns True if e is contained in
# x, otherwise it returns False.

# ::

"c" in ["a", "b", "c"]
"d" in ["a", "b", "c"]

# The Boolean expression ``e not in x`` returns True if e is NOT
# contained in x, otherwise it returns False.

# ::

"d" not in ["a", "b", "c"]
"c" not in ["a", "b", "c"]

1 not in ["a", "b", "c"]

# Number of elements in a list
# ````````````````````````````

# Use the built-in function ``len()`` to get the number of elements in
# a list. For example, ::

assert len([]) == 0
assert len([1, 2, 3]) == 3
assert len(list(range(0,100))) == 100

# Largest and smallest element of a list
# ``````````````````````````````````````

# You have a list ``x`` defined as follows, ::

x = ["a", "b", "c"]

# To retrieve the largest element in ``x`` use the built-in function
# ``max()``, ::

assert max(x) == "c"

# To retrieve the smallest element use the built-in function
# ``min()``, ::

assert min(x) == "a"

# If all the elements of a list are equal ``max()`` and ``min()``
# return the same value, ::

assert max(["a", "a", "a"]) == "a"
assert min(["a", "a", "a"]) == "a"

# If the elements of a list cannot be compared a TypeError exception
# is raised. For example, the elements in the following list cannot be
# compared because they are of different types, ::

try:
    max([1, 2, 3, "a", "b", "c"])
except TypeError as e:
    print(ln(), "TypeError", e)

# If the list is empty a ValueError exception is raised, ::

try:
    min([])
except ValueError as e:
    print(ln(), "ValueError", e)

# Count occurrences of an element
# ```````````````````````````````

# You want to determine how many times an object e occurs in a list x.

# ::

assert ["a", "b", "c", "a"].count("a") == 2
assert ["a", "b", "c", "a"].count("c") == 1

# if not in list, ::

assert ["a", "b", "c", "a"].count("d") == 0

# Get index of first occurrence
# `````````````````````````````

# You have an element of a list and you need to know its index, ::

assert ["a", "b", "c"].index("c") == 2

# element is not contained a ValueError exception is raised, ::

try:
    ["a", "b", "c"].index("d")
except ValueError as e:
    print(ln(), "ValueError", e)

# Modifying lists
# ~~~~~~~~~~~~~~~

# Lists are mutable sequences so you can add new elements to them as
# well as remove, replace and reorder existing elements. The following
# sections discuss these list modifying operations.

# Adding elements to a list
# `````````````````````````

# + append
# + extend
# + insert

# Removing elements from a list
# `````````````````````````````

# + remove
# + pop
# + clear
# + del

# Removing elements using assignment to slice ::

x = ["a", "b", "c", "d", "e", "f"]
x[2:5] = []
print(ln(), x)

# Remove all elements from a list, ::

x = ["a", "b", "c", "d", "e", "f"]
x[:] = []
print(ln(), x)

# Replacing elements in a list
# ````````````````````````````

# Using index operator as target of assigment statement, ::

x = ["a", "b", "c"]
x[0] = "d"
print(ln(), x)

# Using slice operator as target of assigment statement, ::

x = ["a", "b", "c", "d"]
x[1:3] = ["d", "d"]
print(ln(), x)

# Sorting and reversing elements
# ``````````````````````````````

# You can sort the elements of a list, ::

#: a list of integers
x = [3, 1, 2]

#: sort list in place
#: note that the sort method returns
#: the value 'None' not the sorted list
assert x.sort() == None
print(ln(), x)

# You can reverse the order of elements using the ``reverse()``
# method, ::

#: a list of strings
x = ["a", "b", "c"]

#: reverse list in place
#: note that the reverse method returns
#: the value 'None' not the reversed list
assert x.reverse() == None
print(ln(), x)

# Comparing lists
# ~~~~~~~~~~~~~~~

# You can compare lists containing objects of the same type.

# ::

assert [1, 2] == [1, 2]
assert [1, 2] != [1, 3]
assert [1, 2] != []
assert [1, 2] != ["1", "2"]

# Iterating lists
# ~~~~~~~~~~~~~~~

# ::

x = ["a", "b", "c"]
for i in x:
    print(ln(), i)

x = [1, 2, 3]
for i in x:
    print(ln(), i)

# References
# ~~~~~~~~~~

# + `Standard type hierarchy (LR)`_
# + `Sequence types (SL)`_
# + `Lists (PT)`_
# + `More on lists (PT)`_

# .. _Standard type hierarchy (LR): https://docs.python.org/3.7/reference/datamodel.html#the-standard-type-hierarchy
# .. _Sequence types (SL): https://docs.python.org/3.7/library/stdtypes.html#sequence-types-list-tuple-range
# .. _Lists (PT): https://docs.python.org/3.7/tutorial/introduction.html#lists
# .. _More on lists (PT): https://docs.python.org/3.7/tutorial/datastructures.html#more-on-lists
