import unittest
# check whether a number is in a defined range. 
def find_string(num):
    if num in range(1, 101):
        return True
    else:
        return False
class Tests(unittest.TestCase):
    data = [

        (100,True), 
        (90, True),
        (200, False)
    ]
    def test_find_string(self):
        for test in self.data:
            num, exp_out = test
            real_out = find_string(num)
            print("Expected output:{}, Real Output:{}" .format(exp_out, real_out))
            self.assertEqual(exp_out, real_out)


if __name__ == "__main__":
    unittest.main()

        