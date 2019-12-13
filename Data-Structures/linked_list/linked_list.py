class Node:

  def __init__(self, value = None, next_node = None):
    self.value = value
    self.next = next_node

  def __str__(self):
    return str(self.value)

  def set_value(self, value = None):
    self.value = value

  def set_next(self, next_node = None):
    if next_node == None or isinstance(next_node, Node):
      self.next = next_node
    else:
      raise ValueError


class Linked_List:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        return "linked list."

    def __str__(self):
        """
        Returns string of values
        """
        as_string ='LinkedList :'
        current = self.head
        while current:
            as_string += f'[{current.next}] -> x'
            current = current.next()
        return as_string


    def insert_node(self, value):
        """Inserts the data as a node """
        node = Node(value, self.head)
        self.head = node

    def includes_node(self, value):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next()
        return False


    def append_to_end (self, value):
        if not self.head:
            self.insert_node(value)
            return
        else:
            current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def insert_after(self, search_value, new_value):
        current = self.head
        while current:
            if current.value == search_value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next
        raise ValueError

    def insert_before (self, search_value, new_value):
        if not self.head:
            raise ValueError
        elif self.head.value == search_value:
            self.insert_node(new_value)
            return True
        current = self.head
        while current.next:
            if current.next.value == search_value:
                new_value = Node(new_value)
                new_value.next = current.next
                current.next = new_value
                return True
            current = current.next
        raise ValueError

    def kth_from_end (self, k):
        current = self.head
        temp = current
        for i in range (0, k):
            if temp.next:
                temp = temp.next
            else:
                raise ValueError
        while temp.next:
            temp = temp.next
            current = current.next
        return current.data


