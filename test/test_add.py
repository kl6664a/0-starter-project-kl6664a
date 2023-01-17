import unittest

import HelloWorld


class AddTest(unittest.TestCase):
    def test_addOne(self):
        self.assertEqual(2, HelloWorld.addTwoNumbers(1, 1))

    def test_addTwo(self):
        self.assertEqual(-1, HelloWorld.addTwoNumbers(-2, 1))

    def test_addThree(self):
        self.assertEqual(-75, HelloWorld.addTwoNumbers(-25, -50))


if __name__ == '__main__':
    unittest.main()
