# Class representing an element of a LinkedList
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


''' New class representing singly linked lists, it takes an element as the head,
if it does not contain one it will be set to None'''


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # method to add elements
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
