# a closure is a function object that has access to variables in its enclosing scope


def transmit_to_space(message):
    "This is the enclosing function"

    def data_transmitter():
        "The nested function"
        print(message)

    return data_transmitter


fun2 = transmit_to_space("Burn the Sun!")
fun2()
