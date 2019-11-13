import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack(DoublyLinkedList):
    def __init__(self):
        self.size = 0
        super().__init__()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.head:
            self.size -= 1
            return self.remove_from_head()

    def len(self):
        return self.size
