Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#comment
type(x)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    type(x)
NameError: name 'x' is not defined
x=10
type(x)
<class 'int'>
x=10.23
type(x)
<class 'float'>
Type(x)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    Type(x)
NameError: name 'Type' is not defined. Did you mean: 'type'?
.x=10
SyntaxError: invalid syntax
_x=10
type(_x)
<class 'int'>
My=53
type(My)
<class 'int'>
y="murugavel"
type(y)
<class 'str'>
# type() is built in method which informs the type of value
 y=10.56
 
SyntaxError: unexpected indent
.y=9
SyntaxError: invalid syntax
9=9
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
9=i
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
0=x
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
x=10
y=20
sum=x+y
sum
30
tot=sum
tot
30
f=tot
f
30
id(x)
4321125832
id(y)
4321126152
print(sum)
30
print(x)
10
id(sum)
4321126472
id(30)
4321126472
id(tot)
4321126472
id(f)
4321126472
n='hello good morning'
Print(n)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    Print(n)
NameError: name 'Print' is not defined. Did you mean: 'print'?
print(n)
hello good morning
type(n)
<class 'str'>
m="""Anderson"""
print(m)
Anderson
o=m+n
print(o)
Andersonhello good morning
m=""" Anderson"""
o=n+m
print(o)
hello good morning Anderson
type(o)
<class 'str'>
str=
SyntaxError: incomplete input
str=?
SyntaxError: incomplete input
str='change is permanent'
type(str)
<class 'str'>
print(str)
change is permanent
z="""known is a drop
      unknown is a ocean"""
print(z)
known is a drop
      unknown is a ocean
z="known is a drop,
SyntaxError: incomplete input
z="known is a drop,
SyntaxError: incomplete input
z="known is a drop
SyntaxError: incomplete input
z
'known is a drop\n      unknown is a ocean'
'known is a drop\n      unknown is a ocean'
'known is a drop\n      unknown is a ocean'

z="""known is a drop,
unknown is an ocean"""
z
'known is a drop,\nunknown is an ocean'
print(z)
known is a drop,
unknown is an ocean
z="""known is a drop,
 "this is a sample example to illsustrate srting literate"
  unkown is an ocean"""
print(z)
known is a drop,
 "this is a sample example to illsustrate srting literate"
  unkown is an ocean
type(z)
<class 'str'>
z
'known is a drop,\n "this is a sample example to illsustrate srting literate"\n  unkown is an ocean'
str
'change is permanent'
id?
SyntaxError: incomplete input
id?
SyntaxError: incomplete input
type?
SyntaxError: incomplete input
id=?
SyntaxError: incomplete input
typr
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    typr
NameError: name 'typr' is not defined. Did you mean: 'type'?
type
<class 'type'>
id
<built-in function id>
print
<built-in function print>
\\
SyntaxError: unexpected character after line continuation character
\
  \
\
g="\\"
SyntaxError: unexpected indent
g=\\
SyntaxError: unexpected character after line continuation character
g=\
type(g)
Traceback (most recent call last):
  File "<pyshell#88>", line 2, in <module>
    type(g)
NameError: name 'g' is not defined

\r
SyntaxError: unexpected character after line continuation character
x=\r
SyntaxError: unexpected character after line continuation character
Text='hello
SyntaxError: incomplete input
z='my name is,\
khan'
z
'my name is,khan'
z='my name is\
... Khan'
>>> z
'my name isKhan'
>>> z='my name is\
...  Khan'
>>> z
'my name is Khan'
>>> print(z)
my name is Khan
>>> text='''known is a drop
...  unknown
...   is a ocean'''
>>> text
'known is a drop\n unknown\n  is a ocean'
>>> print(text)
known is a drop
 unknown
  is a ocean
>>> size(text)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    size(text)
NameError: name 'size' is not defined. Did you mean: 'slice'?
>>> bit(text)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    bit(text)
NameError: name 'bit' is not defined. Did you mean: 'bin'?
>>> bin (text)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    bin (text)
TypeError: 'str' object cannot be interpreted as an integer
>>> bin(text)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    bin(text)
TypeError: 'str' object cannot be interpreted as an integer
>>> bin(z)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    bin(z)
TypeError: 'str' object cannot be interpreted as an integer
>>> 'abc'
'abc'
>>> len(text)
37
>>> text='\abc'
>>> len(text)
3
