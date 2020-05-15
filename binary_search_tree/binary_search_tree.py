from queue import Queue
from stack import Stack

"""
Binary search trees are a data structure that enforce an ordering over the data they store. That ordering in turn makes it a lot more efficient at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each` on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods on the BSTNode class.
"""
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # first, we check to see if the desired value is less than that of the current node so we can decide if the desired value needs to be placed to the left or right of the current node
        if value < self.value:
            # if the desired value is less than that of the current node, we want to check to see if there's a node to the left already, and if there is not, we call the BinarySearchTree class to create a new tree with the desired value as the root node of the new tree
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                # otherwise, we know there's a node there already so we recursively call the insert() method to go through this process again until we reach a leaf
                self.left.insert(value)
        # if the desired value not less than the value of the current node, it must be greater than or equal to it, so we go to the right
        else:
            # if the desired value is greater than or equal to that of the current node, we want to check to see if there's a node to the right already, and if there is not, we call the BinarySearchTree class to create a new tree with desired value as the root node of the new tree
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                # otherwise, we know there's a node there already so we recursively call the insert() method to go through this process again until we reach a leaf
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # first, we check to see if the target value is equal to the value in the root node we're looking at
        if target == self.value:
            return True
        # if the target value doesn't match the value of the current root node, we check to see if it's less than the current root node to decide if the target value is on the left side of the tree
        if target < self.value:
            # next, we check to see if there is a node to the left, and if there is not, we return None
            if self.left is None:
                return False
            else:
                # if there is a node to the left, then we recursively call the contains() method to start the process over again with the left node as the new root node
                return self.left.contains(target)
        # if the target value is not equal to or less than the value in the current root node, we assume it is greater than and check the node to the right of the current root node
        else:
            # if no node exists to the right, we return False
            if self.right is None:
                return False
            else:
                # if there is a node to the right, then we recursively call the contains() method to start the process over again with the right node as the new root node
                return self.right.contains(target)
    
    # this is an example of what contains() might look like if it was written as an iterative method instead of recursive
    def contains_iteratively(self, target):
        # first, we set the current node to a variable
        current = self
        # second, we create a while loop that will help us traverse the tree as long as the current node exists
        while current is not None:
            # in the loop, we first check to see if the target value is less than the value of the current node, and if it is, we set the left node as the current node which allows us to move down the tree in the left direction
            if target < current.value:
                current = current.left
            # if the target value is not less than the value of the current node, we check to see if it is greater, and if it is, we set the right node as the current node which allows us to move down the tree in the right direction
            elif target > current.value:
                current = current.right
            # otherwise, we assume the target value is equal to the value of the current node so we return True and the loop ends
            else:
                return True
        # if the iterative method is unable to find the target value in any of the tree's nodes, we return False
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        # to find the max value in the tree, we assume it will be to the right since any node to the left will contain a value that is less than that of the node we're looking at
        if self.right:
            # if a node exists to the right, then we recursively call the get_max() method to start the process over again
            return self.right.get_max()
        else:
            # if no node exists to the right, then we have found the right most mode, and therefore the maximum value in the tree
            return self.value
        
    # this is an example of what get_max() might look like if it was written as an iterative method instead of recursive
    def get_max_iteratively(self):
        # first, we set the value of the current node to a variable to track to the current maximum value
        max = self.value
        # then we set the current node to a variable which will help us track which node we're looking at
        current = self
        # next, we create a while loop that will traverse the tree
        while current:
            # for each node we look at, we then check to see if the value of the current node is greater than the current maximum value
            if current.value > max:
                # if the value of the current node is greater than the max variable, we set the value of the current node to be the new max value
                max = current.value
            # to traverse to the next node, we set the right node to be the new current node and the loop starts over - so the loop will break when current.right is None
            current = current.right
        # finally, once the loop is done, we return the final value of max
        return max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # first, we need to call fn() on the value of the current root node
        fn(self.value)
        # then we check to see if a node to the left exists, and if it does, we recursively call the for_each() method for that node
        if self.left:
            self.left.for_each(fn)
        # we also check to see if a node to the right exists, and if it doesn, we recursively call the for_each() method for that node
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Use QUEUE for breadth first because First In First Out
        queue = Queue()
        queue.enqueue(node)
        while queue.size > 0:
            # print(queue.head.value.value)
            tracking_node = queue.dequeue()
            print(tracking_node.value)
            if tracking_node.left:
                queue.enqueue(tracking_node.left)
            if tracking_node.right:
                queue.enqueue(tracking_node.right)
            # print(tracking_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Use STACK for depth first because Last In First Out
        stack = Stack()
        stack.push(node)
        while stack.size > 0:
            print(stack.head.value.value)
            tracking_node = stack.pop()
            if tracking_node.left:
                stack.push(tracking_node.left)
            if tracking_node.right:
                stack.push(tracking_node.right)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
