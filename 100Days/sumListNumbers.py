
import unittest
def sumNumbers(inp_list):
    
    numsum=0
    for x in inp_list:
        numsum = numsum+x
        
    return numsum

class Tests(unittest.TestCase):
    data = [
        ([100, 200, 300, 400, 0, 500], 1500),
        ([100, -200, -300, 400, 0, 500], 500),
    ]

    def test_sumNumbers(self):
        for test in self.data:
            inp_list, exp_out = test
            real_out = sumNumbers(inp_list)
            print("Expected Output:{}, Real Output:{}". format(exp_out, real_out))
            self.assertEqual(real_out, exp_out)
if __name__ == "__main__":
    unittest.main()
