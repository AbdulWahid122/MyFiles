"""
1.Write a python program to check if a number is positive,negative or zero?

num=float(input('Enter the number:  '))

if num>0:
    print("Number is positive")

elif num==0:
    print('Number is zero')

else:
    print('Number is Negative') 


2.Write a python program to check if a number is odd or even?

num=float(input("Enter a number: "))

if num%2==0:
    print("Number is even")

else:
    print("Number is odd")


3.Wrtie a python program to check leap year?


year=float(input('Enter year: '))

if year%4==0 and year%100!=0 or year%400==0: 

     print(year,'is a leap year.')

else:
    print(year,'is not a leap year')    


4.Write a program to check prime number?

num=int(input('Enter a number: '))

for i in range (2,num):
    if num%i==0:
        print('Number is not a prime')
        break

else:
    print("Number is prime")


5.write  a python to print all prime numbers in an interval of 1-10000?

lower=1
upper=1000

print('prime number between',lower,'and',upper,'are')

for num in range (lower,upper+1):

    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)

"""

