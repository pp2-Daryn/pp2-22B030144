print(10 > 9) # Output: True
print(10 == 9) # Output: False
print(10 < 9) # Output: False

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  # Print a message based on whether the condition is True or False

x = "Hello"
y = 15

print(bool(x))
print(bool(y))
# The bool() function allows you to evaluate any value, and give you True or False in return
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#The following will return False:
