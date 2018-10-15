
import unittest

def clocktime(timeprints):
    h,m = timeprints.split(':')
    if int(h) < 0 or int(m) < 0 or int(h) > 12 or int(m) > 60:
        raise ValueError
   
    else:
        ma = int(m)*6
        ha = 0.5*((int(h)*60)+int(m))
        angle = abs(ha - ma)
        return angle


class TestClocktimeCase(unittest.TestCase):
   
    data= [
        ("12:30",195),
        ("3:30", 75)

    ]

    def test_clockti(self):
        for test in self.data:
            timeprints, exp_output= test
            real_output = clocktime(timeprints)
            print("Expected Output:{}, Real Output:{}". format(exp_output, real_output))
            self.assertEqual(exp_output, real_output)

if __name__ == '__main__':
    unittest.main()