"""
1.Is the python standard library included with PyInputPlus?
No, We have to install it with pip install PyInputPlus.

2. Why is PyInputPlus commonly imported with import pyinputplus as pyip?
So that you can enter a shorter name when calling the module's functions.

3.How do you distinguish between inputInt() and inputFloat()?
inpputInt() accepts an Integer value and inputFloat() accepts floating point numeric value.

4.Using PyInputPlus,how do you ensure that the user enters a whole number between 9 to 99?
By using pyip.inputint(min=0,max=99)

5.what is transferred to the keyword argumnets allowRegexes and blockRegexes?
A list of regex strings that are either explicitly allowed or denied.

6.If a blank input is entered three times, what does inputStr(limit=3) do?
The function will raise RetryLimitExeption.

7.If blank input is entered three times, what does inputStr(limit=3,default='hello') do?
The function returns the value 'hello'









"""

