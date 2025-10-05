##LISTS:Mutable(changable) sequences of values.
marks=[94.4, 87, 95, 66, 45]#Use comma to enter different lists.
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])#The first element is labeled as 0.
student=["Karan", 78, 17, "New Delhi"]

#You cannot change the string once assinging it but can do for Lists.
str="Hello"
try:
    str[0]="y"
    print(str[0])
except:
    student[0]="Yuvraj"
    print(student[0]) #Finds the indexed element.
print(student)

#List slicing is same as string.
print(marks[1:4])

#List Methods
marks.append(89) #Adds an element in last
marks.sort() #Sorts in asc. order
print(marks.sort()) #Gives NONE as it doesn't print directly.
print(marks) #Now print in ascending order.
marks.sort(reverse=True)
print(marks) #Now print in descending order.
marks.reverse()
print(marks) #Now print in revrse order from the last order.
marks.insert(7, 54) #Insert 54 at the 7th position in the list(last updated)
print(marks) 
marks.remove(66) #Removes the element from the list.
print(marks)
marks.pop(5) #Removes the indexed element from the list.
print(marks)

##TUPLES:Immutable sequences of values.
tup=(87,64,33,95,76,33,'hello') #Uses () than [] in lists.
print(tup)
print(type(tup))
tup1=() #can be empty.
print(tup1)
print(type(tup1))
tup2=(1,)
print(tup2)
tup3=(1)
print(tup3)
print(type(tup2))
print(type(tup3))
#Both tup2 and tup3 gives different results but tup3 is no longer a tuple but just an integer value(could also be stringe or float depending on what you wrote) under the name of tup2.
#Tuples Slicing is same as lists and stringes.
print(tup[1:4])

#Tuples Methods
print(tup.index(33)) #Find the index of first occurence 33 in tuple.
print(tup.count(33)) #Counts the total number of occurrences.

print(tup[0]) #Finds the indexed element.

#Prac1: WAP to ask the user to enter names of their 3 favourite movies & store them in a list.
Movie1=(input("Write the name of your favourite movie:"))
while Movie1.strip()=="": #.strip is used to eliminate all empty spaces/tab/newlines. While is a loop function.
    Movie1=(input("Write the name of your favourite movie:"))
Movie2=input("Write the name of your other favourite movie:")
while Movie2.strip()=="":
    Movie2=(input("Write the name of your other favourite movie:"))
Movie3=input("Write the name of your another favourite movie:")
while Movie3.strip()=="":
    Movie3=(input("Write the name of your another favourite movie:"))
Movies=[Movie1, Movie2, Movie3]
print("Your 3 favourite movies are:", Movies)

#Prac2: WAP to check if a list contains a palindrome of elements.
list22=[1,2,3]
list22.copy #Gives a shallow list of the OG list.
if(list22==list22.reverse()):
    print("The list is a palindrome.")
else:
    print("The list is a palindrome.")

#Prac3: WAP to count the number of students with the "A" grade in the following tuple. Store the above values in a list & sort them from "A" to "D".
Grade=["C","D","A","A","B","B","A"]
print(Grade.count("A"))
Grade.sort()
print(Grade)