import unittest


def my_types():
    my_int = 3
    print(my_int)
    my_float = 2.3
    print(my_float)
    my_str = "hello"
    print(my_str)
    my_list = [10, "hello", 200.3]
    print(my_list)
    my_dict = {"mykey": "value", "name": "Frankie"}
    print(my_dict)
    my_tup = (10, "hello", 200.3)
    print(my_tup)
    my_set = {"a", "b"}
    print(my_set)
    my_bool = True
    print(my_bool)


# Test Case
class TestTypes(unittest.TestCase):
    def test_hello(self):
        my_types()
        self.assertEqual("hello", "hello")


if __name__ == "__main__":
    my_types()
