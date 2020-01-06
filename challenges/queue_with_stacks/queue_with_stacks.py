
class Node:
    """
    Node class that has properties for the value stored in the Node, and a pointer to the next node.
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


class Stack:
    """
    A Stack class that has a top property and creates an empty stack when instantiated
    A method called push which takes in any value and adds s new node with that value to the top of the stack
    A method called pop that removes the node from the top of the stack and returns the nodes value
    A methon called peek that returns the value of the node located on top of the stack without removing it from the stack
    An is_empty method returns True or False if the stack is empty
    """

    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        new_node = Node(value, self.top)
        self.top = new_node

    def pop(self):
        try:
            top_node = self.top
            self.top = top_node.next
            top_node.next = None
            return top_node.value
        except AttributeError:
            return None

    def peek(self):
        try:
            return self.top.value
        except AttributeError:
            return None


    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False

class PseudoQueue:
    def __init__(self, stack1):
        """this PseudoQueue class will implement the standard queue interface using 2 Stack objects. """
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        """inserts value into the PseudoQueue, using a first-in, first-out approach.."""
        self.stack1.push(value)

    def dequeue(self):
        """"extracts a value from the PseudoQueue, using a first-in, first-out approach. """

        if self.stack1.top == None:
            raise Exception
        while self.stack1.top != None:
            popped_value = self.stack1.pop()

            self.stack2.push(popped_value)

        stack2_popped = self.stack2.pop()

        while self.stack2.top != None:
            self.stack1.push(self.stack2.pop())
        return stack2_popped


if __name__ == "__main__":
    new_stack = Stack()
    print(new_stack)