import unittest

import HelloWorld


class SubTest(unittest.TestCase):
    def test_subOne(self):
        self.assertEqual(0, HelloWorld.subtractTwoNumbers(1, 1))

    def test_subTwo(self):
        self.assertEqual(-3, HelloWorld.subtractTwoNumbers(-2, 1))

    def test_subThree(self):
        self.assertEqual(25, HelloWorld.subtractTwoNumbers(-25, -50))


if __name__ == '__main__':
    unittest.main()
