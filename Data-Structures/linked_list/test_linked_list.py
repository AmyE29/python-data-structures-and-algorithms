import pytest
from linked_list import Linked_List, Node

# Can successfully instantiate an empty linked list
def test_empty_linked_list():
    instance_of_linked_list = Linked_List()
    assert isinstance(instance_of_linked_list, Linked_List) == True

# Can properly insert into the linked list
def test_instance_of_node():
    assert Node('Node_1').value == 'Node_1'

def test_one_item_in_list(list_one):
    assert list_one.head and Node('Node_1').next_node == None

def test_two_items_into_new_list(list_two):
    assert str(list_two.head) == 'Node_2'

def test_value_TRUE(list_two):
    assert list_two.includes_node('Node_1') == True

def test_print_list(list_one):
    assert list_one.__str__() == "The values of this list are ['Node_1']. A total of 1 nodes."

@pytest.fixture()
def list_one():
    new_list = Linked_List()
    new_list.insert_node('Node_1')
    return new_list

@pytest.fixture()
def list_two():
    new_list = Linked_List()
    new_list.insert_node('Node_1')
    new_list.insert_node('Node_2')
    return new_list
