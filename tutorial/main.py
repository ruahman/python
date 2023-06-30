""" main module """


def main():
    """main method"""
    i = 1

    max = 10  # pylint: disable=redefine-builtin
    while i < max:
        print(i)
        i = i + 1


# call function main
main()
