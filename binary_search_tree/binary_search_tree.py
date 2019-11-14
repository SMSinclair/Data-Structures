import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # < go left
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        
        # >= go right
        if value >= self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # to search a given key in binary search tree, we first compare it with root, 
        # if the key is present at root, we return root. If key is greater than root's key, 
        # we recur for right subtree of root node. Otherwise we recur for the left subtree.
        if target == self.value:
            return True

        if target > self.value:
            return self.right.contains(target)
        else:
            return self.left.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        # go right until you can go right no further
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #visit each node exactly one time
        # go left until you can't aqnymore, then
        # go back and go right
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

a = BinarySearchTree(7)
a.insert(8)
a.insert(6)
a.insert(5)
# print(a.left.value)
# print(a.value)
# print(a.right.value)
# print(a.left.left.value)

# print(a.contains(5))

# print(a.get_max())

a.for_each(print)