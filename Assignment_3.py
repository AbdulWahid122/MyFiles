""""
1. Why are functions advantageous to have in your programs?

Functions reduce the need for duplicate code. This makes programs shorter, easier to read,
and easier to update.



2. When does the code in a function run: when it is specified or when it is called?

When it is called.




3. What statement creates a function?

The “def” keyword is a statement for defining a function in Python.



4. What is the difference between a function and a function call?

A function is a block of code that does a particular operation and returns a result. 
It usually accepts inputs as parameters and returns a result.
Once a function is created in Python, we can call it by writing function_name() itself.



5. How many global scopes are there in a Python program? How many local scopes?

There are two types of variable present in the python:
Local Variable and Global Variable:
Local Variable: A variable created inside a function belongs to the local scope of that function, # and can only be used inside that function.
Example
A variable created inside a function is available inside that function:
def myfunc():
  x = 300
  print(x)

myfunc()


Global Variable:A variable created in the main body of the Python code is a global variable and 
belongs to the global scope.
Global variables are available from within any scope, global and local.


6. What happens to variables in a local scope when the function call returns?

It will return the value of a variable.



7. What is the concept of a return value? Is it possible to have a return value in an expression?

The return keyword is to exit a function and return a value, Yes it is possible to return value in 
expression.
return will give you datatype as it is, while print will give you in Nonetype.


8. If a function does not have a return statement, what is the return value of a call to 
that function?

None


9. How do you make a function variable refer to the global variable?

By using global keyword

def myfunc():
  global x  
  x=300  
myfunc()
print(x)


10. What is the data type of None?

<class 'NoneType'>


11. What does the sentence import areallyourpetsnamederic do?

That will import a module named areallyourpetsnamederic.


12. If you had a bacon() feature in a spam module, what would you call it after importing spam?

spam.bacon()


13. What can you do to save a programme from crashing if it encounters an error?

We will perform exception handling.add()


14. What is the purpose of the try clause? What is the purpose of the except clause?

we can pass code in try clause on which we have a doubt that we can get an error,
And in expect clause we can pass an error.
For example:

a=10
b=0
try:
  c=a/b
  print(c)

except:
  print("b should not be zero")

  





"""