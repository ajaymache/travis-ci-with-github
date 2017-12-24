#importing unittest package
import unittest

#importing arithmetic module
from ..arithmetic.arithmetic import arithmetic

class TestCases(unittest.TestCase):
        
    def test_add(self):
        calc = arithmetic()
        self.assertEqual(calc.add(2, 3), 5)
        
if __name__ == '__main__':
    unittest.main()