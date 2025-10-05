"""Prac1: Create a new file “practice.txt” using python. Add the following data in it:
Hi everyone
we are learning File I/O
using Java.
I like programming in Java"""

with open("practice.txt", "w") as f:
    f.write("Hi everyone we are learning File I/O\n")
    f.write("using Java.\nI like programming in Java")

#Prac2: WAF that replace all occurrences of “java” with “python” in above file.
with open("practice.txt", "r") as f:
    data=f.read()
new_data=data.replace("Java", "Python")
print(new_data)

#Prac3:Search if the word “learning” exists in the file or not.
def check_for_word():
    word="learning"
    with open("practice.txt", "r") as f:
        data=f.read()
        if(data.find(word))!=-1:
            print("found")
        else:
            print("Not found")
    
#Prac4: WAf to find in which line of the file does the word learning occur first.
def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt", "r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
    return -1

print(check_for_line())

#Prac5:From a file containing numbers separated by comma, print the count of even numbers.
count=0
with open("practice.txt", "r"):
    data=f.read()
    
    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count+=1
print(count) 

