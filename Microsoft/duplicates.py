''' removes duplicates from a sorted list '''
import unittest
def rem_dups(dupl_lst):
    unique_lst = []
    for i in dupl_lst:
        if i not in unique_lst:
            unique_lst.append(i)
    return unique_lst


print (rem_dups([2, 2, 5, 7, 7, 8]))
class Tests(unittest.TestCase):
    data = [
        ([2, 8, 8], [2, 8]),
        ([2, 14, 5], [2, 14, 5])

    ]
    def test_rem_dups(self):
        for test in self.data:
            dupl_lst, exp_out = test
            real_out = rem_dups(dupl_lst)
            self.assertEqual(real_out, exp_out)
            print("Expected output: {}, Real ouput: {}" .format(
                exp_out, real_out))
   
if __name__ == '__main__':
    unittest.main()



