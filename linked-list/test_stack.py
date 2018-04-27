import linked_list
import stack
import unittest


class TestStack(unittest.TestCase):
    """ Test Stack methods in the Stack library"""

    def testInitializeStack(self):
        # Test cases
        # Set up some Elements
        e1 = linked_list.Element(1)
        e2 = linked_list.Element(2)
        e3 = linked_list.Element(3)
        e4 = linked_list.Element(4)

        # Start setting up a Stack
        # Test
        result = stack.Stack(e1)
        self.assertEqual(result.ll.head.value, 1)
        result = stack.Stack(e2)
        self.assertEqual(result.ll.head.value, 2)
        result = stack.Stack(e3)
        self.assertEqual(result.ll.head.value, 3)

    def testPushElement(self):
        # Test cases
        # Set up some Elements
        e1 = linked_list.Element(1)
        e2 = linked_list.Element(2)
        e3 = linked_list.Element(3)
        e4 = linked_list.Element(4)

        # Start setting up a Stack
        # Test
        result = stack.Stack(e1)
        result.push(e2)
        self.assertEqual(result.ll.head.value, 2)
        result.push(e3)
        self.assertEqual(result.ll.head.value, 3)

    def testPopElement(self):
        # Test cases
        # Set up some Elements
        e1 = linked_list.Element(1)
        e2 = linked_list.Element(2)
        e3 = linked_list.Element(3)
        e4 = linked_list.Element(4)

        # Start setting up a Stack
        # Test
        result = stack.Stack(e1)
        result.push(e2)
        result.push(e3)
        self.assertEqual(result.pop().value, 3)
        self.assertEqual(result.pop().value, 2)
        self.assertEqual(result.pop().value, 1)
        self.assertEqual(result.pop(), None)
        result.push(e4)
        self.assertEqual(result.pop().value, 4)


if __name__ == '__main__':
    unittest.main()
