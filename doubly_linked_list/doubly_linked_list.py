"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is pointing to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # first, we create the new node and set it to a variable
        new_node = ListNode(value)
        # next, we increase the length by 1 to account for the new node
        self.length += 1
        # now we check to see if a head and tail node exist, and if not, we set the new node to be both the head and tail
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # otherwise, if there is more than one node we set the old head to be the next node after the new node
            new_node.next = self.head
            # then we set the new node to be the node before the old head
            self.head.prev = new_node
            # and finally, we set the new node to be the current head
            self.head = new_node


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # first, we set the value of the current head to a variable
        value = self.head.value
        # then we delete the current head node and return the value of the deleted node
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # first, we create a new node and set it to a variable
        new_node = ListNode(value)
        # next, we increase the length by 1 to account for the new node
        self.length += 1
        # now we check to see if a head and tail node exist, and if they don't, we set the new node to be the head and tail simultaneously
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # otherwise, if there is more than one node, we set the old tail to be the previous node before the new node
            new_node.prev = self.tail
            # then we set the new node to be next node after the old tail
            self.tail.next = new_node
            # finally, we set the new node to be the current tail
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # first, we set the value of the current tail node to a variable
        value = self.tail.value
        # then we delete the tail node and return the value of the deleted node
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # first, we check to see if the node in question is already the head node
        if node is self.head:
            return
        # if the node in question is not the head, we call the add_to_front method which creates a new head and sets the value to be that of the node in question
        self.add_to_head(node.value)
        # then we delete the node in question
        self.delete(node)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # first, we check to see if the node in question is already the tail node
        if node is self.tail:
            return
        # if the node in question is not the tail, we call the add_to_end method which creates a new tail and sets the value to be that of the node in question
        self.add_to_tail(node.value)
        # finally, we delete the node in question
        self.delete(node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # first, we reduce the length by 1 to account for the node we're about to delete
        self.length -= 1
        # is this the only node?
        # if so, we set the value of the head/tail to None
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # is this the head?
        # if so, we set the new head to the value after the node in question, then call the node.delete() method to delete the node in question and make sure the remaining nodes are pointing at the correct nodes
        elif node is self.head:
            self.head = node.next
            node.delete()
        # is this the tail?
        # same goes for the tail
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        # is this in the middle?
        # then we simply call the node.delete() method to delete the node in question and make sure the remaining nodes are pointing at the correct nodes
        else:
            node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # first, we set the current head to a variable
        current_node = self.head
        # then we set the value of the head to a variable in order to track the maximum as we traverse the linked list
        max_value = self.head.value
        # next we create a loop to traverse the list until it reaches the end of the list
        while(current_node is not None):
            # now we check the value of each node and compare it to the current maximum
            if current_node.value > max_value:
                # if the value of the node the loop is looking at is greater than the maximum, we set the value to the variable tracking the maximum value
                max_value = current_node.value
            # then we set the current node to the next one in order to traverse the list
            current_node = current_node.next
        # once the loop is finished we return the maximum value
        return max_value
