import pytest

from linked_list import Linked_List, Node

# Can successfully instantiate an empty linked list
def test_empty_linked_list():
    instance_of_linked_list = Linked_List()
    assert isinstance(instance_of_linked_list, Linked_List) == True

#tests to create new node
def test_new_node():
  assert isinstance(Node(), Node)

# tests to find node value
def test_find_value_none():
  test_node = Node()
  assert None == test_node._value

# # Can properly insert into the linked list
def test_add_values_to_list(empty_list):
  empty_list.insert_node(Node())
  assert empty_list.get_length() == 1
  empty_list.insert_node(Node())
  empty_list.insert_node(Node())
  assert empty_list.get_length() == 3


def test_get_value_none():
  test_node = Node()
  assert None == test_node._value


def test_find_value():
  test_value = Node(6)
  test_node = Node(test_value)
  assert test_value == test_node._value

def test_find_next_node_node():
  test_value = Node()
  test_value.next = Node()
  assert isinstance(test_value.next, Node)

def test_print_empty_list(empty_list):
  expected = """The linked list is 0 long"""
  assert expected == str(empty_list)

# def test_print_filled_list(empty_list):
#   expected = """The linked list is 2 long"""
#   empty_list.insert_node(1)
#   empty_list.insert_node(2)
#   assert expected == str(empty_list)

def test_insert_after_empty(empty_list):
  with pytest.raises(ValueError):
    empty_list.insert_after(1,2)

def test_insert_after_front(empty_list):
  empty_list.insert_node(1)
  assert empty_list.insert_after(1, 2)
  assert empty_list.includes_node(2)

# def test_value_TRUE(list_two):
#     assert list_two.includes_node('Node_1') == True

# def test_print_list(list_one):
#     assert list_one.__str__() == "The values of this list are ['Node_1']. A total of 1 nodes."

# @pytest.fixture()


@pytest.fixture()
def empty_list():
  return Linked_List()
