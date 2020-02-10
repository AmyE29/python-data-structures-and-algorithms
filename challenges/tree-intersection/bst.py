class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree:
    def __init__(self, value=None):
        self._root = value

    def pre_order(self, current=None, output_array=None):
        if output_array == None:
            output_array = []
        
        if not current:
            current = self._root

        output_array.append(current.value)

        if current.left:
            self.pre_order(current.left, output_array)

        if current.right:
            self.pre_order(current.right, output_array)

        return output_array

    def in_order(self, current=None, output_array=None):
        if output_array == None:
            output_array=[]
        if not current:
            current = self._root

        if current.left:
            self.in_order(current.left, output_array)

        output_array.append(current.value)

        if current.right:
            self.in_order(current.right, output_array)

        return output_array

    def post_order(self, current=None, output_array=None):
        if output_array == None:
            output_array=[]

        if not current:
            current = self._root

        if current.left:
            self.post_order(current.left, output_array)

        if current.right:
            self.post_order(current.right, output_array)

        output_array.append(current.value)

        return output_array


  
class BinarySearchTree(BinaryTree):
    # def __init__(self):

    def add(self, value, current=None):

        if not self._root:
            self._root = Node(value)
            return

        if current is None:
            current = self._root

        if current:
            if value < current.value:
                if not current.left:
                    current.left = Node(value)
                else:
                    self.add(value, current.left)

            if value >= current.value:
                if not current.right:
                    current.right = Node(value)
                else:
                    self.add(value, current.right)

    def contains(self, value, curr=None):
        if not self._root:
            return False

        if not curr:
            curr = self._root

        if value == curr.value:
            return True

        if value < curr.value:
            if curr.left:
                return self.contains(value, curr.left)

        if value > curr.value:
            if curr.right:
                return self.contains(value, curr.right)

        return False