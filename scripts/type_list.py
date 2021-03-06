# The ``list`` data type
# ======================

# .. contents::
#    :local:
#    :depth: 1
#    :backlinks: none

# Overview
# ~~~~~~~~

# The ``list`` type is one of Python's *mutable sequence*
# types. Specifically, a ``list`` object is a mutable, ordered
# sequence of elements which can be objects of any type. Although
# lists can contain elements of different types they are most commonly
# used when a mutable, ordered collection of objects of the *same*
# type is required.

# The following are different ways of creating *new* list objects:

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

# The ``list`` type supports the following *querying* operations
# common to all sequence types (mutable and immutable):

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

print('Example 1:')

# import maths module, used in some examples
import math

# Creating lists
# ~~~~~~~~~~~~~~

# Creating lists using list displays
# ``````````````````````````````````

# If you want to create a list from elements you know before run-time
# you can write down the elements using a special syntax called a
# *list display*. A *list display* is simply a list of coma separated
# expressions enclosed in square brackets. For example, suppose you
# want to create a list containing the three integers 1, 2 and 3 in
# that order. You define the list using the following list display,

print('Example 2:')

# list display to create
# a list of integers
x = [1, 2, 3]
print(x)

# confirm x is a list
print(type(x))

# At run-time the interpreter evaluates the *list display* expression
# to a new object of type ``list``. A list display expression is
# essentially a literal for defining lists. Just like a string literal
# is special notation for telling the interpreter you want a string
# object, a list display is special notation for telling the
# interpreter you want a list object.

# To create an empty list you write a display list without any
# enclosed expressions,

print('Example 3:')

# list display to create
# an empty list
x = []
print(x)

# confirm x is empty
assert len(x) == 0

# You can create a list containing a single element using the
# following list display,

print('Example 4:')

# list display to create
# a singleton list
x = [1]
print(x)

# Note that, unlike creating a singleton tuple, creating a singleton
# list does not require a trailing comma.

# The expressions corresponding to the elements in a list display can
# be as simple or as complex as your problem requires. In the
# following list display the elements are arithmetic expressions
# involving identifiers, function calls and arithmetic operators,

print('Example 5:')

# list display with
# compound expressions
x = [math.sqrt(3 ** 2 + 5 ** 2), math.pi * 7 ** 2]
print(x)

# You can use list displays to create lists with elements of any type
# as shown in the following examples,

print('Example 6:')

# list display to create
# a list of strings
x = ["", "a", "bc"]
print(x)

# list display to create
# a list of tuples
x = [(), (1,), (2, 3)]
print(x)

# list display to create
# a list of lists
x = [[], [1], [2, 3]]
print(x)

# As mentioned earlier, lists are most commonly used in cases in which
# all elements are of the same type. However, the ``list`` type is not
# limited to that case. A list can include elements of different
# types. The following example shows a list display with elements of
# type ``int``, ``float``, ``str``, ``list`` and ``tuple``,

print('Example 7:')

# list display with elements
# of different types
x = [0, math.pi, "abc", ["a", "b"], (1, 2)]
print(x)

# If you need to define a very long list you can make a list display
# span multiple lines as show in the next example,

print('Example 8:')

# list display spanning
# multiple lines
x = ["a", "b", "c",
     "d", "e", "f",
     "g", "h", "i",
     "j", "k", "l"]
print(x)

# Creating lists using ``list()`` constructor
# ```````````````````````````````````````````

# As discussed in the previous section you can create a list by
# explicitly writing down its elements using list displays. However,
# sometimes you don't know the elements before running the program.
# If the elements you require are contained in an existing *iterable*
# object then you can use the ``list()`` constructor to create the new
# list. The ``list()`` constructor takes an iterable object as an
# argument and returns a new list object with the same elements and
# ordering as that of its argument.

# Since sequences are iterable you can use sequence objects to create
# new lists. For example, if you have the string "abc" and want to
# create a list consisting of each letter of the string, you call the
# ``list()`` constructor with the string as an argument,

print('Example 9:')

# invoke list constructor to create
# a list from a string
x = list("abc")
assert x == ["a", "b", "c"]

# In the following examples the ``list()`` constructor is used to
# create a new list from different types of iterable objects,

print('Example 10:')

# invoke list constructor to create
# a list from a range
x = list(range(0,5))
assert x == [0, 1, 2, 3, 4]

# invoke list constructor to create
# a list from a tuple
x = list(("a", "b", "c"))
assert x == ["a", "b", "c"]

# invoke list constructor to create
# a list from an existing list
y = ["a", "b", "c"]
x = list(y)

# the two lists have the same elements
assert x == y
# but they are different list objects
assert id(x) != id(y)

# You can create an empty list by invoking the ``list()`` constructor
# without an argument,

print('Example 11:')

# invoke list constructor to create
# an empty list
x = list()
assert x == []

# Creating lists using list comprehensions
# ````````````````````````````````````````

# The previous section shows that you can create a new list from the
# elements of an existing iterable object using the ``list()``
# constructor.  However, sometimes you need to create a list from the
# elements of an iterable object by first performing some calculation
# on each of its elements. For example, suppose you have a string
# "abc" and you need to create a list from its letters by prefixing
# each with the underscore character "_" to produce the list ["_a",
# "_b", "_c"].

# You can accomplish this using a ``for`` statement to iterate over
# the string.  In each iteration the ``for`` loop variable is bound to
# the next letter in the string and can be used to produce a new
# element using a concatenation expression. The new element can then
# be added to the list using the ``append()`` method as show in the
# following snippet,

print('Example 12:')

x = []
for item in "abc":
    x.append("_" + item)
assert x == ["_a", "_b", "_c"]

# In this and similar situations you can use special syntax called a
# *list comprehension* that allows you to write the equivalent of the
# ``for`` loop in a single expression that evaluates to the desired
# list.

# A list comprehension expression starts with an opening square
# bracket and ends with a closing square bracket. In its simplest form
# the components enclosed in square brackets consist of an expression
# that produces each element of the new list, followed by a ``for``
# statement that loops over the elements of the given iterable
# object.

# You can use the following list comprehension to create the list
# above in a more succinct and convenient way in a single expression,

print('Example 13:')

# list comprehension to create
# a list from a string by prefixing
# each element with underscore
x = ["_" + item for item in "abc"]
assert x == ["_a", "_b", "_c"]

# The expression before the ``for`` loop can be any valid exression
# involving the loop variable (``item`` in this case) which is bound
# to a new element of the given iterable object at the start of every
# iteration. The following example uses the string method ``upper()``
# to create a list of upper case letters from the string "abc",

print('Example 14:')

# list comprehension to create
# a list from a string by making
# each element upper case
x = [item.upper() for item in "abc"]
assert x == ["A", "B", "C"]

# There are situations in which you want the new list to only include
# elements satisfying some condition. The list comprehension syntax
# allows the use of an ``if`` statement for that purpose. The
# following example creates a list by squaring the elements of the
# range object but only if the element is even,

print('Example 15:')

# list comprehension with conditional filtering
x = [item ** 2 for item in range(0, 10) if item % 2 == 0]
assert x == [0, 4, 16, 36, 64]

# If you need to iterate over more than one iterable object you can
# use multiple ``for`` statements. Suppose you want to create a list
# in which the elements are the products of the elements in two tuples
# of integers but only including products less than 10. You can do
# that with a list comprehension with two ``for`` loops and an ``if``
# statement,

print('Example 16:')

# list comprehension with multiple 'for' loops
x = [m * n for m in (2, 2, 2) for n in (3, 4, 5) if m * n < 10]
assert x == [6, 8, 6, 8, 6, 8]

# If you need to write a long list comprehension you can make it span
# multiple lines,

print('Example 17:')

# list comprehension spanning
# multiple lines
x = [l + m + n
     for l in ("a", "b")
     for m in ("c", "d")
     for n in ("e", "f")]

assert x == ["ace", "acf",
             "ade", "adf",
             "bce", "bcf",
             "bde", "bdf"]

# Creating a list by concatenating existing lists
# ```````````````````````````````````````````````

# If you want to create a new list by combining the elements of
# existing lists you can use the addition operator ``+`` to
# *concatenate* two or more lists. The following are examples of
# creating new lists by *adding* existing lists,

print('Example 18:')

# create a list by 'adding' two existing lists 
x = ["a"] + ["b", "c"]
assert x == ["a", "b", "c"]

# create a list by 'adding' three existing lists
x = [1, 2]; y = [3, 4];
z = x + y + [5, 6]
assert z == [1, 2, 3, 4, 5, 6]

# Adding the empty list to an existing list creates a new list object
# that is a copy of the list,

print('Example 19:')

# 'adding' an empty list to an existing
# list creates a copy of the list
y = [1, 2, 3]
x = [ ] + y

# confirm x is a copy of y
assert x == y

# confirm x and y are different objects
assert id(x) != id(y)

# It is possible to create a new list by *repeating* an existing list
# a specified number of times using the operator ``*=``. It is shorter
# and more elegant than explicitly adding a list to itself a number of
# times. The following example creates a new list by adding list ``x``
# to itself three times,

print('Example 20:')

x = ["a", "b"]
x *= 3
assert x == ["a", "b", "a", "b", "a", "b"]

# Creating a list by slicing an existing list
# ```````````````````````````````````````````

# You can create a new list by *slicing* an existing list using the
# *slice* operator ``x[i:j]``. Here ``x`` is an existing list; the
# first argument ``i`` is the index of the element of ``x`` that you
# want to be the first element in the new list; and ``j`` is the index
# of the last element you want included *plus* 1. For example, suppose
# you have the following list of strings,

print('Example 21:')

y = ["a", "b", "c", "d", "e", "f"]

# You want to create a new list from a slice of ``y`` containing the
# elements "c", "d" and "e". The index of "c" is 2 (counting from 0
# from the the beginning of list ``y``). Therefore 2 is the first
# argument of the slice operator. The index of "e" is 4 so you add 1
# to it to get 5, the second argument of the slice operator,

print('Example 22:')

# create a list by slicing
# an existing list
x = y[2:5]
assert x == ["c", "d", "e"]

# If you are creating a slice from the beginning of an existing list
# you can omit the first argument of the slice operator. It is assumed
# to be 0. For example, if you want to create a slice from ``y``
# containing elements "a", "b" and "c", you only have to include the
# second argument (the index of the last element you want to include
# *plus* 1),

print('Example 23:')

# create a list by slicing
# from the beginning of existing list
x = y[:3]
assert x == ["a", "b", "c"]

# Similarly you can create a slice to the end of the list by omitting
# the last argument,

print('Example 24:')

# create a list by slicing
# to the end of existing list
x = y[3:]
assert x == ["d", "e", "f"]

# If you omit both arguments the slicing operation makes a shallow
# copy of the list. In the following example ``x`` is a new list
# containing references to the same objects as list ``y``,

print('Example 25:')

# create a copy of a list
# using slice operator
x = y[:]
assert x == y

# You can use negative arguments with the slice operator to indicate
# you are counting from the end of the list starting at -1. For
# example, suppose you want to create slice ``["c", "d", "e"]`` from
# list ``y`` above using negative indices. The first element "c" has
# index -4 and the last element "e" has index -2, you add 1 to it to
# get -1 for the second argument of the slice operator,

print('Example 26:')

x = y[-4:-1]
assert x == ["c", "d", "e"]

# Querying lists
# ~~~~~~~~~~~~~~

# Lists are sequences so you can use the standard sequence operations
# to query them. The following sections show how to use those common
# sequence operations on list objects.

# Referencing elements of a list
# ``````````````````````````````

# Since a list is a sequence you can use the indexing operator
# ``x[i]`` to reference an element of list ``x`` at a specific index
# ``i``. The first element has index 0, the second index 1 and so on.
# Suppose you have the following list of strings,

print('Example 27:')

# a list of strings
x = ["a", "b", "c"]

# The following examples show how to reference the elemens of list
# ``x`` using the index operator,

print('Example 28:')

# reference first element of x
assert x[0] == "a"
# reference second element of x
assert x[1] == "b"
# reference third element of x
assert x[2] == "c"

# If you specify an index that is out of range the interpreter raises
# an ``IndexError`` exception with the error message "list index out of
# range", as shown in the following example,

print('Example 29:')

# attempt to reference an element
# with an index that is out of range
try:
    x[3]
except IndexError as e:
    print(e)

# You can avoid this problem using the built-in function ``len()`` to
# calculate the index of the last element, provided the list is not
# empty,

print('Example 30:')

# reference last element
# calculating its index
# from list length
assert x[len(x) - 1] == "c"

# You can also use *negative* indices to reference elements from the
# end of the list. Index -1 references the last element, -2 the second
# last element and so on. Therefore, you can also reference the last
# element of a list using its negative index rather than calculating
# its positive index from the length of the list. In the following
# snippet the elements of list ``x`` are referenced using negative
# indices,

print('Example 31:')

assert x[-1] == "c"
assert x[-2] == "b"
assert x[-3] == "a"

# Testing list membership
# ```````````````````````

# A common requirement is to ask whether a given object is an element
# of a specified list.  You can use the membership operators ``in``
# and ``not in`` for this task. Suppose you have the following list,

print('Example 32:')

x = ["a", "b", "c"]

# Let ``item`` be an arbitrary object. The expression ``item in x``
# evaluates to True if ``item`` is an element of list ``x``, otherwise
# it evaluates to False,

print('Example 33:')

# confirm "c" is an
# element of x
assert "c" in x

# confirm "d" is not an
# element of x
assert ("d" in x) == False

# The expression ``item not in x`` evaluates to True if ``item`` is
# not an element of list ``x``, otherwise it evaluates to False,

print('Example 34:')

# confirm "d" is not an
# element of x
assert "d" not in x

# confirm "c" is an
# element of x
assert ("c" not in x) == False

# Largest and smallest element of a list
# ``````````````````````````````````````

# You can use the built-in functions ``max()`` and ``min()`` to
# reference the largest and smallest elements of a list
# respectively. Suppose you have the following list,

print('Example 35:')

x = ["a", "b", "c"]

# the largest element is "c" and the smallest is "a",

print('Example 36:')

# confirm largest element is "c"
assert max(x) == "c"

# confirm smallest element is "a"
assert min(x) == "a"

# If a list contains only one element or all the elements are the same
# the functions ``max()`` and ``min()`` return the same value,

print('Example 37:')

# confirm largest = smallest
x = ["a"]
assert max(x) == min(x)

x = ["a", "a", "a"]
assert max(x) == min(x)

# If the elements of a list cannot be compared the interpreter raises
# a ``TypeError`` exception. For example, the elements in the
# following list cannot be compared because they are a mixture of
# ``str`` and ``int`` types,

print('Example 38:')

# attempt to compare 'int' and 'str'
# elements raises a TypeError exception
x = [1, "a"]
try:
    max(x)
except TypeError as e:
    print("TypeError", e)

# If the list is empty the interpreter raises a ``ValueError``
# exception,

print('Example 39:')

# attempt to call 'max()' with an empty list
# raises a ValueError exception
try:
    max([])
except ValueError as e:
    print("ValueError", e)

# Counting occurrences of an element
# ``````````````````````````````````

# Lists can contain more than one instance of the same element. There
# are situations in which you want to determine exactly how many times
# a given element occurs in a list. The method ``count()`` can be used
# for that purpose. As an example, suppose you have the following
# list,

print('Example 40:')

x = ["a", "a", "c", "a"]

# You want to determine how many times the elements "a" and "c" appear
# in ``x``. You simply invoke ``x.count()`` with each element as an
# argument in turn as show in the following snippet,

print('Example 41:')

# element "a" occurs three times
assert x.count("a") == 3

# element "c" occurs 1 time
assert x.count("c") == 1

# "d" is not an element of x
# so its count is 0
assert x.count("d") == 0

# Getting the index of first occurrence
# `````````````````````````````````````

# We saw above that if you have the index of an element you can
# reference it using the index operator. Sometimes you need to do the
# opposite. That is, you have an element and you want to get its
# index. The method ``index()`` can be used for that purpose. Suppose
# you have a list ``x`` as follows,

print('Example 42:')

x = ["a", "b", "c"]

# To get the index of one of its elements you invoke ``x.index()``
# passing the element as an argument, the following are examples,

print('Example 43:')

# index of "a" is 0
assert x.index("a") == 0
# index of "b" is 1
assert x.index("b") == 1
# index of "c" is 2
assert x.index("c") == 2

# If the object you pass to the ``index()`` method is not an element
# of the list the interpreter raises a ``ValueError`` exception, as
# show in the following snippet

print('Example 44:')

# attempt to get index of an object
# that is not an element of x
try:
    x.index("d")
except ValueError as e:
    print("ValueError", e)

# Modifying lists
# ~~~~~~~~~~~~~~~

# Lists are *mutable* sequences so you can add, remove, replace and
# reorder its elements. This section introduces these list
# modification operations. I first introduce the ``append()`` and
# ``extend()`` methods and the augmented assignment statement ``+=``,
# three ways of adding elements to the end of a list. I then cover the
# ``insert()`` method, a way of adding an element to a list at a
# specified index. This is followed by a discussion of the ``pop()``,
# ``remove()`` and ``clear()`` methods and the ``del`` statement, all
# ways of removing elements from a list. Then I show how to use the
# index operator as a *target* of an assignment statement to replace
# an element of a list at a specified index. I also show how *list
# slicing* operations can be used to add, replace and remove elements
# in a consistent and elegant way. The section ends with a discussion
# of the ``sort()`` and ``reverse()`` methods, two ways of reording
# the elements of a list.

# Adding elements to a list
# `````````````````````````

# Adding elements to the end of a list
# ....................................

# You can use the ``append()`` and ``extend()`` methods to add
# elements to the end of a list. The ``append()`` method takes a
# single object as an argument and adds it to the end of the
# list. Suppose you have the following list,

print('Example 45:')

x = ["a"]

# You can add the strings "b" and "c" to the end of list ``x`` using
# the ``append()`` method twice,

print('Example 46:')

# add "b" to end of list x
x.append("b")
assert x == ["a", "b"]

# add "c" to end of list x
x.append("c")
assert x == ["a", "b", "c"]

# It is important to note that the ``append()`` method does not return
# the modified list, it returns the value ``None``. The following
# snippet adds string "d" to list ``x`` and confirms that the call to
# ``append()`` evaluates to ``None``,

print('Example 47:')

# append() method returns None
assert x.append("d") == None

# The fact that ``append()`` returns ``None`` rather than the modified
# list reminds us that it works by modifying the instance on which
# it's invoked and does not return a new object.

# Let's consider now the ``extend()`` method. It takes an *iterable*
# object as an argument and adds each of its elements to the end of
# the list on which it is invoked. Since sequences are iterable you
# can use any sequence object to extend an existing list. The
# following example shows how a list can be extended using a string, a
# tuple and another list,

print('Example 48:')

# extend list x using a string
x = ["a"]
x.extend("bc")
assert x == ["a", "b", "c"]

# extend list x using a tuple
x = ["a"]
x.extend(("b", "c"))
assert x == ["a", "b", "c"]

# extend list x using another list
x = ["a"]
x.extend(["b", "c"])
assert x == ["a", "b", "c"]

# Like the ``append()`` method, the ``extend()`` method returns
# ``None`` instead of the modified list,

print('Example 49:')

# extend() method returns None
x = ["a"]
assert x.extend("bc") == None

# An alternative to the ``extend()`` method is the *assignment with
# addition* statement ``+=``. Suppose you have the following list,

print('Example 50:')

x = ["a"]

# To add elements to ``x`` using an iterable object, say the string
# "bc", you make ``x`` the target of the *assignment with addition*
# statement ``+=``,

print('Example 51:')

x += "bc"

# The interpreter evaluates this statement (roughly) in the following
# way: it evaluates list ``x``, it evaluates the iterable object "bc",
# it iterates over "bc" adding each element to the end of list ``x``
# and finally rebinds the resulting list to ``x``. This is illustrated
# in the following snippet,

print('Example 52:')

# a list
x = ["a"]

# save its object id
idx = id(x)

# add elements in iterable "bc" to list x
x += "bc"

# confirm elements were added
assert x == ["a", "b", "c"]

# confirm x is bound to the original list object
assert id(x) == idx

# The following examples extend a list using a tuple and another list,

print('Example 53:')

# add elements of tuple to list x 
x = ["a"]
x += ("b", "c")

# add elements of list to list x
x = ["a"]
x += ["b", "c"]

# It is important to note that the *assignment with addition*
# statement ``x += iterable`` is *not* the same as ``x = x +
# iterable``, where ``iterable`` is an arbitrary iterable
# object. Firstly, the second form only works if ``iterable`` is of
# type ``list``. In addition, the second form is a concatenation
# operation which creates a new object and binds it to ``x``, as shown
# in the following snippet,

print('Example 54:')

# a list
x = ["a"]

# save its object id
idx = id(x)

# add elements of a list to list x
# using addition operator
x = x + ["b", "c"]

# confirm elements were added
assert x == ["a", "b", "c"]

# confirm x is a new list object
assert id(x) != idx

# Adding an element at a specified index
# ......................................

# Sometimes you want to add an element at a specific location in a
# list rather than the end. You can use the ``insert()`` method to add
# an element at a specified index. The ``insert()`` method takes two
# arguments. The first argument is the index at which to insert a new
# element, the second arguement is a reference to the object you want
# to insert.

# The following examples illustrate how to insert an element in a list
# ``x`` at index 0 (index of first element), at index ``len(x) - 1``
# (index of last element) and at an index between these two locations,

print('Example 55:')

# a list x
x = ["b", "c", "d"]

# insert "a" at index 0,
# making it first element
x.insert(0, "a")
assert x == ["a", "b", "c", "d"]

# a list x
x = ["a", "b", "d"]

# insert "c" at index len(x) - 1,
# index of last element
x.insert(len(x) - 1, "c")
assert x == ["a", "b", "c", "d"]

# a list x
x = ["a", "c", "d"]

# insert "b" at index 1,
# index of second element
x.insert(1, "b")
assert x == ["a", "b", "c", "d"]

# You can insert an element at the end of a list by specifying an
# index *greater* than the index of the last element in the list,

print('Example 56:')

# a list x
x = ["a"]

# insert "b" at end of list using
# an index greater than 0, say 1
x.insert(1, "b")
assert x == ["a", "b"]

# insert "c" at end of list using
# an index greater than 1, say 10
x.insert(10, "c")
assert x == ["a", "b", "c"]

# The ``insert()`` method accepts negative indices counting from the
# end of the list. For example,

print('Example 57:')

# a list x
x = ["b", "c"]

# insert "a" at index -2
x.insert(-2, "a")
assert x == ["a", "b", "c"]

# a list x
x = ["a", "c"]

# insert "b" at index -1
x.insert(-1, "b")
assert x == ["a", "b", "c"]

# If you specify a negative index that is less than the negative index
# of the first element, the ``insert()`` method simply inserts the
# element at the beginning of the list,

print('Example 58:')

# a list x
x = ["b", "c"]

# insert "a" at start of list using
# an index <  -2, say -10
x.insert(-10, "a")
assert x == ["a", "b", "c"]

# You can also use the ``insert()`` method to add an element to an
# empty list by specifying any integer value as the index,

print('Example 59:')

# an empty list x
x = []

# add element using index 0
x.insert(0, "a")
assert x == ["a"]

# an empty list x
x = []

# add element using index 1
x.insert(1, "a")
assert x == ["a"]

# an empty list x
x = []

# add element using index -1
x.insert(-1, "a")
assert x == ["a"]

# Finally, note that the ``insert()`` method also returns ``None``
# rather than the modified list,

print('Example 60:')

# insert() method returns None
x = ["b"]
assert x.insert(0, "a") == None

# Removing elements from a list
# `````````````````````````````

# To remove elements from a list you can use the ``clear()``,
# ``remove()`` and ``pop()`` methods and the ``del`` statement.

# You use the ``clear()`` method to remove *all* elements from a list,

print('Example 61:')

# a list x
x = ["a", "b", "c"]

# remove all elements from x
x.clear()

# confirm all elements removed
assert x == []

# You use the ``remove()`` method to remove the *first* element in a
# list that is *equal* to a given object.  For example, suppose you
# have a list in which the string "b" occurs serveral times,

print('Example 62:')

x = ["a", "b", "c", "b", "b"]

# To remove the first occurrence of "b" you invoke the ``remove()``
# method with the string object "b" as an argument,

print('Example 63:')

# remove first element equal to "b"
x.remove("b")

# confirm first occurrence of "b" was removed
assert x == ["a", "c", "b", "b"]

# If no element in the list is equal to the object passed to
# ``remove()`` the interpreter raises an exception,

print('Example 64:')

# a list x
x = ["a", "b", "c"]

# attempt to remove element not in x
# raises a ValueError exception
try:
    x.remove("d")
except ValueError as e:
    print("ValueError", e)

# Like other list modification methods ``clear()`` and ``remove()``
# return ``None``, not the modified list,

print('Example 65:')

# confirm clear() returns None
x = ["a", "b", "c"]
assert x.clear() == None

# confirm remove() returns None
x = ["a", "b", "c"]
assert x.remove("b") == None

# You use the ``pop()`` method to retrieve *and* remove an element at
# a specified index,

print('Example 66:')

# a list x
x = ["a", "b", "c"]

# retrieve and remove element at index 0
y = x.pop(0)

# confirm element retrieved
assert y == "a"

# confirm element removed
assert x == ["b", "c"]

# Invoking the ``pop()`` method without arguments retrieves and
# removes the last element in the list,

print('Example 67:')

# a list x
x = ["a", "b", "c"]

# retrieve and remove last element
y = x.pop()

# confirm last element retrieved
assert y == "c"

# confirm last element removed
assert x == ["a", "b"]

# You can use the ``del`` statement with the index operator to remove
# an element from a list at a specified index,

print('Example 68:')

# a list x
x = ["a", "b", "c"]

# remove element at index 0
del x[0]

# confirm
assert x == ["b", "c"]

# Replacing elements in a list
# ````````````````````````````

# You can replace elements in a list using the index operator as a
# target of an assigment statement,

print('Example 69:')

# a list x
x = ["a", "b", "c"]

# replace first element 
x[0] = "d"

# confirm
assert x == ["d", "b", "c"]

# Modifying lists using list slices
# `````````````````````````````````

# Most of the list modification operations described above can also be
# performed using list slices as the *target* of an assignment
# statement.

# In this section I first consider some general characteristics of
# list *slicing*. I then show that assigning an iterable object to a
# list slice is interpreted by Python as a *replacement* operation in
# which the elements represented by the list slice are replaced, in
# the actual list, by the elements of the iterable object. In other
# words, it is a way of telling the interpreter how to replace
# elements in a list.

# In this section I also consider the case in which the two arguments
# of the slice operator are set to the same value. I show that, in the
# context of an assignment statement, this is interpreted as an
# *insertion* operation in which the elements of an interable object
# are inserted at the index specified in the slice operator,
# 'pushing', as it were, the existing elements in the actual list to
# the 'right'.

# Suppose you have a list ``x`` and you want to represent a subset of
# ``x`` consisting of a contiguous sub-sequence of its elements. This
# sub-sequence is commonly called a *slice* of ``x``. You can use the
# *slice* operator to represent such list slices. Suppose the index of
# the first element of x to be included in the slice is ``i`` and the
# index of the last element to be included is ``j``, so that ``i`` <
# ``j``. Then this slice of ``x`` is represented by ``x[i:j+1]``.

# Note that the first argument ``i`` is the index of the first element
# of the slice while the second argument ``j+1`` points to an element
# immediately after the last element of the slice. The following are
# some examples of list slices,

print('Example 70:')

# a list x
x = ["a", "b", "c" ,"d", "e", "f"]

# create a slice of x starting at index 0
# and ending at index 2
assert x[0:3] == ["a", "b", "c"]

# create a slice of x starting at index 2
# and ending at index 4
assert x[2:5] == ["c", "d", "e"]

# create a slice of x starting at index 4
# and ending at index 5
assert x[4:len(x)] == ["e", "f"]

# create a slice of x starting at index 2
# and endining at index 2
assert x[2:3] == ["c"]

# The slice operator can take an optional third argument to indicate
# the *slice step* to use when producing the slice. A slice step
# indicates how much you have to add to the index of the current
# element in the slice to obtain the index of the next element in the
# slice. For example, suppose you have the following list,

print('Example 71:')

# a list x
x = ["a", "b", "c", "d", "e", "f"]

# You want to create a slice containing elements "a", "c" and "e". The
# first element of the slice is "a" which has index 0. You add the
# slice step to index 0 to get index 2, the index of "c", the next
# element in the slice. You now add the slice step to index 2 to get
# index 4, the index of "e", the next and last element in the
# slice. The following snippet shows the invocation of the slice
# operator for this example,

print('Example 72:')

# create a slice of x using a slice step of 2
assert x[0:len(x):2] == ["a", "c", "e"]

# Note that a slice step of 1 is equivalent to the standard case in
# which we omit the third argument to the slice operator. The
# following snippet shows this equivalence,

print('Example 73:')

# a list x
x = ["a", "b", "c", "d", "e", "f"]

# confirm a slice step of 1 is the same
# as omitting slice step argument
assert x[0:len(x)] == x[0:len(x):1]

# When a list slice is used as the 'target' of an assignment statement
# with an iterable object as the 'source', the statement is
# interpreted as a replacement operation.

print('Example 74:')

# a list x
x = ["a", "d", "e", "f"]

# replace from "d" to "f"
x[1:4] = ["b", "c"]

# confirm slice replaced
assert x == ["a", "b", "c"]

# a list x
x = ["a", "d"]

# replace "d" 
x[1:2] = ["b", "c"]

# confirm slice replaced
assert x == ["a", "b", "c"]

# a list x
x = ["a", "b", "c", "d", "e", "f"]

# remove slice from "d" to end of list
x[3:len(x)] = []

# confirm slice removed
assert x == ["a", "b", "c"]

# a list x
x = ["a", "b", "c"]

# remove all elements in list
x[:] = []

# confirm all elements removed
assert x == []

# If you set the two arguments of the slice operator to the same value
# the operator evaluates to the empty list ``[]``. This is shown in the
# next example,

print('Example 75:')

# a list x
x = ["a", "b" ,"c"]

# a slice of x with both arguments set to
# the same value produces the empty list
assert x[0:0] == []
assert x[1:1] == []
assert x[2:2] == []
assert x[len(x):len(x)] == []

# Using a list slice with two arguments set to the same value, in the
# context of an assignment statement, is interpreted as an
# insertion operation.

print('Example 76:')

# a list x
x = ["d", "e", "f"]

# insert elements at index 0
# i.e. at beginning of list
x[0:0] = ["a", "b", "c"]

# confirm elements inserted
assert x == ["a", "b", "c", "d", "e", "f"]

# a list x
x = ["a", "b", "c"]

# 'insert' elements at index len(x)
# i.e. index immediatly after last element
x[len(x):len(x)] = ["d", "e", "f"]

# confirm elements added
assert x == ["a", "b", "c", "d", "e", "f"]

# Note that if the empty list is assigned nothing happens,

print('Example 77:')

# a list x
x = ["a", "b", "c"]

# assign empty list
x[1:1] = []

# confirm nothing happens
assert x == ["a", "b", "c"]

# To **add an element** to the end of a list you can use a slice of
# the list with the first and second arguments set to an index that
# points *past* the last element in the list. The first index that
# points past the last element is equal to the length of the list
# which is conveniently obtained using the built-in function
# ``len()``. The following is an example,

print('Example 78:')

# a list x
x = ["a"]

# add string "b" to end of list x  using length
# of list as arguments to the slice operator
x[len(x):len(x)] = ["b"]

# confirm string "b" added
assert x == ["a", "b"]

# You can use a similar approach to **extend a list** with the
# elements of a given iterable object. You set both arguments of the
# slice operator to the length of the list so it 'points' past the
# last element and 'assign' the iterable object using the assignment
# statement. This is shown in the following example,

print('Example 79:')

# a list x
x = ["a"]

# extend list using a string
x[len(x):len(x)] = "bc"

# confirm list was extended
assert x == ["a", "b", "c"]

# a list x
x = ["a"]

# extend list using a tuple
x[len(x):len(x)] = ("b", "c")

# confirm list was extended
assert x == ["a", "b", "c"]

# You can extend an empty list by setting both arguments of the slice
# operator to 0 or by omitting both arguments as shown in the next
# example,

print('Example 80:')

# an empty list x
x = []

# extend list using another list
x[:] = ["a", "b", "c"]

# confirm list was extended
assert x == ["a", "b", "c"]

# You can **insert elements** at a specified index by setting both
# arguments of the slice operator to the desired index.  The left hand
# side of the assignment statement must be an interable object. The
# following are examples list insert operations,

print('Example 81:')

# a list x
x = [3]

# insert at index 0 using another list
x[0:0] = [1, 2]

# confirm elements were inserted
assert x == [1, 2, 3]

# a list x
x = ["a", "d"]

# insert at index 1 using a tuple
x[1:1] = ("b", "c")

# confirm elements were inserted
assert x == ["a", "b", "c", "d"]

# You can conveniently insert elements at the last index of the list
# using the length of the list or the negative index of the last
# element, -1,

print('Example 82:')

# a list x
x = ["a", "d"]

# insert at last index using list length
# to calculate last index
x[len(x)-1:len(x)-1] = ["b", "c"]

# confirm elements were inserted
assert x == ["a", "b", "c", "d"]

# a list x
x = ["a", "d"]

# insert at last index using negative
# index of last element, i.e. -1
x[-1:-1] = ["b", "c"]

# confirm elements were inserted
assert x == ["a", "b", "c", "d"]

# You can also remove elements using a list slice as the target of the
# ``del`` statement. This is an alternative to assigning the empty
# list to a list slice. The following examples illustrate,

print('Example 83:')

# a list x
x = ["a", "b", "c", "d", "e", "f"]

# remove element "b" to "e"
del x[1:5]

# confirm elements removed
assert x == ["a", "f"]

# a list x
x = [1, 2, 3]

# remove all elements
del x[:]

# confirm all elements removed
assert x == []

# Sorting and reversing elements
# ``````````````````````````````

# A common requirement is to sort the elements of a list. You can use
# the ``sort()`` method to sort the elements of a list *in place*. The
# elements of the list must be of the same type and support the less
# than '<' operation. For example, you can sort the following list of
# integers,

print('Example 84:')

x = [3, 1, 2]
assert x.sort() == None
assert x == [1, 2, 3]

# Note that the ``sort()`` method does not return the sorted list. It
# returns ``None`` instead. This is a reminder that sorting is
# performed *in place* modifying the original list. This approach
# saves memory when sorting large lists.

# Sometimes you want to create a new list containing the same elements
# of an existing list but in the *reverse order*. You can you use the
# ``reverse()`` method for that task. Like the ``sort()`` method above
# reversing modifies the original list and returns ``None``. For
# example, suppose you want to reverse the order of the following list
# of strings,

print('Example 85:')

x = ["a", "b", "c"]
assert x.reverse() == None
assert x == ["c", "b", "a"]

# Comparing lists
# ~~~~~~~~~~~~~~~

# You can compare lists with elements of the same type and the same
# number of elements using the comparison operator ``==``.

# Two lists with the same elements,

print('Example 86:')

x = list("abc")
y = list("abc")
assert id(x) != id(y)
assert x == y

# Two empty lists,

print('Example 87:')

x = list()
y = list()
assert id(x) != id(y)
assert x == y

# Two lists with different elements of the same type,

print('Example 88:')

x = ["a", "b"]
y = ["a", "c"]
assert x != y

# Two lists with elements of the same type with different number of
# elements,

print('Example 89:')

x = ["a", "b", "c"]
y = ["a", "c"]
assert x != y

# Two lists with elements of different types,

print('Example 90:')

x = ["a", "b"]
y = [1, 2]
assert x != y

# Iterating lists
# ~~~~~~~~~~~~~~~

# Lists are iterable objects so you can use them in contexts where an
# iterable object is valid. In particular, you can use a list as the
# iterable in a ``for`` loop. In the following example a ``for`` loop
# is used to iterate over a list of integers to produce the sum of its
# elements,

print('Example 91:')

x = [1, 2, 3]; sum = 0

for item in x:
    sum = sum + item

assert sum == 6

# You can't iterate over a list and modify the list at the same time.

# You can, of course, use the traditional method of iterating using a
# ``while`` statement,

print('Example 92:')

x = [1, 2, 3]; i = 0; sum = 0

while i < len(x):
    sum = sum + x[i]
    i = i + 1

assert sum == 6

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