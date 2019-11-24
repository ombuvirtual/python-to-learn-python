# Python to Learn Python module
from inspect import currentframe, getframeinfo

def ln():
    """Gets current line number in source code"""
    return str(currentframe().f_back.f_lineno) + ">"

def l():
    """Gets current line number in source code"""
    return str(currentframe().f_back.f_lineno) + ">"

def pl():
    """Gets current line number in source code"""
    prefix = "\nexample at line "
    lineno = str(currentframe().f_back.f_lineno)
    suffix = ":"
    print(prefix + lineno + suffix)
