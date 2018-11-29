import unittest
def compress(inp):
    count_alphabets = 1
    new_string = ""
    # new_string += inp[0]

    inp_len  = len(inp)
    while inp_len is not None:
        if len(new_string) >= inp_len:
            return inp

        if inp[index] == inp[index+1]:
            count_alphabets += 1
        else:
            if count_alphabets > 1:
                new_string += str(count_alphabets)
            new_string += inp[index+1]
            count_alphabets = 1
    if(count_alphabets > 1):
        new_string += str(count_alphabets)
    return new_string  

class tests(unittest.TestCase):
 
    data  = [
        ("aaabbcc", "a3b2c2"),
        ("aaaabbbbcccddddd", "a4b4c3d5")
        # ("abc", "abc")
        # (4, 5, ValueError)
     
    ]
    def test_compress(self):
        for tests in self.data:
            inp,exp_out = tests
            real_out = compress(inp)
            print("expected:{}, real:{}" .format(exp_out, real_out))
            self.assertEqual(exp_out, real_out)
if __name__ == '__main__':
    unittest.main()