print("Hello")
print('Hello')
# You can display a string literal with the print() function
a = "Hello"
print(a)
# Assign String to a Variable
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# You can use three double quotes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
# Or three single quotes
b = "Hello, World!"
print(b[2:5])
# Slicing
b = "Hello, World!"
print(b[:5])
#Slice From the Start
b = "Hello, World!"
print(b[2:])
# Slice To the End
b = "Hello, World!"
print(b[-5:-2])
# Negative Indexing
# MODIFY STRINGS
a = "Hello, World!"
print(a.upper())
# Upper Case
a = "Hello, World!"
print(a.lower())
# Lower case
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
# Remove Whitespace
a = "Hello, World!"
print(a.replace("H", "J"))
# Replace String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
# Split strings
