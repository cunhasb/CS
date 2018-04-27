import linked_list


class Stack(object):
    def __init__(self, top=None):
        self.ll = linked_list.LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)
        return self.ll

    def pop(self):

        return self.ll.delete_first()
