import unittest


def run():
    a = 3 + 1
    print(type(a))
    a = 3.5
    print(type(a))


# Test Case
class TestRun(unittest.TestCase):
    def test_run(self):
        run()


if __name__ == "__main__":
    run()
