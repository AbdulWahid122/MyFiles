'''
1. What exactly is []?

This is list.


2. In a list of values stored in a variable called spam, how would you assign the value &#39;hello&#39; as the
third value? (Assume [2, 4, 6, 8, 10] are in spam.)

spam=[2, 4, 6, 8, 10]
spam.insert(2,"hello")
print(spam)

Let's pretend the spam includes the list ['a','b','c','d'] 
for the next three queries.

3. What is the value of spam[int(int('3'* 2) / 11)]?
['a', 'b', 'c', 'd']


4. What is the value of spam[-1]?
d

5. What is the value of spam[:2]?
['a', 'b']


Let's pretend bacon has the list [3.14,"cat",11,"cat", True] 
for the next three questions.

6. What is the value of bacon.index("cat")?
1

7. How does bacon.append(99) change the look of the list value in bacon?

[3.14, 'cat', 11, 'cat', True, 99]


8. How does bacon.remove("cat") change the look of the list in bacon?

[3.14, 11, 'cat', True]


9. What are the list concatenation and list replication operators?

Concatenation:  Concatenation with list.
Operator is +

Example:
l1=[1,2]
l2=[3,4]
a=l1+l2
print(a)


Replication: Replication with list
The repetition operator * will make multiple copies of that particular object and 
combines them together.

Operator is *

Example:
l1=[1,2]
a=l1*2
print(a)



10. What is difference between the list methods append() and insert()?

append() will add element at last in the list.

l=["cat","dog","cow","goat"]
l.append("tiger")
print(l)


insert() will add element at the desired index in the list.

l=["cat","dog","cow","goat"]
l.insert(1,"snake")
print(l)

11. What are the two methods for removing items from a list?

List.remove()
List.pop()

Example:
l=["cat","dog","cow","goat"]

l.remove("dog")
print(l)

l.pop()
print(l)


12. Describe how list values and string values are identical.
The similarity between Lists and Strings in Python is that both are sequences. The differences 
between them are that firstly, Lists are mutable but Strings are immutable. Secondly, elements of 
a list can be of different types whereas a String only contains characters that are all of 
String type.


13. What's the difference between tuples and lists?

tuple is denoted by ()

list is denoted by []

tuple is immutable.
list is mutable.

Type of list is <class 'list'>

Type of tuple is <class 'list'>



14. How do you type a tuple value that only contains the integer 42?

p=tuple([42])




15. How do you get a list value's tuple form? How do you get a tuple value's list form?

list value's tuple form:

l=[4,5,"cat"]
t=tuple(l)
print(t)
print(type(t))


tuple value's list form:

t=(4,5,"cat")
l=list(t)
print(l)
print(type(l))



16. Variables that contains list values are not necessarily lists themselves. Instead, what do they
contain?

They contain references to list values.


17. How do you distinguish between copy.copy() and copy.deepcopy()?

The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will 
do a deep copy of a list. That is, only copy.deepcopy() will duplicate any lists inside the list.

'''