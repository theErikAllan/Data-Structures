"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when implementing a Queue?

RESPONSE TO 3. - The difference between using an array vs a linked list when implementing a Queue lies in establishing the correct relationship between the existing data and data you want to add. With an array, we simply enqueue a value to the end of an array (i[len(array) - 1]) or dequeue a value from the front of the array (i[0]). However, with a Linked List, if we want to enqueue a value, we must create a new Node at the end, or tail of the Linked List and connect it to the previous tail Node. Additionally, if we want to remove a value, we dequeue the Node at the front, or head of the Linked List, and we establish the next Node as the new head of the Linked List.

   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#         self.front = 0
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def dequeue(self):
#         if self.size > 0:
#             value = self.storage[self.front]
#             self.storage[self.front] = None
#             self.front += 1
#             self.size -= 1
#             return value

class EmptyError(Exception):
    pass

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


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
        self.head = None
        self.tail = None
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        new = Node(value, None)
        if self.size == 0:
            self.head = new
        else:
            self.tail.next_node = new
        self.tail = new
        self.size += 1


    def dequeue(self):
        if self.size == 0:
            return
        result = self.head.value
        self.head = self.head.next_node
        self.size -= 1
        if self.size == 0:
            self.tail = None
        return result