class Node:
    """
    Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
    """
    def __init__(self, value, left =None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return
        q = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            current = q.dequeue()
            if current.left:
                q.enqueue(current.left)
            else:
                current.left = node
                return
            if current.right:
                q.enqueue(current.right)
            else:
                current.right = node
                return
         
    def breadth_first(self):
        if not self.root:
            return None
        q = Queue()
        new_list = []
        
        q.enqueue(self.root)
        while not q.is_empty():
            current = q.dequeue()
            if current.left:
                q.enqueue(current.left)
            if current.right:
                q.enqueue(current.right)
            new_list.append(current.value)
        return new_list

    
class Queue:
    def __init__(self):
        self.front = None
        self.end = None

    def enqueue(self, value):
        if isinstance(value, Node):
            node = value
        else:
            node = Node(value)

        if not self.front:
            self.front = node
            self.end = node
            return
        
        if self.end:
            self.end.next = node
            self.end = node  

    def dequeue(self):
        if not self.front:
            return None
        node = self.front
        self.front = node.next
        return node

    def is_empty(self):
        if not self.front:
            return True
        return False

