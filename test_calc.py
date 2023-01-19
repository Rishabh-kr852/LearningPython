import unittest             # import the library for unit test
import calc                 # import module on which unit testing is needed to be done

class TestClac(unittest.TestCase):               # inherit unittest.TestCase to calss formed, it is necessary to inherit to use unittest inbuilt functions
    
    def test_add(self):                          # function name must start from keyword 'test_' otherwise it won't run at time of execution
        # result = calc.add(10,4)
        self.assertEqual(calc.add(10,5), 15)             # self.callFunction(var1, var2) 
        self.assertEqual(calc.add(-1,1), 0)              
        self.assertEqual(calc.add(-1,-1), -2)            # write better test cases, here addition of two -ve numbers are shown
        
    
    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5), 5)            
        self.assertEqual(calc.subtract(-1,1), -2)              
        self.assertEqual(calc.subtract(-1,-1), 0)
    
    def test_multipy(self):
        self.assertEqual(calc.multiply(10,5), 50)            
        self.assertEqual(calc.multiply(-1,1), -1)              
        self.assertEqual(calc.multiply(-1,-1), 1)
        
    def test_divide(self):
        self.assertEqual(calc.divide(10,5), 2)            
        self.assertEqual(calc.divide(-1,1), -1)              
        self.assertEqual(calc.divide(-1,-1), 1)
        
        # self.assertRaises(ValueError, calc.divide, 10,0)    # assertRaises(ValueError, function without args, arg1, arg2). 
        
        with self.assertRaises(ValueError):       # this is context method which looks familiar as readin,writing docs and it also accepts args in function
            calc.divide(10,0)


# to execute the command write 'python -m unittest test_calc.py'
# to avoid writting above code again and again the following code is implemented

if __name__ == '__main__':
    unittest.main()