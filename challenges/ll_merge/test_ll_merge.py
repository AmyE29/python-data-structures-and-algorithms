import pytest
from ll_merge import LinkedList, Node, merge_list

@pytest.fixture()
def ll_five():
    empty_list = LinkedList()
    empty_list.insert(9)
    empty_list.insert('a')
    empty_list.insert(8)
    empty_list.insert('c')
    empty_list.insert(True)
    return empty_list

@pytest.fixture()
def ll_three():
    empty_list = LinkedList()
    empty_list.insert(2)
    empty_list.insert('a')
    empty_list.insert(3)
    return empty_list

@pytest.fixture()
def ll_none():
    return LinkedList()

@pytest.fixture()
def ll_one():
    empty_list = LinkedList()
    empty_list.insert('a')
    return empty_list
@pytest.fixture()
def ll_eight():
    empty_list = LinkedList()
    empty_list.insert(4)
    empty_list.insert('z')
    empty_list.insert(2)
    empty_list.insert('c')
    empty_list.insert(True)
    empty_list.insert('w')
    empty_list.insert(7)
    empty_list.insert(1)
    return empty_list

@pytest.fixture()
def ll_six():        
    empty_list = LinkedList()
    empty_list.insert(9)
    empty_list.insert('h')
    empty_list.insert(8)
    empty_list.insert('p')
    empty_list.insert(False)
    empty_list.insert(6)
    return empty_list

# Test that fixture imputs are Linked Lists
def test_is_ll(ll_five):
    assert isinstance(ll_five, LinkedList)

# Test none
def test_merge_none(ll_none):
    new_ll = merge_list(ll_none, ll_none)
    assert new_ll.get_length() == ''

# Test one
def test_merge_one(ll_one):
    empty_list = LinkedList()
    empty_list.insert('b')
    new_ll = merge_list(ll_one, empty_list)
    assert new_ll.get_length() == 'a -> b -> '

# Test many
def test_merge_many(ll_six, ll_eight):
    new_ll = merge_list(ll_six, ll_eight)
    assert new_ll.get_length() == '6 -> 1 -> False -> 7 -> p -> w -> 8 -> True -> h -> c -> 9 -> 2 -> z -> 4 -> '
# Test different lengths
def test_merge_different_length(ll_three, ll_five):
    new_ll = merge_list(ll_five, ll_three)
    assert new_ll.get_length() == 'True -> 3 -> c -> a -> 8 -> 2 -> a -> 9 -> '