#Functions are a block of statements that perform a specific tasks.
def sum(a,b):
    s=a+b
    return s
print(sum(2,3))
sum(4888,9977)
"""def func_name(var1,var2):
    some work
    return val""" #This saves function as a defined one and can now be reusable.

def average(a,b,c):
    A=(a+b+c)/3
    return A
   
print(average(15,45,52))

#Prac1: WAF to print length of a list.
def length_of_list(list):
    print(len(list))
numbers=[1,2,3,6,5,8,7]
length_of_list(numbers)

#Prac2: WAF to print the elements of a list in a single line.
def line(list):
    for item in list:
        print(item, end=' ')
line(numbers)
print("\n")

#Prac3: WAF to print factorial of a number.
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
n=int(input("Enter a number to find its factorial: "))
print("The factorial of", n, "is", factorial(n))

#Prac4: WAF to convert USD to INR.
def usd_to_inr(usd):
    inr = usd * 82.73
    return inr
usd = float(input("Enter amount in USD: "))
print("Amount in INR:", usd_to_inr(usd))

#Recursion is a process in which a function calls itself directly or indirectly.
def show(n):
    if(n==0):
        return # Base case: if n is 0, return without doing anything
    print(n) # Print n before the recursive call
    show(n-1)  # Recursive call to show with n-1
    print(n)  # Print n after the recursive call

n = int(input("Enter a number for recursion: "))
show(n)

#returns n!
def fact(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    else:
        return n * fact(n - 1)  # Recursive case: n! = n * (n-1)!

n = int(input("Enter a number to find its factorial using recursion: "))
print("The factorial of", n, "is", fact(n))

#Prac5: Write a recursive function to calculate the sum of first n natural numbers.
def sum_natural(n):
    if n == 0:  # Base case: if n is 0, return 0
        return 0
    else:
        return n + sum_natural(n - 1)  # Recursive case: n + sum of first (n-1) natural numbers

n = int(input("Enter a number to calculate the sum of first n natural numbers: "))
print("The sum of first", n, "natural numbers is:", sum_natural(n)) 

#Prac6: Write a recursive function to print all elements in a list.
def print_list_elements(lst):
    if not lst:  # Base case: if the list is empty, return
        return
    print(lst[0])  # Print the first element
    print_list_elements(lst[1:])  # Recursive call with the rest of the list

numbers = [1, 2, 3, 4, 5]
print("Elements in the list are:")
print_list_elements(numbers)