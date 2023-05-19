Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
units=int(input('enter your power consumption: '))
enter your power consumption: 150
if(units<=100):
    print('no charge')
elif(units>100 and units<=200):
    print('Bill amount is 500')
elif(units>200):
    print('bill amount is 2000')
else:
    print('enter a valid input')

    
Bill amount is 500
units=int(input('enter your power consumption: '))
enter your power consumption: 500
if(units<=100):
    print('no charge')
elif(units>100 and units<=200):
    print('Bill amount is 500')
elif(units>200):
    print('bill amount is 2000')
else:
    print('enter a valid input')

    
bill amount is 2000

#write a program to display last digit of a number
num=int(input('enter the number; '))
enter the number; 79
last_digit=num%10
print('last_digit')
last_digit

num=int(input('enter the number; '))
enter the number; 79
last_digit=num%10
print(last_digit)
9

num=int(input('enter the number; '))
enter the number; 68
last_digit=num%10
print(last_digit)
8

#program to check last number is divisible by 3
num=int(input('enter the number; '))
enter the number; 33
if(num%3==0):
    print('number is divisible by 3')
else:
    print('number is not divisible by 3')

    
number is divisible by 3
num=int(input('enter the number; '))
enter the number; 56
if(num%3==0):
    print('number is divisible by 3')
else:
    print('number is not divisible by 3')

    
number is not divisible by 3

#program to accept cost price of a bike & road tax to be paid
cost_price=int(input('enter the price of the bike: '))
enter the price of the bike: 105000
if(cost_price<=50000):
    print('road tax to be paid is= ',cost_price*0.05)
elif(cost_price>50000 and cost_price<=100000):
    print('road tax to be paid is= ',cost_price*0.10)
elif(cost_price>100000):
    print('road tax to be paid is= ',cost_price*0.15)
... else:
...     print('enter a valid entry')
... 
...     
road tax to be paid is=  15750.0
>>> 
>>> #time period of service & bonus
>>> salary=int(input('enter the salary: '))
enter the salary: 18000
>>> service=int(input('enter the years of service: '))
enter the years of service: 9
>>> if(service<6):
...     print('net bonus amount is: ',salasry*0.05)
... elif(service>=6 and service<=10):
...     print('net bonus amount is: ',salasry*0.08)
... elif(service>10):
...     print('net bonus amount is: ',salasry*0.10)
... else:
...      print('enter a valid entry')
... 
...      
Traceback (most recent call last):
  File "<pyshell#61>", line 4, in <module>
    print('net bonus amount is: ',salasry*0.08)
NameError: name 'salasry' is not defined. Did you mean: 'salary'?
>>> salary=int(input('enter the salary: '))
enter the salary: 18000
>>> service=int(input('enter the years of service: '))
enter the years of service: 9
>>> if(service<6):
...     print('net bonus amount is: ',salary*0.05)
... elif(service>=6 and service<=10):
...     print('net bonus amount is: ',salary*0.08)
... elif(service>10):
...     print('net bonus amount is: ',salary*0.10)
... else:
...      print('enter a valid entry')
... 
...      
net bonus amount is:  1440.0
