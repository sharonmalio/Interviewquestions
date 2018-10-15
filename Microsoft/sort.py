''' Insertion sort'''
''' TALK/ LISTEN'''
# Input -> array
# Output -> sorted array
# How to deal with duplicates either remove or keep in sorted array
# Dealing with invalid input i.e where input is not an array
''' EXAMPLES '''
# An already sorted array    return arr
# Empty array                raise exception
# Array len of 1             arr
# Array                      sorted arr

''' BRUTE FORCE '''
#loop through the arr [4, 8, 1, 7]
#for each pair sort [4, 8, 1, 7], []
''' OPTIMIZE '''
''' WALK THROUGH '''
''' IMPLEMENT '''
''' TEST '''

import unittest
def insert_sort(arr):
    if not isinstance(arr, list):
        raise ValueError
    else:
        if len(arr) == 0:
            raise Exception ('Empty string')
        elif len(arr) == 1:
            return arr
        else:
            for i in range(len(arr)):
                current = arr[i]
                temp = i-1
                while temp >= 0 and current < arr[temp]:
                    arr[temp + 1] = arr[temp]
                    temp -= 1
                arr[temp+1] = current
            return arr

class Test(unittest.TestCase):
    def test_unsorted(self):
        self.assertEqual(insert_sort([8, 1, 4]),[1, 4, 8])

if __name__ == '__main__':
    unittest.main()

