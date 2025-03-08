"""show how strings work"""

# pylint: disable=invalid-name

message = "This is a string in Python"
message = "It's a string"
message = '"Beautiful is better than ugly.". Said Tim Peters'
message = r"C:\python\bin"

# multiline strings
help_message = """
Usage: mysql command
    -h hostname     
    -d database name
    -u username
    -p password 
"""

print(help_message)

# formating
name = "John"
message = f"Hi {name}"
print(message)

# concat
greeting = "Good "
time = "Afternoon"

greeting = greeting + time + "!"
print(greeting)


# asses string elements
str = "Python String"
print(str[0])  # P
print(str[1])  # y


# string length
str = "Python String"
str_len = len(str)
print(str_len)


# string slice
str = "Python String"
print(str[0:2])

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)

# string slice
b = "Hello, World!"
print(b[2:5])

# slice from the start
b = "Hello, World!"
print(b[:5])


# slice to the end
b = "Hello, World!"
print(b[2:])

# remove whitespace
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"

# split string
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']

# string formate
age = 36
txt = f"My name is John, I am {age}"
print(txt)
