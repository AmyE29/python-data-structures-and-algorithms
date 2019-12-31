class Node:
    """
    Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """
    Define a method for each of the depth first traversals called preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately.
    """
    def __init__(self):
        self.root = None

    def pre_order(self, node=None, arr=[]):
        """
        Returns an array of the values, ordered from the start, going far left, then finishing to the right.
        """
        node = node or self.root
        if node.left:
            self.pre_order(node.left, arr)

        if node.right:
            self.pre_order(node.right, arr)

        return arr


    def post_order(self, node=None, arr=[]):
        """
        Returns an array of the values, ordered starting from the far left, traversing to the top, then finishing to the right.
        """
        node = node or self.root
        if node.left:
            self.post_order(node.left, arr)

        if node.right:
            self.post_order(node.right, arr)

        arr.append(node.value)
        return arr


    def in_order(self, node=None, arr=[]):
        """
        Returns an array of the values, ordered starting from the far left, traversing to the far right, then finishing to at the root.
        """
        node = node or self.root
        if node.left:
            self.in_order(node.left, arr)

        arr.append(node.value)

        if node.right:
            self.in_order(node.right, arr)
        return arr

class BinarySearchTree(BinaryTree):
    def add(self, value):
        """
        Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree.
        """
        if not self.root:
            self.root = None
            return

        node = Node(value)

        if value < self.root.value:
            if not self.root.left:
                self.root.left = node
        else:
            if not self.root.right:
                self.root.right = node


    def contains(self, value, node= None):
        """
        Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.
        """
        node = node or self.root
        if not self.root:
            return False

        if node.value == value:
            return True

        if value < node.value:
            if node.left:
                return self.contains(value, node.left)
            else:
                return False
        else:
            if node.right:
                return self.contains(value, node.right)
            else:
                return False