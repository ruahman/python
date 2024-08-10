def repeater(old_function):
    def new_function(*args, **kwds):
        old_function(*args, **kwds)
        old_function(*args, **kwds)

    return new_function


@repeater
def multiply(num1, num2):
    print(num1 * num2)


multiply(2, 3)


def multiplier(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)

        return new_function

    return multiply_generator  # it returns the new generator


# Usage
@multiplier(3)  # multiply is not a generator, but multiply(3) is
def return_num(num):
    return num


# Now return_num is decorated and reassigned into itself
return_num(5)  # should return 15
