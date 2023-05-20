Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# accept number of days from the user & calculate library charges
days=int(input('enter the number of days: '))
enter the number of days: 18
if(days<=5):
    print('total charge is ',days*2)
elif(days>=6 and days<=10):
    print('total charge is ',days*3)
elif(days>=11 and days<=15):
    print('total charge is ',days*4)
elif(days>15):
    print('total charge is ',days*5)
else:
    print('enter a valid entry')

    
total charge is  90
# accept the kilometers covered & calculate charges accordingly
kms=int(input('enter the distance covered: '))
enter the distance covered: 9
if(kms<=10):
    print('the charges are ',kms*11)
elif(kms>10 and kms<=90):
    print('the charges are ',kms*10)
elif(kms>90):
    print('the charges are ',kms*9)
else:
    print('enter a valid entry')

    
the charges are  99
# The given number is of one digited or two digited or three digited or more than three digited
n=int(input('enter the number: '))
enter the number: 888
if(n>0 and n<10):
    print('one digit number')
elif(n>=10 and n<100):
    print('two digit number')
elif(n>=100 and n<1000):
    print('three digit number')
else:
    print('more than three digit number')

    
three digit number
>>> # Electricity bill
>>> uc=int(input('enter the units consumed: '))
enter the units consumed: 279
>>> if(uc<=100):
...     bill_amt=uc*0.5
...     print(bill_amt)
... if(uc>101 and uc<=200):
...     
SyntaxError: invalid syntax
>>> uc=int(input('enter the units consumed: '))
enter the units consumed: 279
>>> if(uc<=100):
...     bill_amt=uc*0.5
...     print(bill_amt)
... elif(uc>101 and uc<=200):
...     bill_amt=50+(uc-100)*1
...      print(bill_amt)
...      
SyntaxError: unexpected indent
>>> uc=int(input('enter the units consumed: '))
enter the units consumed: 279
>>> if(uc<=100):
...     bill_amt=uc*0.5
...     print(bill_amt)
... elif(uc>101 and uc<=200):
...     bill_amt=50+(uc-100)*1
...     print(bill_amt)
... elif(uc>201 and uc<=300):
...     bill_amt=150+(uc-200)*1.5
...     print(bill_amt)
... elif(uc>300):
...     bill_amt=300+(uc-300)*2
...     print(bill_amt)
... else:
...     print('enter a valid entry')
... 
...     
268.5
