#lambda is used as a single line function instead of defining a function using def keyword
#syntax: lambda arguments: expression
s = lambda x: x*x
print(s(5))

l = [1,2,3,4,5]
print(list(map(lambda x: x*x, l)))

sum = lambda a,b: a+b
print(sum(2,3))

#join is used to join the elements of an iterable (like list, tuple) into a single string with a specified separator
#syntax: 'separator'.join(iterable)

l = [1,2,3,4,5]
print(" ".join(map(str,l)))

k = ['a','b','c','d']
print("::".join(k))

#format is used to format strings by embedding expressions inside string literals
#syntax: "string with placeholders {}".format(values)

name = "Asabeneh"
age = 250
print("Hello, my name is {0} and my age is {1} years.".format(name, age))

#map is used to apply a function to all items in an iterable (like list, tuple)
#syntax: map(function, iterable)

l = [1,2,3,4,5]
print(list(map(lambda x: x*2, l)))

#filter is used to filter items in an iterable based on a function that returns True or False
#syntax: filter(function, iterable)

l = [1,2,3,4,5]
print(list(filter(lambda x: x%2==0, l)))

#reduce is used to apply a function cumulatively to the items of an iterable, reducing it to a single value
#syntax: reduce(function, iterable)

from functools import reduce
l = [1,2,3,4,5]
print(reduce(lambda x,y: x+y, l))