class Node(object):

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return self.data

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class Linked_List:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        return "linked list."

    def __str__(self):
        """
        Returns string of values
        """
        data = self.return_list()
        # return f"The values are {data}"

    def insert_node(self, data):
        """Inserts the data as a node """
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def includes_node(self, value):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def return_list(self):
        try:
            current = self.head
            collection_of_values = []
            while current:
                collection_of_values.append(str(current))
                current = current.next_node
            return collection_of_values

new_list = Linked_List()
new_list.insert_node('Node_1')
new_list.insert_node('Node_2')
