def run():
    a = 33
    b = 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")

    if 5 > 2:
        print("Five is greater than two!")

    # short hand
    a = 10
    b = 20
    bigger = a if a > b else b
    print("Bigger is", bigger)


if __name__ == "__main__":
    run()
