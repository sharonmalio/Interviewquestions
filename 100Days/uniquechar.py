import unittest
def uniquchars(word):

    storeunique = set()

    for c in word:
        if c in storeunique:
            return False
        else:
            storeunique.add(c)
    return True
    
# Implement an algorithm to determine if a string has all unique characters. What if you
# can not use additional data structures?
class Tests(unittest.TestCase):
    data  = [
        ("sharon" , True),
         ("shush", False), 
        ("kanini", False), 
        ("mariakamau", False)
      

    ]
    def test_uniquchars(self):
        for tests in self.data:
            word,exp_out = tests
            real_out = uniquchars(word)
            print("expected:{}, real:{}" .format(exp_out, real_out))
            self.assertEqual(exp_out, real_out)
if __name__ == '__main__':
    unittest.main()
