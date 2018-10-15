# given 1a3b2g give an output of abbbgg
# TALK
# what kind of input is it
# what is the relationship between the input and the output
# what are we outputting
# how do we deal with invalid inputs
# do we hamndle all the other inputs or it is specific to this.
# Examples
# input class            output
#[""]  empty string     0 or null
#["1"]  invalid        exception
#["1a"]  simple string           a
#["1a3b2g"]             abbbgg
#["a"]      invalid     exception
#["1a23b40c"] complex   a
# Bruteforce
#
# optimization
# is there a btter code?
# space complexity and time complexity
# walk through
# implement
# a*2 = aa
# 1a3b
# https://stackoverflow.com/questions/13673781/splitting-a-string-where-it-switches-between-numeric-and-alphabetic-characters
# https://stackoverflow.com/questions/24660545/splitting-strings-in-a-series-when-a-number-is-encountered-in-python
# we can try and use a regular expression

import unittest
def character_digit(inp):
    if len(inp) == 0 or all(x.isdigit() for x in inp) :
        raise Exception('Invalid input')
    elif all( x.isalpha() for x in inp ):
        print (inp)
        return inp
    else: 
        num = 0
        alphabet = ''
        results = ''
        for index, i in enumerate(inp):
            if i.isdigit():
                num = num * 10 + int(i)  
            elif i.isalpha():
                alphabet += i   
                results += num * alphabet
                num = 0
                alphabet = ''
        print(results)
        return results

character_digit("4h2g")

class Tests(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(character_digit("4h2g"),("hhhhgg"))
        

if __name__ == '__main__':
    unittest.main()


