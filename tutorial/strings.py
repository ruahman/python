# pylint: disable=C0103
"""show how strings work"""

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
