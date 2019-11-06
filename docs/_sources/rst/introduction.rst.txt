Introduction
============

Welcome to *Python to Learn Python*!

*Python to Learn Python* is a collection of amply documented Python
scripts designed as an introduction to the *core* Python language. You
can think of it as an *executable book*, a book with pages and
chapters consisting of scripts that you can *Read, Run and Review*.

What is Python to Learn Python?
-------------------------------

It is a github public repository located at `Python to Learn Python`_.

It consists of three directories: ``scripts``, ``output`` and
``docs``.

The ``scripts`` directory contains mostly Python scripts, some
reStructuredText documents and very few shell scripts. Python scripts
end with the extension ``.py``, reStructuredText documents end with
``.rst`` and shell scripts with ``.sh``. Most files have a filename
that starts with a numeric prefix to indicate the order in which they
are supposed to be read and worked through. Some of the files are
short and can be thought of as pages in a book but others are too long
to be considered pages so they are better viewed as short chapters.

The ``output`` directory contains the output generated when the
scripts are run at project build time. The output from a script has
the same file name as the script, except it ends with the extension
``.output`` rather than ``.py``. The scripts are run as part of the
project build so the output files are always in sync with the source
code and comments in the corresponding scripts.

The ``docs`` directory contains the html for the github pages
associated with the project which are located at `Python to Learn
Python Pages`_. The html pages are generated from reStructuredText
documents using the `Sphinx tool`_. The reStructuredText documents
themselves are extracted directly from the contents of the scripts
including comments *and* source code. This means the html pages are
always in sync with the scripts.

.. _`Python to learn Python`: https://github.com/ombuvirtual/python-to-learn-python
.. _`Python to Learn Python Pages`: https://ombuvirtual.github.io/python-to-learn-python/
.. _`Sphinx tool`: http://www.sphinx-doc.org/en/master/

