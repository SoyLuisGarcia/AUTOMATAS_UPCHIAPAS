import unittest


class TestBasicos(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(2+2,4)
    
    def test_resta(self):
        self.assertTrue(1-1==0) 
    
    def test_multiplicacion(self):
        self.assertEqual(2*6,12) 

if __name__=='__main__':
    unittest.main()

#Garcia_Gonzalez_183405