import unittest

from main import hex2int, int2hex

class Test_hex2int(unittest.TestCase):
    def test_one(self):
        result = hex2int('a2f')
        self.assertEqual(result, 2607)

    def test_two(self):
        result = hex2int('A2F')
        self.assertEqual(result, 2607)
    
    def test_three(self):
        result = hex2int('12cd')
        self.assertEqual(result, 4813)

    def test_four(self):
        result = hex2int('gc')
        self.assertEqual(result,'Invalid value')


class Test_int2hex(unittest.TestCase):
    def test_one(self):
        result = int2hex(1)
        self.assertEqual(result, 1 )

    def test_two(self):
        result = int2hex(10)
        self.assertEqual(result, 'A')
    
    def test_three(self):
        result = int2hex(12)
        self.assertEqual(result,'C' )

    def test_four(self):
        result = int2hex(56)
        self.assertEqual(result,'Invalid value')



if __name__ == '__main__': 
    unittest.main() 