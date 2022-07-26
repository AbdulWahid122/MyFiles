""" 

Ans1) Two values of boolean data type are True and False, Example

Print(bool(0))
False

Print(bool(1))
True

***********************************

Ans2) Three different types of boolean operators are 
  
 AND, OR, NOT 

"and" operator will check for both the condition to be true. 

"or" operator will check for either of the condition to get true.

"not" will check to be not equal to something

These are used in conditions.

********************************************

3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean
values for the operator and what it evaluate ).

F is false
T is True
After arrow what it gives

for "and"

F F  -->  F 
F T  -->  F  
T F  -->  F  
T T  -->  T

for "or"

F F --> F 
F T --> T
T F --> T
T T --> T
  
***********************************
4. What are the values of the following expressions?

(5 > 4) and (3 == 5)

a=5
b=4

print(a>b and 3==5)

False

*******************************
not (5 > 4)

False
*****************
(5 > 4) or (3 == 5)

True

************************
not ((5 > 4) or (3 == 5))

False
******************************
(True and True) and (True == False)

False

*********************************
(not False) or (not True) 

True

*************************
 
5. What are the six comparison operators?

==  equals to equals to , 
!=  not equals to, 
<   lesser than,
>   Greater than,
<=  Less than or equals to,
>=  Greater than or equals to,

**********************************

6. How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.
 
Assignment operator is used to assign the value and equals to equals to operator is used to check 
whether the variable is equals to some values or not in the condition. 

a=10
b=10
if a==b:
    print("a is equals to b")
else:
    print("a is not equals to b")
    
**************************************************    
7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print("eggs")
if spam > 5:
print("bacon")
else:
print("ham";)
print("spam")
print("spam")

Ans:

spam = 0
if spam == 10:
    print("eggs")
if spam > 5:
    print("bacon")
else:
    print("ham")
    print("spam")
    print("spam")

*************************************
8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.

spam=2

if spam==1:
    print("Hello")

elif spam==2:
    print("Howdy")

else:
    print("Greeting!")

*************************************


9.If your programme is stuck in an endless loop, what keys you’ll press?

Ctrl+C

*************************************

10. How can you tell the difference between break and continue?

Continue used when we do not want to give any print statement and we do not want any error because 
of that.
Break is used when we want to break the loop after acheiving some condition.
 Both are used in loops.

***********************************

11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

I think every statement is same and having a same output, There is no difference.

*****************************************
12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.

for i in range(1,11):
    print(i)

*********
i=1

while (i<=10):
    print(i)
    i=i+1

*********************
13. If you had a function named bacon() inside a module named spam, how would you call it after
importing spam?

def bacon(name):

    print("Hello",name)
    
import spam

spam.bacon("Wahid")

Output: Hello Wahid

"""

