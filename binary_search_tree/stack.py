"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when implementing a Stack?

RESPONSE TO 3. - The difference between using an array vs a linked list when implementing a Stack lies in establishing the correct relationship between the existing data and data you want to add. With an array, we can simply push the new value to index 0 and increase the indices of the existing data in the array by 1, or we can pop the last value in an array and move on. With a Linked List, however, if we want to add a value, we must create a Node for it and push it to the front, or the head of the Linked List, and connect it to the original head Node. Similarly, if we want to remove a Node, we pop the head Node and then establish the next Node in the sequence as the new head Node.
"""

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         self.size = len(self.storage)
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size = len(self.storage)
#         return self.storage

#     def pop(self):
#         if self.size > 0:
#             popped = self.storage.pop()
#             self.size = len(self.storage)
#             return popped


class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node
    
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # first node in the list 
        self.head = None

    def add_to_end(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node 
        new_node = Node(value)
        # what if the list is empty? 
        if not self.head:
            self.head = new_node
        # what if the list isn't empty?
        else:
            # what node do we want to add the new node to? 
            # the last node in the list 
            # we can get to the last node in the list by traversing it 
            current = self.head 
            while current.get_next() is not None:
                current = current.get_next()
            # we're at the end of the linked list 
            current.set_next(new_node)

    def remove_from_head(self):
        # what if the list is empty?
        if not self.head:
            return None
        # what if it isn't empty?
        else:
            # we want to return the value at the current head 
            value = self.head.get_value()
            # remove the value at the head 
            # update self.head 
            self.head = self.head.get_next()
            return value

class Stack:
    def __init__(self,):
        self.head = None
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size
    
    def push(self, element):
        self.head = Node(element, self.head)
        self.size += 1

    def pop(self):
        if self.size > 0:
            result = self.head.value
            self.head = self.head.next_node
            self.size -= 1
            return result
