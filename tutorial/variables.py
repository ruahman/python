def run():
    a = 3 + 1
    print(type(a))
    a = 3.5
    print(type(a))

    x = 5
    y = "Hello, World!"
    print(x, y)

    x, y, z = "Orange", "Banana", "Cherry"
    print(x)
    print(y)
    print(z)

    fruits = ["apple", "banana", "cherry"]
    x, y, z = fruits
    print(x)
    print(y)
    print(z)

    # this make a global variable
    global gx
    gx = "global"
    print(gx)


# Test Case
if __name__ == "__main__":
    run()
