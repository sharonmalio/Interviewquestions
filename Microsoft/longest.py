import unittest

def longest(input_str):
    longest_subtring = ''
    

#     longest_str = ''
#     if not isinstance(input_str, str) or len(input_str) == 0:
#         raise Exception ('Invalid input')
#     else:
#         # print(input_str)
#         i = j = 0
#         max_len = 0
#         sub = set()
#         while (i < len(input_str)) and (j < len(input_str)):
#             if input_str[j] not in sub:
#                 sub.add(input_str[j])
#                 j += 1
#                 max_len = max(max_len, j-i)
#             else:
#                 sub.remove(input_str[j])
#                 i += 1
#     return max_len
# print(longest('aghjvacf'))

# class Tests(unittest.TestCase):
#     def test_single_char(self):
#         self.assertEqual(longest('a'), 1)
    
#     def test_simple_str(self):
#         self.assertEqual(longest('aghjvacf'),7)

# if __name__ == '__main__':
#     unittest.main()