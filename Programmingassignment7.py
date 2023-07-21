'1. Write a Python Program to find sum of array?'
'''
arr = [12, 3, 4, 15]

print(sum(arr))
'''


'2. Write a Python Program to find largest element in an array?'
'''
arr = [12, 3, 4, 15,99]

def Large_element(arr):
    return max(arr)

print(Large_element(arr))'''

'3. Write a Python Program for array rotation?'
'''
a=[]

size=int(input('Enter size of the array: '))

for i in range(size):
    val=int(input('Enter values of array: '))
    a.append(val)
    
print('The original list is',a)

n=int(input('Please enter number of rotaion: '))

for count in range(n):

    x=a[0]
    for i in range(1,size):
        a[i-1]=a[i]
    a[size-1]=x
print('List after rotation is',a)
'''
'4. Write a Python Program to Split the array and add the first part to the end?'
'''
def splitArr(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]
 
        arr[n-1] = x
 
 
# main
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
 
splitArr(arr, n, position)
 
for i in range(0, n):
    print(arr[i], end=' ')
'''
'5. Write a Python Program to check if given array is Monotonic?'

'''
# Check if given array is Monotonic
def isMonotonic(A):
    x, y = [], []
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse=True)
    if(x == A or y == A):
        return True
    return False
 
 
# Driver program
A = [6, 5, 4, 4]
 
# Print required result
print(isMonotonic(A))

'''




    
    
    
    
    
    





    