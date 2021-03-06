class Graph:
    def __init__(self):
        self._adjancency_list = {}

    def add_node(self, value):
        v = Vertex(value)
        self._adjancency_list[v] = []
        return v
    
    def size(self):
        return len(self._adjancency_list)
        

    def add_edge(self, start_V, end_V, weight=0):
        if start_V not in self._adjancency_list:
            raise KeyError('There is no start vertex')
        if end_V not in self._adjancency_list:
            raise KeyError('There is no end vertex')
        adjancenies = self._adjancency_list[start_V]
        adjancenies.append((end_V, weight))

    def get_nodes(self):
        return self._adjancency_list.keys()

    def get_neighbors(self, vertex):
        return self._adjancency_list[vertex]

class Vertex:
    def __init__(self, value):
        self.value = value