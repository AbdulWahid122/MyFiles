'1. Write a Python Program to Display Fibonacci Sequence Using Recursion?'

'''def fabonacci_series(n):
    if n<=1:
        return n
    else:
        return fabonacci_series(n-1)+fabonacci_series(n-2)

n_terms=9

if n_terms<=0:
    print('Please enter valid number')

else:
  for i in range(n_terms):
    print(fabonacci_series(i))'''
    

'*******************************************************'

'2. Write a Python Program to Find Factorial of Number Using Recursion?'
'''
def Recursive_Factorial(n):
    if n==1:
        return n
    else:
        return n*Recursive_Factorial(n-1)

n_terms=10

if n_terms<0:
    print('invalid input')

elif n_terms==0:
    print('Factorial of 0 is 1.')

else:
        print(Recursive_Factorial(n_terms))'''
        
'************************************************************************'

'3. Write a Python Program to calculate your Body Mass Index?'
'''
def Bodymassindex(weight,height):
    return round(weight/height**2,2)

weight=float(input('Enter your weight in kg: '))
height=float(input('Enter your height in meters: '))

print('Your Body Mass Index is',Bodymassindex(weight,height))'''

'******************************************************************************'
'4. Write a Python Program to calculate the natural logarithm of any number?'
'''
def Natural_Log(n):
    import math
    return math.log(n)

num=int(input('Please enter the number: '))


print('Natural log number of the number',num,'is',(Natural_Log(num)))'''

'*************************************************************************************************'


'5. Write a Python Program for cube sum of first n natural numbers?'

'''
def natural_number(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+pow(i,3)

    return sum

n=7

print(natural_number(n))'''