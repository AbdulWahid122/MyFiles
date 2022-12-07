"""
1.Write a python program to convert kiometers to miles?

Kilometer=float(input('Enter a vlue in kilometer:  '))

Miles=0.62137*Kilometer

print('Value of kilometer in miles:{}'.format(Miles))



2.Write a Python program to convert Celsius to Fahrenheit?

Celsius=float(input('Enter value in celsius:  '))

Fehrenheit=((9/5)*Celsius)+32

print('The value of celsius in fehrenheit is:{}'.format(Fehrenheit))


3.Write a python program to display calender?

import calendar

a=int(input('Enter the year:  '))
b=int(input('Enter the month:  '))

print(calendar.month(a,b))

4.Write a Python program to solve quadratic equation?

import cmath

a=1
b=5
c=6

#calculate the discriminant

d=(b**2)-(4*a*c)

#find the solutions

sol1=(-b-cmath.sqrt(d))/(2*a)

sol2=(-b+cmath.sqrt(d))/(2*a)

print('The solutions are {0} and {1}'.format(sol1,sol2))


5.Write a python program to swap two variables without temp variable?

x=9
y=5

x,y=y,x

print('The value of x and y after swap is {0} and {1}'.format(x,y))


"""











