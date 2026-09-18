def run():
    # string
    x = "Hello World"
    print(x)
    x = str("Hello World")
    print(x)

    # int
    x = 20
    print(x)
    x = int(20)
    print(x)

    # float
    x = 20.5
    print(x)
    x = float(20.5)
    print(x)

    # list
    x = ["apple", "banana", "cherry"]
    print(x)
    x = list(("apple", "banana", "cherry"))
    print(x)

    # tuple
    x = ("apple", "banana", "cherry")
    print(x)
    x = tuple(("apple", "banana", "cherry"))
    print(x)

    # range
    x = range(6)
    print(x)

    # dictionary
    x = {"name": "John", "age": 36}
    print(x)
    x = dict(name="John", age=36)
    print(x)

    # set
    x = {"apple", "banana", "cherry"}
    print(x)
    x = set(("apple", "banana", "cherry"))
    print(x)

    # bool
    x = True
    print(x)
    x = bool(True)
    print(x)

    # bytes
    x = b"Hello"
    print(x)
    x = bytes(5)
    print(x)

    # NoneType
    x = None
    print(x)


# Test Case
if __name__ == "__main__":
    run()
