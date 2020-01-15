class Node():

  def __init__(self, value = None, next_node = None):
    self._value = value
    self._next = next_node
    self._length = 0

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
  
  def get_length(self):
     """Returns the current length of the linked list"""
    return self._length 
  


class LinkedList:
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
    

    def insert(self, value):
        """Inserts the data as a node """
        value = Node(value)
        value.next = self.head
        self.head = value

        self._length += 1

def merge_list(ll_one, ll_two):
    """ Merges two linked lists together as a zipped list."""
    current_one = ll_one.head
    current_two = ll_two.head

    while current_one and current_two:
        one_next = current_one.next
        two_next = current_two.next

        current_one.next = current_two
        if one_next == None:
            break
        current_two.next_node = one_next

        current_one = one_next
        current_two = two_next
  
    return ll_one.head