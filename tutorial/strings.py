import unittest


def run():
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

    # strings are immutable
    name = "Sam"
    # this cause problems
    # name[0] = "P"
    # instead use concatenation
    print("concat: " + "P" + name[1:])

    # upper
    print("cap: ", name.upper())

    # split
    name = "Sam Vila"
    print("split: ", name.split())
    name = "Diego-vila"
    print("split: ", name.split("-"))

    # formating
    name = "John"
    print("format:", f"Hi {name}")
    age = "23"
    print(f"format: {name} is {age} years old")

    print("format: ", "String here {} then also {}".format("somethign1", "something2"))
    print("format: ", "The {2} {1} {0}".format("fox", "brown", "quick"))
    print("format: ", "The {q} {b} {f}".format(f="fox", b="brown", q="quick"))

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

    # reverse index
    print("reverser " + b[-3])

    # copy
    print(f"copy: {b[:]}")

    # skip
    print(f"skip: {b[::2]}")

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


# Test Case
class TestRun(unittest.TestCase):
    def test_run(self):
        run()


if __name__ == "__main__":
    run()
