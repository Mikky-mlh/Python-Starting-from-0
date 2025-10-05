str1="This is how you write two sentences in consecutive lines. \nUsing revrese slash n."
print(str1)
#\t is fpr tab. Concatenation between strings can be used with +. len function counts how many objects are there including space.
print(len(str1))

#Indexing: Every object ina string is indexed from 0 to infinite. You can print each object through str[number] command.
print(str1[3])

#Slicing: Accesing parts of a string: str[starting_idx:ending_idx]. Ending_idx if left blank would just run through the entirity of string and vice versa.
str="Old is Gold."
print(str[1:4])
print(str[ :4])
print(str[1: ])
#Negative slicing starts at the end of string with -1
print(str[-10:-1])

#String Functions
print(str.endswith("ge"))
print(str.capitalize())
print(str.replace("Old", "New"))
print(str.find("is"))
print(str.count("is"))

#Prac1: WAP to input user's first and print its length.
Name1=input("Enter your first name:")
print("Welcome", Name1, len(Name1))

#Prac2: WAP to find the occurence of $ in a string.
str2="$ is a big currency."
print(str2.count("$"))

#Conditional Statements
#1. if-elif-else
Light=input("Colour of the light:")
if(Light=="Red"):
    print("STOP")
elif(Light=="Yellow"):
    print("WAIT")
elif(Light=="Green"):#elif=else-if. Else only works if 'if' is False
    print("GO")
else: #No need to specify.
    print("Light is broken")

Marks=float(input("Enter your marks out of 100:"))
if(Marks >= 90):
    print("Grade: A")
elif(Marks >=80<90):
    print("Grade: B")
elif(Marks >=70<80):
    print("Grade: C")
elif(Marks >=50<70):
    print("Grade: D")
elif(Marks >=30<50):
    print("Grade: E")
elif(Marks <30):
    print("Grade: F")

#Nesting
age=int(input("Enter your age:"))
if(age>=18):
    if(age>=75):
        print("Cannot drive.")
    else:
        print("Can drive.")
else:
    print("Cannot drive.")

#Prac3: WAP to check if a number entered by the user is odd or even.
num=int(input("Enter your number:"))
rem=num%2
if(rem==0):
    print("EVEN")
else:
    print("ODD")

#Prac4: WAP to find the greatest of 3 numbers entered by the user.
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))

if(a>=b and a>=c):
    print("First number is largest", a)
elif(b>=c):
    print("Second number is largest", b)
else:
    print("Third number is largest", c)

#Prac5: WAP to check if a number is a multiple of 7 or not.

num1=int(input("Enter your number:"))
rem=num1%7
if(rem==0):
    print("DIVISIBLE")
else:
    print("NOT DIVISIBLE")