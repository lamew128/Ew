import unittest

import function2

class TestFunction(unittest.TestCase):
    def setUp(self):
        pass

    def test_multiply_by_2(self):
        self.assertEqual( function2.multiply_by_2(2), 4)

    def test_triple(self):
        self.assertEqual( function2.triple(3), 9)

if __name__ == '__main__':
    unittest.main()