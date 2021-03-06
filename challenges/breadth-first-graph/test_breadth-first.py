import pytest

from breadth_first import Graph, Vertex

def test_add_node():
    graph = Graph()
    expected = 'shoe' 
    actual = graph.add_node('shoe').value
    assert actual == expected

def test_size_empty():
    graph = Graph()
    expected = 0
    actual = graph.size()
    assert actual == expected

def test_size_many():
    graph = Graph() 
    graph.add_node('shoe')
    graph.add_node('boot')
    graph.add_node('sandal')
    graph.add_node('slipper')
    graph.add_node('flipflop')
    graph.add_node('sneaker')
    expected = 6
    actual = graph.size()
    assert actual == expected

def test_add_edge():
    graph = Graph()
    start = graph.add_node('start')
    end = graph.add_node('end')
    graph.add_edge(start, end)

def test_add_edge_weight():
    graph = Graph()
    start = graph.add_node('start')
    end = graph.add_node('end')
    graph.add_edge(start, end, 20)
    expected = (end, 20)
    actual = graph._adjancency_list[start][0]
    assert actual == expected

def test_get_nodes():
    graph = Graph()
    shoe = graph.add_node('shoe')
    boot = graph.add_node('boot')
    sneaker = graph.add_node('sneaker')
    expected = 3
    actual = len(graph.get_nodes())
    assert actual == expected

def test_get_neighbors():
    graph = Graph()
    shoe = graph.add_node('shoe')
    boot = graph.add_node('boot')
    graph.add_edge(shoe, boot, 6)
    neighbors = graph.get_neighbors(shoe)
    expected = (boot, 6)
    assert len(neighbors) ==1
    assert neighbors[0][0].value == 'boot'
    assert isinstance(neighbors[0][0],Vertex)
    assert neighbors [0][1]== 6

def test_get_many_neighbors():
    graph = Graph()
    shoe = graph.add_node('shoe')
    boot = graph.add_node('boot')
    sandal = graph.add_node('sandal')
    flipflop = graph.add_node('flipflop')
    graph.add_edge(shoe, boot, 6)
    graph.add_edge(shoe, sandal, 5)
    graph.add_edge(shoe, flipflop, 12)
    graph.add_edge(boot, sandal, 5)
    neighbors = graph.get_neighbors(shoe)
    expected = [boot, 6 ,flipflop, 12, sandal, 5]
    assert len(neighbors) ==3
    assert neighbors[0][0].value == 'boot'
    assert neighbors[1][0].value == 'sandal'
    assert neighbors[2][0].value == 'flipflop'
    assert isinstance(neighbors[0][0],Vertex)
    assert neighbors [0][1]== 6
    assert neighbors [1][1]== 5
    assert neighbors [2][1]== 12





