print("My name is Yuvraj.", "My age is 17.")
#Using ',' after one sentence, it will print the next one in the same line.
print(35+98)
#Identation is important.
name="Yuvraj"
age=17 
price=37.99
#The above are variables. Only left side can be used for printing the right side not vice versa.
print(name, age, price)
print("My name is :", name)
#For printing variables, do not use "".

print(type(name))
print(type(price))
print(type(age))      
#Type shows the data type of your command.

name1="Mikky"
name2='Mikky'
name3='''Mikky'''
#Can use any of the above for defining variables even for a same constant.
print(name1)
print(name2)
print(name3)

old=False
a=None
b=1.44
print(type(old))
print(type(a))
print(type(b))
#The keywords(functions and data type) cannot be used as identifier. It is also case sensitive.

c=2
d=6
sum=c+d
print(sum)
diff=c-d
print(diff)

#'#' only for single line comment. '"""' for multiline comment.

#Arithmetic op..
print(c+d)
print(c/d)
print(c*d)
print(c-d)
print(c%d) #shows remainder
print(c**d) #c^d

#relational op..
print(c==d) #equal
print(c!=d) #not equal
print(c>=d)

#Assingment op..(=,+=,-=,*=,/=,%=,**=)
num=10
num*=10
print(num)

#Logical op..(not, and, or)
print(not True)
print(not (c>d))

val1=True
val2=False
print("AND operator:", val1 and val2) #And operator works on 2 values. Gives True when both values are true otherwise False.
print("AND operator", (c==d) and (c<=d))
print("OR operator", val1 or val2) #OR operator works on 2 values. Gives True even if or when one value is true otherwise False.
print("OR operator", (c==d) or (c<=d))

#Type conversion
#Automatic
e=2
f=4.35
g="2" #Using "" made 2 a string and now g cannot be added.
sum1=e+f
print(sum1)
#casting
h=int("2")
sum3=h+f
print(sum3)
print(type(h))
i=str(6)
print(type(i))
print(i)

#Input function makes user put an information after being coded i.e. after you run the program.
name4=str(input("enter your name: "))#Always be a string result.
print("Welcome",name4)
val=int(input("Enter your age:"))#Now will only take integer value for an input by user.
print(type(val), val)

#Prac1: WAP to input 2 numbers & print their sum.

number1=int(input("Enter the first value:"))
number2=int(input("Enter the second value:"))
print("sum=",number1+number2)

#Prac2: WAP to input side ofa square &print its area.

side= float(input("Enter the length of the side of a square:"))
print("Area of the given square of side", side, "is:", side**2)

#Prac3: WAP to input 2 floating point numbers & print their average.

Numb1= float( input("Enter the first value:"))
Numb2= float( input("Enter the second value:"))
print("Average of", Numb1, "and", Numb2, "is:", (Numb1+Numb2)/2)

#Prac4: WAP to input 2 int numbers. Print True if first is greater than or equal to second. If not print False.

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print(a>=b)