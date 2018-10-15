import unittest
def anagrams(str1, str2):
    # if str1.isdigit or str2.isdigit:
    #     raise ValueError
    if len(str1) !=len(str2):
        return False
 
    else:
        for c in str1:
            if c in str2:
                return True
            else:
                return False
class Tests(unittest.TestCase):
    data = [
        ("sharon", "nsharo" , True),
        ("shush","sharon" , False), 
        ("Shush", "shusho", False),
  
        # (4, 5, ValueError)
    ]
    def test_anagrams(self):
        for tests in self.data:
            str1, str2, exp_output=tests
            real_output =  anagrams(str1,str2)
            print("expected:{},real:{}" . format(exp_output, real_output))
            self.assertEqual(exp_output, real_output)
    # def test_ValueError(self):
    #     self.assertRaises(ValueError, anagrams, 4, 6)

if __name__ == '__main__':
    unittest.main()
            
    
