"""

Number 1 -

Question -
What is the result of the code, and explain?

X = 'iNeuron'

def func():

print(X)

func()

Answer -
The line, func() Call the function we defined which prints the value of X.

X = 'iNeuron'
def func():
    print (X)
func()
iNeuron
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 2 -

Question -
What is the result of the code, and explain?

X = 'iNeuron'

def func():

X = 'NI!'

func()

print(X)

Answer -
The line, func() Call the function we defined, with "NI" as the value of X inside the funtion, but doesn't prints it, as there is no print statement inside the function.

The line, print(X), prints the value of X, which is "iNeuron", which is outside func().

X = 'iNeuron'
def func():
    X = 'NI!'
func()
print(X)
iNeuron
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 3 -

Question -
What does this code print, and why?

X = 'iNeuron'

def func():

X = 'NI'

print(X)

func()

print(X)

Answer -
The line, func() Call the function we defined which prints the value of X, which is "NI" inside the funtion.

The line, print(X), prints the value of X, which is "iNeuron", which is outside func().

X = 'iNeuron'
def func():
    X = 'NI!'
    print (X)
func()
NI!
print(X)
iNeuron
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 4 -

Question -
What output does this code produce? Why?

X = 'iNeuron'

def func():

global X

X = 'NI'

func()

print(X)

Answer -
The line, func() Call the function we defined, with "NI" as the value of X inside the funtion, but doesn't prints it, as there is no print statement inside the function, and we have used global keyword, which means, global keyword allows us to modify the variable, that is "X", outside of the current function.

The line, print(X), prints the value of X, which is now "NI", as we used global keyword inside the function.

X = 'iNeuron'
def func():
    global X
    X = "NI"
func()
print(X)
NI
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 5 -

Question -
X = 'iNeuron'

def func():

X = 'NI'

def nested():

print(X)

nested()

func()

X

Answer -
X = 'iNeuron'
def func():
    X = "NI"
def nested():
    print(X)
nested()
iNeuron
func()
X
'iNeuron'
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 6 -

Question -
def func():

X = 'NI'

def nested():

nonlocal X

X = 'Spam'

nested()

print(X)

func()

Answer -
The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.Use the keyword nonlocal to declare that the variable is not local.

def func():
    X = 'NI'
    def nested():
        nonlocal X
        X = 'Spam'
    nested()
print(X)
iNeuron
func()
print(myfunc1())
hello
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


"""