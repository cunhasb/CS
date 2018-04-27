import linked_list
import unittest


class TestStack(unittest.TestCase):
    """ Test Stack methods in the Stack library"""

    def testInitializeStack(self):
        # Test cases
        # Set up some Elements
        e1 = Element(1)
        e2 = Element(2)
        e3 = Element(3)
        e4 = Element(4)

        # Start setting up a Stack
        # Test
        stack = Stack(e1)
        self.assertEqual(stack.head.value, 1)
        stack = Stack(e2)
        self.assertEqual(stack.head.value, 2)
        stack = Stack(e3)
        self.assertEqual(stack.head.value, 3)


if __name__ == '__main__':
    unittest.main()
