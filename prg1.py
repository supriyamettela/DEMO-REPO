def subtract(a,b):
    return(a-b)

import unittest

class subtractclass(unittest.testcase):
    def test1(self):

        result = subtract(10,7)
        self.assertEqual(result,3)

    def test2(self):

        result = subtract(0,7)
        self.assertEqual(result,-7)

    def test3(self):

        result = subtract(6,7)
        self.assertEqual(result,-1)

    def test4(self):

        result = subtract(10,0)
        self.assertEqual(result,0)

    def test5(self):

        result = subtract(77,7)
        self.assertEqual(result,70)

    def test6(self):

        result = subtract(-7,-7)
        self.assertEqual(result,0)

 

   


if __name__=='__main__':
    unittest.main()
