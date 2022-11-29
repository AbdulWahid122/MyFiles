"""
 Number 1 -

Question -
Create a list called years_list, starting with the year of your birth, and each year thereafter until the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list = [1980, 1981, 1982, 1983, 1984, 1985].

Answer -
years_list = [1996,1997,1998,1999,2000,2001]
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 2 -

Question -
In which year in years_list was your third birthday? Remember, you were 0 years of age for your first year.

Answer -
years_list[2]
1998
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 3 -

Question -
In the years list, which year were you the oldest?

Answer -
years_list[-1]
2001
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 4 -

Question -
Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".

Answer -
things = ['mozzarella','cinderella','salmonella']
things
['mozzarella', 'cinderella', 'salmonella']
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 5 -

Question -
Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?

Answer -
This capitalizes the word, but doesn’t change it in the list:

things_cap = things.copy()
things_cap[1].capitalize()
'Cinderella'
things_cap
['mozzarella', 'cinderella', 'salmonella']
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 6 -

Question -
Make a surprise list with the elements "Groucho," "Chico," and "Harpo."

Answer -
surprise = ['Groucho', 'Chico', 'Harpo']
surprise
['Groucho', 'Chico', 'Harpo']
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 7 -

Question -
Lowercase the last element of the surprise list, reverse it, and then capitalize it

Answer -
surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1].capitalize()
'Oprah'
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 8 -

Question -
Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.

Answer -
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
e2f
{'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 9 -

Question -
Write the French word for walrus in your three-word dictionary e2f.

Answer -
e2f['walrus']
'morse'
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 10 -

Question -
Make a French-to-English dictionary called f2e from e2f. Use the items method.

Answer -
f2e = {}
for english, french in e2f.items():
 f2e[french] = english
f2e
{'chien': 'dog', 'chat': 'cat', 'morse': 'walrus'}
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 11 -

Question -
Print the English version of the French word chien using f2e.

Answer -
f2e['chien']
'dog'
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 12 -

Question -
Make and print a set of English words from the keys in e2f.

Answer -
set(e2f.keys())
{'cat', 'dog', 'walrus'}
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 13 -

Question -
Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.

Answer -
life = {'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'],'octopi': {},'emus': {}},'plants': {},'other': {}}
life
{'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'], 'octopi': {}, 'emus': {}},
 'plants': {},
 'other': {}}
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 14 -

Question -
Print the top-level keys of life.

Answer -
print(life.keys())
dict_keys(['animals', 'plants', 'other'])
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 15 -

Question -
Print the keys for life['animals'].

Answer -
print(life['animals'].keys())
dict_keys(['cats', 'octopi', 'emus'])
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Number 16 -

Question -
Print the values for life['animals']['cats']

Answer -
print(life['animals']['cats'])
['Henri', 'Grumpy', 'Lucy']
-------------------------------------------

"""