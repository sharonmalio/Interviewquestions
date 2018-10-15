import unittest
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        node.next=self.head
        self.head = node

    def remove(node):
        values = set()
        prev = None
        while node is not None:
            if node.data in values:
                prev.next = node.next
            else:
                prev = node
                node = node.next
                values.add(node.data)
        return values

class Tests(unittest.TestCase):
    data = [

        (["3->5->6->6->7"],["3->5->6->7"] ), 
        ([3, 3, 6, 6, 7],[3, 6, 7] ),
        ([3, 5, 6, 7],[3, 5, 6, 7] ),

    ]
    def test_remove(self):
        for tests in self.data:
            node, exp_output = tests
            real_output = remove(node)
            print("expected:{}, real:{}" .format(exp_output, real_output))
            self.assertEqual(exp_output, real_output)
if __name__ == '__main__':
    unittest.main()
