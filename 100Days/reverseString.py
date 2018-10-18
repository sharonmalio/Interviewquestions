import unittest
def string_reverse(string_inp):
    if len(string_inp) <= 1:
        return string_inp
    # return string_inp[::-1]
    return string_reverse(string_inp[1:]) + string_inp[0]

    # method 2
def reverse_string(string_inp):
    string_length = len(string_inp)
    reversed_string = []
    while string_length>0:
        reversed_string.append(string_inp[string_length-1])
        string_length -= 1
    return ''.join(reversed_string)

    
class Tests(unittest.TestCase):
    data =[
        ("sharon", "norahs")

    ]
    def test_string_reverse(self):
        for test in self.data:
            string_inp, expected_output = test
            real_output = reverse_string(string_inp)
            print("Expected output:{}, Real output:{}" .format(expected_output,real_output))
            self.assertEqual(expected_output, real_output)
if __name__ == "__main__":
    unittest.main()