"""The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers."""


a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
print(a + b)
print(a - b)
print(a * b)

"""The provided code stub reads two integers, a and b, from STDIN. Add logic to print two lines. The first line should contain the result of integer division,  a//b . The second line should contain the result of float division,  a/b ."""
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a // b)
print(a / b)

"""The provided code stub reads an integer, n, from STDIN. For all non-negative integers i < n, print i^2."""
if __name__ == '__main__':
    n = int(input())
for i in range(n):
    print(i * i)

"""Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function."""
year = int(input("Your Year:"))

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap
print(is_leap(year))

if __name__ == '__main__':
    n = int(input("Number for Weird or Not Weird:").strip())

if n%2!=0:
    print("Weird")
elif n%2==0:
    if 2<=n<=5:
        print("Not Weird")
    elif 6<=n<=20:
        print("Weird")
    elif n>20:
        print("Not Weird")

"""The included code stub will read an integer, n, from STDIN.
Without using any string methods, try to print the following: 123...n
Note that "" represents the consecutive values in between."""
if __name__ == '__main__':
    n = int(input())
for i in range(1, n + 1):
    print(i, end='')

print("/n")

#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    max_score = max(arr)
    arr.remove(max_score)
    runner_up = max(arr)
    print(runner_up)

#Given the names and grades for each student in a class, you are required to find the average of their scores. Then, you need to print the name of the student with the highest average score.
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split() #*unpacks the rest of the line into a list and .split splits the input by whitespace
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        average = sum(student_marks[query_name]) / len(student_marks[query_name])
        print(f"{average:.2f}") #f string formatting to 2 decimal places
    else:
        print("Student not found")
