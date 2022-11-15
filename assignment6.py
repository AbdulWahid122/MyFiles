"""
1. What are escape characters, and how do you use them?

To insert characters that are illegal in a string, use an escape character.
It is a backslash \ followed by the character you want to insert.

2. What do the escape characters n and t stand for?

\n is for new line.
\t is for tab.

s="Hello\nworld"
print(s)


s="Hello\tworld"
print(s)


3. what is the way to include backslash characters in a string?

s='" python\'s owesome" she said'

print(s)

4. The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the
word Howl's not escaped a problem?

Ans: Because it is included in double quote.

s="Howl's Moving Castle"

print(s)

5. How do you write a string of newlines if you don't want to use the n character?
we will write it in a new line.


6. What are the values of a given expressions?

s="Hello, World!"

print(s[1])
ans: e

print(s[0:5])
ans: Hello


print(s[:5])
ans: Hello

print(s[3:])
ans:  lo, World!

7. What are the value of following expressions?

s="Hello"

print(s.upper())
ans: HELLO


print(s.upper().isupper())
True


print(s.upper().lower())
hello

8. What are the values of the following expressions?

s='Remember,remember,the fifth of July.'
print(s.split())
['Remember,remember,the', 'fifth', 'of', 'July.']

print("-".join('There can only one'.split()))
There-can-only-one

9. What string methods can you use to right-justify, left justify, and center a string?


a="Tiger"
b=a.rjust(20)
print(b,"is an animal.")


a="Tiger"
b=a.ljust(20)
print(b,"is an animal.")

a="Tiger"
b=a.center(20)
print(b,"is an animal.")

10. What is the best way to remove whitespace characters from the start and end>

Space,tab,New line etc called white space, It maked code more readable.

s="   this is me."

print(s.lstrip())

print(s.rstrip())
"""






