import unittest
def multiplication(num):
    string = ""
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            string +=  "{}\t".format(i*j, end="\t")
        string += "\n"
    return string
    
class Tests(unittest.TestCase):
    data = [
        (3, '1\t2\t3\t\n2\t4\t6\t\n3\t6\t9\t\n')
    ]
    def test_multiplication(self):
        for test in self.data:
            num, Expected_output = test
            real_output = multiplication(num)
            print("expected:{}, real:{}". format (Expected_output, real_output) )
            self.assertEqual(Expected_output, real_output)

if __name__ =='__main__':
    unittest.main()