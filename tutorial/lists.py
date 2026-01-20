import unittest


def run():
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist)

    # list length
    print(len(thislist))

    # list items
    print(thislist[1])

    # last item
    print(thislist[-1])

    # range
    print(thislist[2:5])

    # end
    print(thislist[:4])

    # start
    print(thislist[2:])

    # check if item exists in list
    if "apple" in thislist:
        print("Yes, 'apple' is in the fruits list")

    thislist[1] = "blackcurrant"
    print(thislist)

    # append
    thislist.append("orange")
    print(thislist)

    # insert
    thislist.insert(1, "orange")
    print(thislist)

    # remove
    # thislist.remove("banana")
    # print(thislist)

    # remove specified index
    thislist.pop(1)

    # loop
    for x in thislist:
        print(x)

    # loop with index
    for i in range(len(thislist)):
        print(thislist[i])

    # list comprehension
    [print(x) for x in thislist]

    # list comprehensions
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

    newlist = [x for x in fruits if "a" in x]

    print(newlist)

    newlist = [x for x in fruits if x != "apple"]

    print(newlist)

    copylist = fruits[:]
    print(copylist)


# Test Case
class TestRun(unittest.TestCase):
    def test_run(self):
        run()


if __name__ == "__main__":
    run()
