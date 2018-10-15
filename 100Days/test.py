
import unittest
def add(inp):
    inp = input("Enter integers separated by space:\n")
    result = [int(x) for x in inp.split()]
    return sum(add(result))
    

class Tests(unittest.TestCase):
    data= [
        ((2, 4, 6), 12)
      
        
   ]
    def test_add(self):
       
        for test in self.data:
            inp, exp_out=test
            real_out = add(inp)
            print("Expected Output:{}, Real Output:{}". format(exp_out, real_out))
            self.assertEqual(exp_out, real_out)

       
        # with self.assertRaises(TypeError):
        #     if type(a) or type(b) is not int:
        #         raise TypeError('Invalid Input')
        #     elif a<0 or b<0:
        #         raise ValueError('Invalid Input')
       

          
        
if __name__ == '__main__':
    unittest.main()