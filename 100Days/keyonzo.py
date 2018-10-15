import unittest


def character_digit(inp):
    if len(inp) == 0:
        return 0
    if len(inp) == 1:
        return inp
    number=''
    alphabet=''
    results= ''
    for index, i in enumerate(inp):
        if inp[index].isdigit():
            number += inp[index]
        elif inp[index].isalpha():
            alphabet = inp[index]
            results += int(number)*alphabet
            number =''
    return results


class CharacterDigitTestCase(unittest.TestCase):
    data= [
        ("",0),
        ("1a3b2g", "abbbgg"),
        ( "2a3b2g", "aabbbgg"),
        ("12a", "aaaaaaaaaaaa")
    ]

    def test_Character_digit_Test(self):
        for test in self.data:
            inp, exp_output= test
            real_output = character_digit(inp)
            print("Expected Output:{}, Real Output:{}". format(exp_output, real_output))
            self.assertEqual(exp_output, real_output)

if __name__ == '__main__':
    unittest.main()