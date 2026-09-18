import unittest

import hello_world


# Test Case
class TestHelloWorld(unittest.TestCase):
    def test_helo(self):
        hello_world.run()
