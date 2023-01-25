# PYTHON VARIABLES
x = 5
y = "John"
print(x)
print(y)
#  1) Example
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
# 2) Example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
# 3) Example
a = 4
A = "Sally"
# 4) Example A will not overwrite a
# VARIABLES NAME
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
# Legal variables name
myVariableName = "John"
# Camel case
MyVariableName = "John"
# Pascal case
my_variable_name = "John"
# Snake case
# ASSIGN MULTIPLE VARIABLES
x = y = z = "Orange"
print(x)
print(y)
print(z)
# 1) Example
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
# Unpack a list
# OUTPUT VARIABLES
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#In the print() function, you output multiple variables, separated by a comma
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#You can also use the + operator to output multiple variables
x = 5
y = 10
print(x + y)
#For numbers, the + character works as a mathematical operator:
# GLOBAL VARIABLES
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#Create a variable inside a function, with the same name as the global variable
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#If you use the global keyword, the variable belongs to the global scope:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

