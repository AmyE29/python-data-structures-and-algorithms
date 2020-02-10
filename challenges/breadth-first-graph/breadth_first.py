import inspect, re, collections

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

    def breadth_first(self, vertex):
        """return a collection of nodes in the order they were visited. Display the collection
        """

        explored = set()
        queue = collections.deque()
        queue.appendleft(vertex)
        while queue:
            current = queue.pop(0)
            explored.add(current)
            lst = self.get_neighbors(current)
            if lst:
                for edge in lst:
                    if edge[0] not in explored:
                        queue.appendleft(edge[0])
        return explored
        
    


class Vertex:
    def __init__(self, value):
        self.value = value

# add all nodes
if __name__ =='__main':
graph = Graph()

Pandora = graph.add_node('Pandora')
Arendell = graph.add_node('Arendell')
Monstropolis = graph.add_node('Monstropolis')
Naboo = graph.add_node('Naboo')
Narnia = graph.add_node('Narnia')
Metroville = graph.add_node('Metroville')

    # add all edges
graph.add_edge(Pandora, Arendell, 1)
graph.add_edge(Arendell, Monstropolis, 2)
graph.add_edge(Arendell, Metroville, 3)
graph.add_edge(Monstropolis, Metroville, 4)
graph.add_edge(Monstropolis, Naboo, 5)
graph.add_edge(Metroville, Naboo, 6)
graph.add_edge(Metroville, Narnia, 7)
graph.add_edge(Naboo, Narnia, 8)

print(graph.breadth_first(Pandora))