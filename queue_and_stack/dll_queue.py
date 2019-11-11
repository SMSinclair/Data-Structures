import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue(DoublyLinkedList):
    def __init__(self):
        self.size = 0
        super().__init__()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def enqueue(self, value):
        self.add_to_head(value)
        self.size += 1

    def dequeue(self):
        if self.tail:
            self.size -= 1
            return self.remove_from_tail()
        else:
            return None

    def len(self):
        return self.size
