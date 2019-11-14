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
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        
        # >= go right
        else:
            if not self.right:
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
            if not self.right:
                return False
            return self.right.contains(target)
        else:
            if not self.left:
                return False
            return self.left.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        # go right until you can go right no further
        if not self.right:
            return self.value
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
    def in_order_print(self, node): # why was this passing a node argument?
        #self.for_each(print)
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # make a queuue
        # add to queue
        # pop head if not empty, add children
        q = Queue()
        q.enqueue(node)
        while(q.len() != 0):
            node = q.dequeue()
            print(node.value)
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(node)
        while(len(s)!=0):
            popped = s.pop()
            print(popped.value)
            if popped.left:
                s.push(popped.left)
            if popped.right:
                s.push(popped.right)
            
            
        
        # s = Stack()
        # prev = None
        # while(node):
        #     s.push(node)
        #     node=node.left
        # while(len(s) != 0):
        #     node = s.pop()
        #     print(node.value)
        #     if node.right:
        #         if node.right != prev:
        #             s.push(node.right)
        #     if node.left:
        #         if node.left != prev:
        #             s.push(node.left)
        #     prev = node

            

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# a = BinarySearchTree(7)
# a.insert(8)
# a.insert(6)
# a.insert(5)
# # print(a.left.value)
# # print(a.value)
# # print(a.right.value)
# # print(a.left.left.value)

# # print(a.contains(5))

# # print(a.get_max())

# # a.for_each(print)
# # a.in_order_print()
# # a.bft_print(a)
# a.dft_print(a)

# bst = BinarySearchTree(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.dft_print(bst)

