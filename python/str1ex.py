Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> s1 = 'hello'
>>> 
>>> x = iter(s1)
>>> 
>>> print(next(x))
h
>>> print(next(x))
e
>>> print(next(x))
l
>>> print(next(x))
l
>>> print(next(x))
o
>>> 
>>> 
>>> for i in s1:
...     print(i)
