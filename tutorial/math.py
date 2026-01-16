import unittest


def run():
    add = 3 + 1
    print(add)
    sub = 3 - 1
    print(sub)
    times = 3 * 2
    print(times)
    div = 6 / 4
    print(div)
    floor = 6 // 4
    print(floor)
    mod = 6 % 4
    print(mod)
    exponent = 2**3
    print(exponent)


# Test Case
class TestRun(unittest.TestCase):
    def test_run(self):
        run()


if __name__ == "__main__":
    run()
