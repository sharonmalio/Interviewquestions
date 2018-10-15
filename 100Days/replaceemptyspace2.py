import unittest

# first method
def replace_string(string1):
    string  = " "
    for char in string1:
        if char == " ":
           string =  string + "%20"
        else:
            string = string + char
    return string
# 2nd method
def spaces(string1):
    string = []
    for char in string1:
        if char == " ":
           string.append("%20")
        else:
            string.append(char)

    return "".join(string)
# third medthod
def spaces2(string1):
    return "%20".join(string1.split(" "))
# fourth method

class Tests(unittest.TestCase):
    data = [

        ("sharon malio", "sharon%20malio"), 
        ("kan ni", "kan%20ni")
    ]
    def test_spaces(self):
        for tests in self.data:
            string1, exp_output = tests
            real_output = replace_string(string1)
            print("expected:{}, real:{}". format(exp_output, real_output))
            self.assertEqual(exp_output, real_output)
if __name__ == '__main__':
    unittest.main()