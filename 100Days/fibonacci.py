import unittest
def fibonacci(n):
    if n<0:
        raise ValueError("number can not be below 0")
    elif n ==1:
        return 0

    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci2(n): 
    a = 0
    b = 1
    if n<2:
        return n
    else: 
        for i in range(2,n+1): 
            c = a + b 
            a = b 
            b = c 
        return b 
  
class Tests(unittest.TestCase):
    data = [
        (9, 34),
        (1, 0),
        (2, 1),
        (8,21)
    ]

    def test_fibonacci(self):
        for test in self.data:
            n, expected_output = test
            real_output = fibonacci2(n)
            print("Expected Output:{}, Real Output:{}" .format(expected_output, real_output))
            self.assertEqual(expected_output, real_output)

if __name__ == "__main__":
    unittest.main