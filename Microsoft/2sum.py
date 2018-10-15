import unittest


def twoSum(numarr, target):
    if type(numarr) is not list:
        raise ValueError

    for i, num in enumerate(numarr):
        othernum = target - num
        if (othernum in numarr and numarr.index(othernum) != i):
            return [num, othernum]

class Tests(unittest.TestCase):
    data = [
        ([2, 8, 19], 10, [2, 8]),
        ([2, 14, 5], 7, [2, 5])
    ]

    def test_checktrue(self):
        for test in self.data:
            numarr, target, exp_output = test
            real_output = twoSum(numarr, target)
            self.assertEqual(real_output, exp_output)
            print("Expected output: {}, Real ouput: {}" .format(
                exp_output, real_output))

    def test_ValueError(self):
        self.assertRaises(ValueError, twoSum, 5, 8)


if __name__ == '__main__':
    unittest.main()
