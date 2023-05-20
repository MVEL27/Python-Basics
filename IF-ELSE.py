Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# accept marked price from the user and calculate the net amount
marked_price=int(input('enter the price: '))
enter the price: 9000
if(marked_price<=7000):
    net_amount=marked_price-(marked_price*0.10)
    print('the net amount is: ',net_amount)
elif(marked_price>7000 and marked_price<=10000):
    net_amount=marked_price-(marked_price*0.15)
    print('the net amount is: ',net_amount)
elif(marked_price>10000):
    net_amount=marked_price-(marked_price*0.20)
    print('the net amount is: ',net_amount)
else:
    print('enter a valid input')

    
the net amount is:  7650.0
marked_price=int(input('enter the price: '))
enter the price: 8700
if(marked_price<=7000):
    net_amount=marked_price-(marked_price*0.10)
    print('the net amount is: ',net_amount)
elif(marked_price>7000 and marked_price<=10000):
    net_amount=marked_price-(marked_price*0.15)
    print('the net amount is: ',net_amount)
elif(marked_price>10000):
    net_amount=marked_price-(marked_price*0.20)
    print('the net amount is: ',net_amount)
else:
    print('enter a valid input')

    
the net amount is:  7395.0
# 
# if statement tests a condition and if the condition evaluates to be true
# it carries out some instructions and does nothing in case condition evaluates to be false

# if else tests a condition and if the condition evaluates to true, it carries out statements
# below if  and in case condition evaluates to false, it carries out statements

#allow vehicles
sales=10000
if(sales>7000):
    print('discount is: ',discount=sales*0.10)
else:
      print('discount is: ',discount=sales*0.05)

      
Traceback (most recent call last):
  File "<pyshell#24>", line 2, in <module>
    print('discount is: ',discount=sales*0.10)
TypeError: 'discount' is an invalid keyword argument for print()
sales=10000
if(sales>7000):
    discount=sales*0.10
    print(discount)
else:
    discount=sales*0.05
    print(discount)

    
1000.0
sales=9368
if(sales>7000):
    discount=sales*0.10
    print(discount)
else:
    discount=sales*0.05
    print(discount)

...     
936.8000000000001
>>> # program to test the divisibilty of one number by another number
>>> num_1=int(input('enter the 1st no: '))
enter the 1st no: 66
>>> num_2=int(input('enter the 2nd no: '))
enter the 2nd no: 33
>>> remainder=num_1%num_2
>>> if(remainder==0):
...      print('number1 is divisible by number2')
... else:
...     print('number1 is not divisible by number2')
... 
...     
number1 is divisible by number2
>>> 
>>> num_1=int(input('enter the 1st no: '))
enter the 1st no: 83
>>> num_2=int(input('enter the 2nd no: '))
enter the 2nd no: 7
>>> if(remainder==0):
...      print('number1 is divisible by number2')
... else:
...     print('number1 is not divisible by number2')
... 
...     
number1 is divisible by number2
>>> num_1=int(input('enter the 1st no: '))
enter the 1st no: 83
>>> num_2=int(input('enter the 2nd no: '))
enter the 2nd no: 7
>>> remainder=num_1%num_2
>>> if(remainder==0):
...      print('number1 is divisible by number2')
... else:
...     print('number1 is not divisible by number2')
... 
...     
number1 is not divisible by number2
