import unittest
from math_helpers import functionA

class goldbach_Tests(unittest.TestCase):
    def test_gb_gives_produces_gb_number(self):
        self.assertTrue(functionA(1,1),functionA(1,2))

if __name__ == '__main__':
    unittest.main()
