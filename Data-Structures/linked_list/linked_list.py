class Node():

  def __init__(self, value = None, next_node = None):
    self._value = value
    self._next = next_node

  def __str__(self):
    return str(self._value)

  def set_value(self, value = None):
    self._value = value

  def set_next(self, next_node = None):
    if next_node == None or isinstance(next_node, Node):
      self._next = next_node
    else:
      raise ValueError

  def find_value(self):
    return self._value

  def find_next(self):
    return self._next


class Linked_List:
    def __init__(self, head=None):
        self.head = head
        self._length = 0

    def __repr__(self):
        return "linked list."

    def __str__(self):
        """
        Returns string of values
        """
        data = "The linked list is " + str(self._length) + " long"

        current = self.head
        while current:
            data += str (current)
            current = current.find_next()
        return data

    def get_length(self):
        """Returns the current length of the linked list"""
        return self._length

    def insert_node(self, value):
        """Inserts the data as a node """
        value = Node(value)
        value.next = self.head
        self.head = value

        self._length += 1


    def includes_node(self, value):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.find_value == value:
                return True
            current = current.find_next()
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
            if current._value == search_value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                self._length += 1
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
                self._length += 1
                return True
            current = current.next
        raise ValueError

