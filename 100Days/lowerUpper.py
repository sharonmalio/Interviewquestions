import unittest
# find number of lowercase characters and the uppercase characters
def lowerUpper(string_inp):
    uppercount = 0
    lowercount = 0    
    for c in string_inp:
        if c.isupper():
            uppercount += 1
        elif c.islower():
            lowercount += 1
    return uppercount, lowercount

    

class Tests(unittest.TestCase):
    data = [
        (("SHAMALIO"),(8, 0)), 
        (("KaniniMalio"), (2, 9))
    ]

    def test_lowerUpper(self):
        for test in self.data:
            string_inp, exp_output = test
            real_output = lowerUpper(string_inp)
            print("Real output:{}, Expected output:{}" .format(exp_output, real_output))
            self.assertEqual(exp_output, real_output)
if __name__ =="__main__":
    unittest.main()