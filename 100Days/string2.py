# Write code to reverse a C-Style String. (C-String means that “abcd” is represented as
# five characters, including the null character.)
# ______________________________________
import unittest
def reverse(string):
   string = string[:-1]
   stringfinal = string[::-1]
   finalfinal = stringfinal + "\0"

class Tests(unittest.TestCase):
    data  = [
        ("sharon\0" , "norahs\0"),
        # ("shush", "hsuhs"), 
        # ("kanini", "ininak"), 
        # ("mariakamau", "uamakairam")
        

    ]
    def test_reverse(self):
        for tests in self.data:
            string,exp_out = tests
            real_out = reverse(string)
            print("expected:{}, real:{}" .format(exp_out, real_out))
            self.assertEqual(exp_out, real_out)
            
if __name__ == '__main__':
    unittest.main()


