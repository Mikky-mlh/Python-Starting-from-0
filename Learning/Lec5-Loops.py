#Loops are used to repeat instructions until a condition is met.
i=1
while i<=10:
    print("Hello World", i)
    i+=1  # Increment the count to avoid an infinite loop.
#The loop will print "Hello World" 10 times.
#After each iteration, count is incremented by 1. If count is not incremented, the loop would run indefinitely. 

j=10
while j>=1:
    print(j)
    j-=1

#Prac1: Print numbers from 1 to 100 using a while loop.
k=1
while k<=100:
    print(k)
    k+=1

#Prac2: Print numbers from 100 to 1 using a while loop.
l=100
while l>=1:
    print(l)
    l-=1

#Prac3: Print the multiplication table of n using a while loop.
n=int(input("Enter a number for multiplication table: "))
m=1
while m<=10:
    print(n, "x", m, "=", n*m)
    m+=1

#Prac4: Print the elements of the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1  # Increment i to move to the next index

#Prac5: Search for a number x in this tuple using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
numbers_tuple = (1, 4, 9, 16, 25, 36, 49, 36, 64, 81, 100)
x = int(input("Enter a number to search in the tuple: "))
i = 0
while i < len(numbers_tuple):
    if numbers_tuple[i] == x:
        print("found at index", i)
    else:
        print("finding....")
    i += 1  # Increment i to check the next element

#Break and Continue statements. 
#Break statement is used to exit the loop prematurely.
#Continue statement is used to skip the current iteration and continue with the next one.

#Example of Break statement:
print("Example of Break statement:")
i=1
while i <= 5:
    print(i)
    if i == 3:
        print("Breaking the loop at i =", i)
        break
    i+= 1

#Example of Continue statement:
print("Example of Continue statement:")
i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue  # Skip the rest of the loop body for this iteration
    print(i)  # This will not execute when i is 3
    i += 1  # Increment i to avoid an infinite loop

#For Loops:
#For loops are used to iterate over a sequence (like a list, tuple, or string
list= [1, 2, 3, 4, 5]
for item in list:
    print(item)  # This will print each item in the list
else:
    print("End of for loop")

#To traverese over a list/tuple we use for loop. But we use while loop to update the value of the variable.
#For loop is used to iterate over a sequence of numbers.

#Range function is used to generate a sequence of numbers, starting from 0 by default, and ending at a specified number. It can also take a step value to specify the increment between each number in the sequence.
for el in range(5):  
    print(el)  # This will print numbers from 0 to 4
for el in range(1, 6):
    print(el)  # This will print numbers from 1 to 5
for el in range(1, 10, 2):
    print(el)  # This will print odd numbers from 1 to 9 (1, 3, 5, 7, 9)  
#range(start, stop, step) generates a sequence of numbers starting from 'start', up to but not including 'stop', with an increment of 'step'.

#Pass statement is a null statement that does nothing. It is used as a placeholder for future code.
for i in range(5):
    pass  # This loop does nothing, but it is syntactically correct.

#Example of Nested Loops:
print("Example of Nested Loops:")
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"i = {i}, j = {j}") #f-string is used for formatted string literals. In this case, it prints the values of i and j in a formatted way.
    print("End of inner loop for i =", i) # This will execute after the inner loop completes for each i