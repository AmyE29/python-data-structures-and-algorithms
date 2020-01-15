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

class Queue:
    """
    A Queue call that has a front property and created an empty Queue when instantiated
    A method called enqueue which takes any value as an arguement and adds a new node with that value to the back of the queue
    A method called dequeue that removes the node from the front of the queue and returns the nodes value
    A method called peek that returns the value of the node located in the front of the queue without removing it from the queue
    A method called is_empty that returns a True or False
    """


    def __init__(self, front=None):
        self.front = front
        self.end = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.end == None:
            self.front = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node

    def dequeue(self):
        try:
            first_node = self.front
            self.front = first_node.next
            first_node.next = None
            return first_node.value
        except AttributeError:
            return None

    def peek(self):
        try:
            return self.front.value
        except AttributeError:
            return None

    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False

if __name__ == "__main__":
    new_stack = Stack()
    print(new_stack)
