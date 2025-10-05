#OOP: Object-Oriented Programming to deal with real-world problems
# Class: Blueprint for creating objects
# Object: Instance of a class
# Attributes: Variables that belong to the class
# Methods: Functions that belong to the class

class Student:
    college_name = "ABC University"  # Class variable, shared by all instances
    name= "Anonymous"  # Default value for name
    marks = 0  # Default value for marks
    def __init__(self, name, marks):  # Constructor
        self.name = name  # Instance variable
        self.marks = marks
        

    def get_student_info(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}, College: {Student.college_name}")

s1 = Student("John", 85) #object creation
s2 = Student("Jane", 90)  # Another object creation
s1.get_student_info()  # Accessing method of the object
s2.get_student_info()  # Accessing method of another object

#Constructor: A special method that is automatically called when an object is created. All classes have a function called __init__(), which is always executed when the object is being initiated.

#Prac1:Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.
class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def print_avg(self):
        sum=0
        for val in self.marks:
            sum += val
        average = sum / len(self.marks)
        print(f"Average marks for {self.name}: {average}")

s1= input("Enter student name: ")
marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))
student1 = Students(s1, [marks1, marks2, marks3])
student1.print_avg()

#Static Method: A method that belongs to the class rather than any instance. It can be called on the class itself without creating an instance.

class Student:
    @staticmethod #Decorator to define a static method
    def print_welcome_message():
        print("Welcome to the Student Management System")

#Abstraction: Hiding the complex implementation details and showing only the essential features of the object. In Python, we can achieve abstraction using abstract classes and interfaces.
class Car:
    def __call__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started")

car1 = Car()
car1.start()  # Starting the car
# The car can be started without knowing the internal workings of the Car class, demonstrating abstraction.

#Encapsulation: Bundling the data (attributes) and methods that operate on the data into a single unit (class). It restricts direct access to some of the object's components.

#Prac2: Create Account class with 2 attributes - balance & account no and create methods for debit, credit and printing the balance.
class Account:
    def __init__(self, bal, acc_no, acc_pass):
        self.balance = bal
        self.acc_no = acc_no
        self.__acc_pass = acc_pass #__makes this private
    
    def reset_pass(self):
        print(self.__acc_pass)

    #Debit Method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total Balance =", self.get_balance())

    #Credit Method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total Balance = ", self.get_balance())

    def get_balance(self):
       return self.balance

acc1 = Account(10000, 123456789, 456123)
print(acc1.__acc_pass)#will not print
acc1.reset_pass()#will print
acc1.debit(1000)
acc1.credit(500)

#del keyword: Used to delete an object or variable.

s2=Student("Yuvraj")
del s2