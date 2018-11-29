import unittest
def stringchange(string1):
    
    new_string = ""
    if len(string1) == 0:
        raise ValueError("we need a string")
    if string1[0].isdigit():
         raise ValueError("we need a string")
    else:
        for index, c in enumerate(string1):
            if string1[index].isalpha() and string1[index+1].isdigit():
                new_string  = new_string + int(string1[index+1])*string1[index]       
        return new_string

# method 2 
def stringchange2(string1):
    if len(string1) == 0 or all(x.isdigit() for x in string1) :
        raise Exception('Invalid input')
    elif all( x.isalpha() for x in string1 ):
        print (string1)
        return string1
    else: 
        num = 0
        alphabet = ''
        results = ''
        for index, i in enumerate(string1):
            if i.isdigit():
                num = num * 10 + int(i)  
            elif i.isalpha():
                alphabet += i   
                results += num * alphabet
                num = 0
                alphabet = ''
        print(results)
        return results
        # method 3
def stringchange3(string1):
    if len(string1) == 0:
        raise ValueError("we need a string")
    if string1[0].isdigit():
        raise ValueError("we need a string")
    else:
       
        while len(string1) !=0:
            counter = 0
            alphabets = ""
            digits = ""
            new_string = ""
            if string1[counter].isalpha():
                alphabets = alphabets + string1[counter]
                counter=counter+1
            elif string1[counter].isdigit():
                digits = string1[counter]
                counter=counter+1
                new_string  = int(digits) * alphabets
                digits = " "
                alphabets = " "     
        return new_string
class Tests(unittest.TestCase):
    data = [
        ("c2", "cc"),
        ("c4", "cccc"),
        ("c4b2", "ccccbb"),
        ("c4b2a3", "ccccbbaaa"),
        ("a2b3c4", "aabbbcccc"),
        ("d11c1", "dddddddddddc"),
        # ("2c", "we need a string") 
        ("k2b3", "kkbbb")
    ]
    def test_stringchange3(self):
        for tests in self.data:
            string1, exp_output = tests
            real_output = stringchange3(string1)
            print("expected:{}, real:{}". format(exp_output, real_output))
            self.assertEqual(exp_output, real_output)
if __name__ == '__main__':
    unittest.main()