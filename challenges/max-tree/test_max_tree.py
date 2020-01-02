import pytest
from max_tree import BinaryTree
def test_maximum_value():
    new_tree = BinaryTree()
    expected = 11
    new_tree.add(2)
    new_tree.add(7)
    new_tree.add(5)
    new_tree.add(2)
    new_tree.add(6)
    new_tree.add(9)
    new_tree.add(5)
    new_tree.add(11)
    new_tree.add(4)
    assert new_tree.find_maximum_value() == expected