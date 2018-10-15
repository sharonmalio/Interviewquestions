import unittest
def spaces(string1):
    return "%20".join(string1.split(" "))
   

class Tests(unittest.TestCase):
    data = [

        ("sharon malio", "sharon%20malio"), 
        ("kan ni", "kan%20ni")
    ]
    def test_spaces(self):
        for tests in self.data:
            string1, exp_output = tests
            real_output = spaces(string1)
            print("expected:{}, real:{}". format(exp_output, real_output))
            self.assertEqual(exp_output, real_output)
if __name__ == '__main__':
    unittest.main()