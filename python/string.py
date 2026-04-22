Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s1 = 'hello'
>>> s1.capitalize()
'Hello'
>>> s1.uper()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s1.uper()
AttributeError: 'str' object has no attribute 'uper'. Did you mean: 'upper'?
>>> s1.upper()
'HELLO'
>>> s1.lower()
'hello'
>>> s1 = "hELLO"
>>> s1.casefold()
'hello'
>>> s1.casefold()
'hello'
>>> s1.count(1)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s1.count(1)
TypeError: count() argument 1 must be str, not int
>>> s1.count("l")
0
>>> s1 = "HELLO"
>>> s1.count("H")
1
>>> s1.endswith("O")
True
>>> s1.find("L")
2
>>> s1.index("O")
4
>>> s1.isdigit()
False
>>> s1.replace("L","*")
'HE**O'
