import unittest
def match_ends(words):
    count = 0
    strings=[]
    for word in words:
        if len(word) >=2 and word[0] == word[len(word)-1]:
            strings.append(word)
            count+=1
    return count
# //match_ends(["sharon", "Shupan", "love", "kill"])

class Tests(unittest.TestCase):
    data = [
        (["sharos", "shupas", "love", "kill"], 2 ),
        (["sharon", "Shupana", "love", "kill"], 0 )
    ]
    def test_matchend(self):
        for tests in self.data:
            words, exp_output = tests
            real_output = match_ends(words)
            print("exp_output:{}, real_output:{}". format(exp_output, real_output))
            self.assertEqual(real_output, exp_output)

if __name__ == '__main__':
    unittest.main()
