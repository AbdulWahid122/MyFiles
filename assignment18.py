"""
Number 1 -

Question -
Create a zoo.py file first. Define the hours() function, which prints the string 'Open 9-5 daily'. Then, use the interactive interpreter to import the zoo module and call its hours() function.

Answer -
import zoo
zoo.hours()
Open 9-5 daily
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 2 -

Question -
In the interactive interpreter, import the zoo module as menagerie and call its hours() function.

Answer -
import zoo as menagerie
menagerie.hours()
Open 9-5 daily
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 3 -

Question -
Using the interpreter, explicitly import and call the hours() function from zoo.

Answer -
from zoo import hours
hours()
Open 9-5 daily
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 4 -

Question -
Import the hours() function as info and call it.

Answer -
from zoo import hours as info
info()
Open 9-5 daily
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 5 -

Question -
Create a plain dictionary with the key-value pairs 'a': 1, 'b': 2, and 'c': 3, and print it out.

Answer -
plain_dict = {'a': 1, 'b': 2, 'c': 3}
plain_dict
{'a': 1, 'b': 2, 'c': 3}
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 6 -

Question -
Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the same order as plain?

Answer -
from collections import OrderedDict
fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
fancy
OrderedDict([('a', 1), ('b', 2), ('c', 3)])
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 7 -

Question -
Make a default dictionary called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and append the value 'something for a' to it in one assignment. Print dict_of_lists['a'].

Answer -
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
dict_of_lists['a']
['something for a']
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



"""