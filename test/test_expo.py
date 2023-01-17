import unittest

import HelloWorld


class ExpoTest(unittest.TestCase):
    def test_expoOne(self):
        self.assertEqual(2, HelloWorld.exponent(2, 1))

    def test_expoTwo(self):
        self.assertEqual(8, HelloWorld.exponent(2, 3))

    def test_expoThree(self):
        self.assertEqual(32, HelloWorld.exponent(2, 5))

    def test_expoFour(self):
        self.assertEqual(4, HelloWorld.exponent(16, 0.5))

    def test_expoFive(self):
        self.assertEqual(0.1, HelloWorld.exponent(10, -1))


if __name__ == '__main__':
    unittest.main()
