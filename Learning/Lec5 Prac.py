#Prac4: Print the sum of numbers from 1 to n using a while loop.
n=int(input("Enter a number to calculate the sum from 1 to n: "))  
sum=0
i=1
while i<=n:
    sum += i  # Add the current value of i to sum
    i += 1    # Increment i by 1
print("The sum of numbers from 1 to", n, "is:", sum)

#Prac5: Print the factorial of n using a while loop.
n=int(input("Enter a number to calculate the factorial: "))
factorial=1
i=1
while i<=n:
    factorial *= i  # Multiply the current value of factorial by i
    i += 1          # Increment i by 1
print("The factorial of", n, "is:", factorial)

#Prac6: Print the Fibonacci series up to n terms using a while loop.
n=int(input("Enter the number of terms for Fibonacci series: "))
a, b = 0, 1
count = 0
while count < n:
    print(a, end=' ') # end=' ' ensures the output is on the same line
    a, b = b, a + b  # Update a and b for the next term
    count += 1  # Increment the count

#Prac7: Check if a number is prime using a while loop.
n = int(input("Enter a number to check if it is prime: "))
is_prime = True
if n <= 1:
    is_prime = False  # Numbers less than or equal to 1 are not prime
i = 2
while i * i <= n:  # Check divisibility up to the square root of n
    if n % i == 0:
        is_prime = False  # If n is divisible by i, it is not prime
        break # Exit the loop if a divisor is found
    i += 1  # Increment i to check the next number
if is_prime:
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")

#Prac8: Count the number of digits in a number using a while loop.
n = int(input("Enter a number to count its digits: "))             
count = 0
if n == 0: 
    count = 1  # Special case for 0, which has 1 digit
while n > 0:
    n //= 10  # Remove the last digit from n
    count += 1  # Increment the count for each digit removed   
print("The number of digits is:", count)

#Prac9: Reverse a number using a while loop.
n = int(input("Enter a number to reverse it: "))    
reversed_number = 0
while n > 0:
    digit = n % 10  # Get the last digit of n
    reversed_number = reversed_number * 10 + digit  # Build the reversed number
    n //= 10  # Remove the last digit from n
print("The reversed number is:", reversed_number)

#Prac10: Find the largest digit in a number using a while loop.
n = int(input("Enter a number to find the largest digit: "))    
largest_digit = 0
while n > 0:
    digit = n % 10  # Get the last digit of n
    if digit > largest_digit:
        largest_digit = digit  # Update largest_digit if the current digit is larger
    n //= 10  # Remove the last digit from n
print("The largest digit is:", largest_digit)

#Example of Nested Loops:
print("Example of Nested Loops:")
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"i = {i}, j = {j}")
    print("End of inner loop for i =", i)  # This will execute after the inner loop completes for each i

