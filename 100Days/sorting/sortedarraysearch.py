import unittest
def binarysearch(inp):
    first = 0
    last = len(inp) - 1
    found = False
    while first<=last:
        mid = first+last//2
        if inp[mid]>inp[mid+1]:
            return inp[mid+1]
        elif inp[mid]<inp[mid-1]:
            return inp[mid]
        else:
            if inp[mid]<inp[last] and inp[mid]<inp[mid+1]:
                first =  mid+1
            elif inp[mid]<inp[last] and inp[mid]>inp[mid-1]:
                last = mid-1
        return
class CharacterDigitTestCase(unittest.TestCase):
    data= [
     
        ([3,4, 5, 6, 7, 1, 2], 1)
  
    ]

    def test_binarysearch_Test(self):
        for test in self.data:
            inp, exp_output= test
            real_output = binarysearch(inp)
            print("Expected Output:{}, Real Output:{}". format(exp_output, real_output))
            self.assertEqual(exp_output, real_output)

if __name__ == '__main__':
    unittest.main()
    
    