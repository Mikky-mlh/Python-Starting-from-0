#Dictionary: It is used to store data values in key:value pairs. They are unordered & mutable but doesn't allow duplicate keys.
dict = {
    "Name":"Yuvraj",
    "CGPA": 9.7,
    "Marks":[98, 97, 80]
}
print(dict)
print(dict["Name"])
dict["Class"]=12 #To add new value
dict["Name"]="Hina" #To change the value assigned.
print(dict)
print(type(dict))
#Nested Dictionary
student={
    "Name": "Mikky",
    "Score": {
        "Phy": 98,
        "Chem": 97,
        "Maths": 88
    }
}
print(student)
student["Score"]["Maths"]=90
print(student["Score"]["Maths"])

b="Hi"
#Dictionary Methods
print(student.keys()) #return all keys
print(student.values()) #return all values
print(student.items()) #returns all (key, val) pairs as tuples
print(student.get("Name")) #returns the key acc.to val.
new_dict={"name": "kk", "age": 16}
student.update(new_dict) #inserts the specified items to the dictionary
print(student)

#Sets: Set is the collection of the unordered items. Each element in the set must be unique & immutable.
nums={1,2,3,4}
set2={1,2,2,2,5,6} #repeated elements stored only once, so it resolved to {1, 2}
print(set2)
print(type(set2))
null_set=set() #empty set syntax
print(null_set)

#Set Methods
nums.add("HI") #adds an element
nums.remove(4) #removes the element
print(nums)
nums.clear() #empties the set
print(nums)
set2.pop() #removes a random value
print(set2)
nums2={1,2,3,4}
print(nums2.union(set2)) #combines both set values & returns new
print(nums2.intersection(set2)) #combines common values & returns new

#Prac1: Store following word meanings in a python dictionary: 
Dictionary={
    "table" : "a piece of furniture",
    "cat" : "a small animal"
}
print(Dictionary)

#Prac2: You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students?
Subjects={"python", "java", "C++", "python", "javascript", "java", "java", "C++", "C", "python"}
print(Subjects)
print(len(Subjects))

#Prac3: WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
Scorecard={

}
Scorecard["Maths"]=float(input("Your marks in Maths:"))
Scorecard["Physics"]=float(input("Your marks in Physics:"))
Scorecard["Chemistry"]=float(input("Your marks in Chemistry:"))
print("Your marks are as:", Scorecard)

#Prac4: Figure out a way to store 9 & 9.0 as separate values in the set.
Set9={"9",9.0}
print(Set9)