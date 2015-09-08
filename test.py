import unittest
import greeter


class TestMyMod(unittest.TestCase):
    def test(self):
        assert(greeter.greet(), 'Hello')
