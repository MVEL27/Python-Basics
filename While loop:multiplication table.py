Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# While loop
x=0
while(x<10):
    print(x)
    x+=1

    
0
1
2
3
4
5
6
7
8
9
x=10
while(x>0):
    print(x)
    x-=1

    
10
9
8
7
6
5
4
3
2
1
count=1
number=int(input('enter the number: '))
enter the number: 9
while(count<=15):
    product=number*count
    print(number,"*",count,"=",product)
    count+=1

    
9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
9 * 10 = 90
9 * 11 = 99
9 * 12 = 108
9 * 13 = 117
9 * 14 = 126
9 * 15 = 135
>>> # program to find cubes of numbers upto 8
>>> n=1
>>> while(n<9):
...     print('the cube of ',n,'is',n*n*n)
...     n+=1
... 
...     
the cube of  1 is 1
the cube of  2 is 8
the cube of  3 is 27
the cube of  4 is 64
the cube of  5 is 125
the cube of  6 is 216
the cube of  7 is 343
the cube of  8 is 512
>>> 
>>> # program to print even numbers upto 20
>>> i=0
>>> while(i<=20):
...     i+=1
...     if(i%2==0):
...         print(i)
... 
...         
2
4
6
8
10
12
14
16
18
20
