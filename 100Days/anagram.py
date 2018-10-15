import unittest
def anagrams(str1, str2):
    # if str1.isdigit or str2.isdigit:
    #     raise ValueError
    if len(str1)!=len(str2):
        return False
    elif sorted(str1) == sorted(str2):
        return True
    else:
        return False

def anagrams1(str1, str2):
    if len(str1) !=len(str2):
        return False
    if str1.isdigit or str2.isdigit:
        raise ValueError
    else:
        for c in str1:
            if c in str2:
                return True
            else:
                return False

class tests(unittest.TestCase):
 
    data  = [
        ("sharon", "nsharo" , True),
        ("shush","sharon" , False), 
        ("Shush", "shusho", False),
        # (4, 5, ValueError)
     
    ]
    def test_anagrams(self):
        for tests in self.data:
            str1, str2,exp_out = tests
            real_out = anagrams(str1, str2)
            print("expected:{}, real:{}" .format(exp_out, real_out))
            self.assertEqual(exp_out, real_out)
if __name__ == '__main__':
    unittest.main()