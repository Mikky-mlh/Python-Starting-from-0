"""Python can be used to perform oerations on a file. (read & write data)
Types of files
1. Text files: txt, docx, log etc
2. binary files; mp4, mov, png, jpeg etc"""

#Open, read & close File.
f=open("idk.txt", "r")
data=f.read()#reads entire file
print(data)
print(type(data))
data=f.readline #read only one line
data=f.read(5)#read only 5 characters
f.close()

""""Modes:
r:read
w:write
x:create a new file and write
a:open for writing, appending to the end of the file if it exists
b:binary mode
t:text mode(default)
+:open a disk for updating(read & write)"""

#Writing to a file
f=open("idk.txt", "w")
f.write("New Line is this.")
print(data)
f.close()

f = open("demo.txt","a")
f.write("this is a new line") #adds to the file

#With Syntax
with open("demo.txt", "r") as f:
    data= f.read()
    print(data)
with open("demo.txt", "w") as f:
    f.write("new data") #rewrote the entire file.

#Deleting a File:Using the os module. Module (like a code library) is a file written by another programmer that generally has a functions we can use.

import os
os.remove("idk.txt")
