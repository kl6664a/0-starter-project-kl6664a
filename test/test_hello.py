import HelloWorld
import unittest


class HelloTest(unittest.TestCase):
    def test_helloOne(self):
        self.assertEqual("Hello World!", HelloWorld.hello())

    def test_helloTwo(self):
        self.assertEqual("Hello World!\n", HelloWorld.helloLine())


if __name__ == '__main__':
    unittest.main()
