#Inheritance: When one class derives the properties & methods of another class.

class Car:
    def __init__(self, type):
        self.type = type

    def __call__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started..")

class ToyotaCar(Car):
    def __init__(self, brand, type):
        self.brand = brand
        super().__init__(type)
        super().start()

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A,B):
     varC = "Welcome to class C"

#Super Method: Used to access methods of parent classes
car1 = ToyotaCar("prius", "electric")
print(car1.type)

#Class Method: A class method is bound to the class & receives the class as an implicit first argument. Static method cannot access or modify class state & generally for utiliy.
class Person:
    name = "anonymous"

    def changename(self, name): #instance method
        self.__class__.name = "yu" 
        #self.__class_. or 'Classname'. to make a direct change in class.

p1 = Person()
p1.changename("k")
print(p1.name)
print(Person.name)

class Human:
    name = "anonymous"

    @classmethod
    def changename(cls, name):
        cls.name = name

h1= Human()
h1.changename("YUVRAJ")
print(h1.name)

#Property Decorator: To use a method as a property

class Student:
    def __init__(self, phy, chem, maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
       # self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths)/3) + "%"


s1= Student(59,56,45)
print(s1.percentage)

s1.phy=98
print(s1.phy)
print(s1.percentage)# % will not change if # code is used but will if @property is used.

#Polymorphism: Operator Overloading:- When the same operator is allowed to have different meaning according to the context.
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(float(input("Real:")), float(input("Img:")))
num2 = Complex(float(input("Real:")), float(input("Img:")))
num3 = num1 + num2
num1.shownumber()
num2.shownumber()
num3.shownumber()

#Prac1: Define a Circle class to create a circle with radius r using the constructor. Define an Area() & Circumference() method of the class which calculates its area and perimeter respectively.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def circumference(self):
        return 2 * 3.14 * self.radius
    
#Prac2: Define a Employee class with attributes role, department & salary. This class should have a method to showDetails() the details of the employee. Create an Engineer class that inherits from Employee and has an additional attribute of name & age. This class should also have a method to showDetails() that overrides the method in Employee.
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print(f"Role: {self.role}, Department: {self.department}, Salary: {self.salary}")

class Engineer(Employee):
    def __init__(self, role, department, salary, name, age):
        super().__init__(role, department, salary)
        self.name = name
        self.age = age

    def showDetails(self):
        super().showDetails()
        print(f"Name: {self.name}, Age: {self.age}")
        
# Example usage
circle = Circle(5)
print("Area of Circle:", circle.area())
print("Circumference of Circle:", circle.circumference())
engineer = Engineer("Software Engineer", "IT", 70000, "Alice", 30)
engineer.showDetails()