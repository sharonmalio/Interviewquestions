import unittest
def sortmove(words):
    list1 = []
    list2 = []

    for word in words:
        if word.startswith("x"):
            list1.append(word)
            return  list1
        else:
            list2.append(word)
            return list2
        mergedlist = sorted(list1)+sorted(list2)
        return mergedlist


class Tests(unittest.TestCase):
    data = [
       
        (["xcfd", "sggr", "rejdj", "xfgs", "adehf"], ["xcfd", "xfgs","adehf", "rejdj", "sggr"])
    ]
    def test_matchend(self):
        for tests in self.data:
            words, exp_output = tests
            real_output = sortmove(words)
            print("exp_output:{}, real_output:{}". format(exp_output, real_output))
            self.assertEqual(real_output, exp_output)

if __name__ == '__main__':
    unittest.main()
