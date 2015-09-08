import unittest
import greeter


class TestMyMod(unittest.TestCase):
    def test(self):
        assert(greeter.greet(), 'Hello')

    def test_that_breaks(self):
        self.assertEqual(1, 0)
