import atkinsieve # The code to test
import unittest   # The test framework

class Test_Testall(unittest.TestCase):
    def test_sieve(self):
        self.assertEqual(atkinsieve.atkin(6), [2, 3, 5])

if __name__ == '__main__':
    unittest.main()