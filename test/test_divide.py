import unittest

import HelloWorld


class DivideTest(unittest.TestCase):
    def test_divideOne(self):
        self.assertEqual(1, HelloWorld.divideTwoNumbers(1, 1))

    def test_divideTwo(self):
        self.assertEqual(-2, HelloWorld.divideTwoNumbers(-2, 1))

    def test_divideThree(self):
        self.assertEqual(0.5, HelloWorld.divideTwoNumbers(-25, -50))


if __name__ == '__main__':
    unittest.main()
