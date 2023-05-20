Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#program that checks whether a given number is odd or even
num=float(input('Enter the number : '))
Enter the number : 96
remainder=num%2
if(remainder==0):
    print(num,"is a even number")
else:
    print(num,"is a odd number")

    
96.0 is a even number

#program to calculate circumference or perimetet of circle based on choices
radius=float(input("enter the radius : "))
enter the radius : 9.5
print("1.Calculate the area of the circle : ")
1.Calculate the area of the circle : 
print("2.Calculate the perimeter of the circle : ")
2.Calculate the perimeter of the circle : 
choice=int(input('enter the choice(1 or 2): '))
enter the choice(1 or 2): 2
if(choice==1):
    area=3.142*radius*radius
    print('area of circle is',area)
else:
    perimeter=2*3.142*radius
    print('perimeter of circle is',perimeter)

    
perimeter of circle is 59.698
#print absolute value of a number
num=int(input('enter the number: '))
enter the number: -93
enter the number: 65
if(num>0):
    print('number is positive')
elif(num==0):
     print('number is zero')
elif(num<0):
    print('number is negative')
else:
    print('invalid entry')
    
SyntaxError: invalid syntax

num=int(input('enter the number: '))
enter the number: -93
>>> if(num>0):
...     print('number is positive')
... elif(num==0):
...      print('number is zero')
... elif(num<0):
...     print('number is negative')
... else:
...     print('invalid entry')
... 
...     
number is negative
>>> 
>>> 
>>> subj1=float(input('enter the number: '))
enter the number: 43.8
>>> subj2=float(input('enter the number 2: '))
enter the number 2: 68.0
>>> subj3=float(input('enter the number 3: '))
enter the number 3: 77.0
>>> marks=(subj1+subj2+subj3)/3
>>> if(marks>=80.0):
...     print('grade A')
... elif(marks<=79.0 and marks>=70.0):
...     print('grade B')
... elif(marks<=69.0 and marks>=60.0):
...     print('grade C')
... elif(marks<=59.0 and marks>=50.0):
...     print('grade D')
... elif(marks<=49.0 and marks>=40.0):
...     print('grade E')
... elif(marks<=39.0):
...     print('Remedial standards')
... else:
...     print('enter a valid number')
... 
...     
grade C
>>> marks
62.93333333333334
