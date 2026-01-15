import unittest


def hello():
    return "hello world"


# Test Case
class TestHelloWorld(unittest.TestCase):
    def test_helo(self):
        self.assertEqual(hello(), "hello world")


if __name__ == "__main__":
    print(hello())
