from tree import BinaryTree, BinarySearchTree

def test_tree():
    """Can successfully instantiate an empty tree"""
    tree = BinaryTree()
    assert tree.root is None

def test_root():
    """Can successfully instantiate a tree with a single root node"""
    tree = BinarySearchTree()
    tree.add(1)
    assert tree.root.value == 1

def test_add_left_right():
    """Can successfully add a left child and right child to a single root node"""
    tree = BinarySearchTree()
    tree.add(45)
    tree.add(15)
    tree.add(60)
    assert tree.root.value==45
    assert tree.left.value==15
    assert tree.right.value==60

def pre_order():
    """Can successfully return a collection from a preorder traversal"""
    tree = BinarySearchTree()
    tree.add(45)
    tree.add(15)
    tree.add(60)
    assert pre_order() == [45,15,60]

def in_order():
    """Can successfully return a collection from an inorder traversal"""
    tree = BinarySearchTree()
    tree.add(45)
    tree.add(15)
    tree.add(60)
    assert in_order() == [15,45,60]

def post_order():
    """Can successfully return a collection from an postorder traversal"""
    tree = BinarySearchTree()
    tree.add(45)
    tree.add(15)
    tree.add(60)
    assert post_order() == [15,60,45]
