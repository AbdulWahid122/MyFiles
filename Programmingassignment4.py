"""
1.write a program to find factorial of a number?
num=int(input('Enter a nummber: '))

factorial=1

if num<0:
    print('factorial does not exist')

elif num==0:
    print('factorial of 0 is 1')    

else:
    for i in range(1,num+1):    

        factorial=factorial*i

print('The factorial of',num,'is',factorial)


2.Write a Python Program to Display the Multiplication Table?


num=int(input('Display multiplicatin of? '))

for i in range(1,11):
    print(num,'*',i,'=',num*i)


3.Write a Python Program to Printthe Fibonacci sequence?

 #Program to display the Fibonacci Sequence up to n-th term

nterms=int(input("How many terms? "))

#first two terms

n1,n2=0,1

count=0

#check if the number of terms is valid

if nterms<=0:
    print('Please enter a positive integer')

#if there is only one term, return n1

elif nterms==1:
    print('Fibonacci sequence upto',nterms,':')
    print(n1)

#generate fibonacci sequence

else:
    print('Fibonacci sequence: ')
    while count<nterms:
        print(n1)
        nth=n1+n2
        #update values

        n1=n2
        n2=nth

        count+=1

4.Write a python program to check armstrong number?
# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


5. Write a Python Program to Find Armstrong Number in an Interval?

# Program to check Armstrong numbers in a certain interval

lower = 100
upper = 2000

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)


6. Write a Python Program to Find the Sum of Natural Numbers?       

# Sum of natural numbers up to num

num = 16

if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)

"""






























