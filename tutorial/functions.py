def my_function():
    print("Hello from a function")


my_function()


def my_function_param(fname):
    print(fname + " Refsnes")


my_function_param("Emil")
my_function_param("Tobias")
my_function_param("Linus")


# Arbitrary Arguments, *args
def my_function_arb(*kids):
    print("The youngest child is " + kids[2])


my_function_arb("Emil", "Tobias", "Linus")


# Keyword Arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


# Arbitrary Keyword Arguments, **kwargs
def my_function_arb_key(**kid):
    print("His last name is " + kid["lname"])
    print("His first name is " + kid["fname"])


my_function_arb_key(fname="Tobias", lname="Refsnes")


# Default Parameter Value
def my_function_default(country="Norway"):
    print("I am from " + country)


my_function_default()


# It is possible to declare functions which receive a variable number of arguments,
# using the following syntax:


def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))


foo(1, 2, 3, 4, 5)


def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" % (first + second + third))

    if options.get("number") == "first":
        return first


result = bar(1, 2, 3, action="sum", number="first")
print("Result: %d" % (result))
