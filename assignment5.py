"""
1. What does an empty dictionary's code look like?

{}

2. What is the value of a dictionary value with the key 'foo' and the value 42?

42

3. What is the most significant distinction between a dictionary and a list?

List is ordered while dictionaries are unordered,
List is having values while dictionary is in the form of key and value pairs.

4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

we'll get an error.

5. If a dictionary is stored in spam, what is the difference between the expressions "cat" in spam and
"cat"; in spam.keys()?


ans: In spam.keys() we will get dict_keys(['cat']).

6. If a dictionary is stored in spam, what is the difference between the expressions "cat" in spam and
"cat" in spam.values()?


ans: we will get value of a cat in dictionary.

7. What is a shortcut for the following code?
if 'color' not in spam:
spam['color'] = 'black'

Ans:

The setdefault() method returns the value of the item with the specified key.If the key 
not exist, insert the key, with the specified value.

example:

spam={"Name":"wahid","age":25,"status":"Unmarried"}

spam.setdefault("color","black")

print(spam)



8.How do you "pretty print" dictionary values using which module and function?

we can make dictionary values more readable and presentable.

we will import json module and function will be json.dumps.

import json
e={"Name":"Ram", "Class":22,"Roll no":21}

print(json.dumps(e,indent=4))

"""



