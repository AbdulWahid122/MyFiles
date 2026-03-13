#1. Write a Python program to check if the given number is a Disarium Number?

# Check if a number is Disarium
def is_disarium(n):
    num_str = str(n)
    total = sum(int(digit) ** (i+1) for i, digit in enumerate(num_str))
    return total == n

# Test
num = int(input("Enter a number: "))
if is_disarium(num):
    print(f"{num} is a Disarium Number")
else:
    print(f"{num} is not a Disarium Number")


#2. Write a Python program to print all disarium numbers between 1 to 100?

print("Disarium numbers between 1 and 100:")
for i in range(1, 101):
    if is_disarium(i):
        print(i, end=" ")

#3. Write a Python program to check if the given number is Happy Number?

def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit)**2 for digit in str(n))
    return n == 1

# Test
num = int(input("Enter a number: "))
if is_happy(num):
    print(f"{num} is a Happy Number")
else:
    print(f"{num} is not a Happy Number")

#4. Write a Python program to print all happy numbers between 1 and 100?

print("Happy numbers between 1 and 100:")
for i in range(1, 101):
    if is_happy(i):
        print(i, end=" ")

#5. Write a Python program to determine whether the given number is a Harshad Number?

def is_harshad(n):
    digit_sum = sum(int(digit) for digit in str(n))
    return n % digit_sum == 0

# Test
num = int(input("Enter a number: "))
if is_harshad(num):
    print(f"{num} is a Harshad Number")
else:
    print(f"{num} is not a Harshad Number")

#6. Write a Python program to print all pronic numbers between 1 and 100?

print("Pronic numbers between 1 and 100:")
for i in range(1, 101):
    for j in range(i):
        if j * (j+1) == i:
            print(i, end=" ")
            break