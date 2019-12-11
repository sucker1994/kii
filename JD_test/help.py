import unittest

class SimpleMath(unittest.TestCase):


    def testMuityply(self):
        self.assertEqual((2*3),6)


if __name__=='__main__':
    unittest.main()