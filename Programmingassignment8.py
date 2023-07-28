'1. Write a Python Program to Add Two Matrices?'
'''
def matrices(m,n):
    o=[]
    for i in range(m):
        row=[]
        for j in range(n):
            inp=int(input(f'Enter o{i}{j}'))
            row.append(inp)
        o.append(row)
    return o

def add(A,B):

    output=[]
    for i in range(len(A)):
        row=[]
        for j in range(len([A][0])):
            row.append(A[i][j]+B[i][j])
        output.append(row)
    return output

m=int(input('Enter value of m: '))
n=int(input('Enter value of n: '))

print('Enter the matrix A: ')
A=matrices(m,n)

print(A)

print('Enter the matrix B: ')

B=matrices(m,n)

print(B)

s=add(A,B)

print(s)

'''

# Program to multiply two matrices using nested loops


# 3x3 matrix
'''
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:

    print(r)

'''

'''
3. Write a Python Program to Transpose a Matrix?

# Program to transpose a matrix using a nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)
'''

'''
4. Write a Python Program to Sort Words in Alphabetic Order?


# Program to sort alphabetically the words form a string provided by the user

my_str = "Hello this Is an Example With cased letters"

# To take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)


'''

'''
5. Write a Python Program to Remove Punctuation From a String?
# define punctuation
punctuations = ''''''!()-[]{};:'"\,<>./?@#$%^&*_~''''''

my_str = "Hello!!!, he said ---and went."

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)

'''

